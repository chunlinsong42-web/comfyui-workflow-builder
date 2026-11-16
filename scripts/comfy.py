#!/usr/bin/env python
"""comfy.py - build, validate, convert, run ComfyUI workflows on the remote box.

Target: ComfyUI reached through an SSH tunnel (default local 127.0.0.1:16006
-> remote 127.0.0.1:6006). Configure instance.json (see instance.example.json),
then start the tunnel first:

    python comfy.py tunnel            # keep running in a background shell

Commands
    tunnel  [--local-port 16006] [--remote-port 6006]
    stats
    catalog                       # fetch /object_info into <skill>/.cache
    nodes   <keyword>             # search catalog for node types
    build   recipe.json [-o wf.json]
    validate wf.json
    convert wf.json [-o prompt.json]
    submit  wf.json [--wait] [--download DIR]
    workflows                     # list remote workflow files (needs SSH)

Recipe format (compact authoring DSL, see references/workflow-format.md):

{
  "title": "示例",
  "nodes": {
     "unet":   {"type": "UNETLoader", "widgets": {"unet_name": "..."}},
     "sampler":{"type": "KSampler", "widgets": {"steps": 8, "cfg": 1}}
  },
  "links": ["unet.MODEL -> sampler.model", "sampler.LATENT -> decode.samples"]
}

Link syntax: "<alias>.<output name|output type|index>" -> "<alias>.<input name>".
"""
import argparse
import json
import os
import socket
import sys
import threading
import time
import urllib.parse
import urllib.request
import uuid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CACHE = os.path.join(ROOT, ".cache")
CONFIG_PATH = os.path.join(ROOT, "instance.json")


def load_instance():
    """Connection settings: environment variables override instance.json."""
    cfg = {}
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
                cfg = json.load(fh)
        except Exception as exc:
            die("cannot read %s: %s" % (CONFIG_PATH, exc))

    def pick(env_key, key, default=None):
        value = os.environ.get(env_key)
        if value is None or value == "":
            value = cfg.get(key, default)
        return value

    return {
        "host": pick("COMFY_SSH_HOST", "host"),
        "port": int(pick("COMFY_SSH_PORT", "port", 22)),
        "user": pick("COMFY_SSH_USER", "user", "root"),
        "password": pick("COMFY_SSH_PASSWORD", "password"),
        "local_port": int(pick("COMFY_TUNNEL_PORT", "local_port", 16006)),
        "remote_port": int(pick("COMFY_REMOTE_PORT", "remote_port", 6006)),
    }


def require_instance():
    inst = load_instance()
    missing = [k for k in ("host", "password") if not inst.get(k)]
    if missing:
        die("missing %s - copy instance.example.json to instance.json and fill it in "
            "(or set COMFY_SSH_HOST / COMFY_SSH_PASSWORD)." % ", ".join(missing))
    return inst


def base_url():
    override = os.environ.get("COMFY_BASE_URL")
    if override:
        return override
    return "http://127.0.0.1:%d" % load_instance()["local_port"]

SCALAR_TYPES = {"INT", "FLOAT", "STRING", "BOOLEAN", "COMBO", "COMBO_OPTION"}
OUT_NODE_TYPES = {
    "SaveImage", "SaveImageAdvanced", "SaveImageKJ", "PreviewImage", "SaveVideo", "SaveWEBM",
    "SaveAnimatedWEBP", "SaveAnimatedPNG", "VHS_VideoCombine", "SaveAudio", "SaveAudioMP3",
    "SaveAudioAdvanced", "PreviewAudio", "ZealmanVideoOutput", "SaveGLB", "SaveImageWebsocket",
}


# ---------------------------------------------------------------- utilities
def die(msg, code=1):
    sys.stderr.write("error: %s\n" % msg)
    sys.exit(code)


def jload(path):
    with open(path, "r", encoding="utf-8") as fh:
        return json.load(fh)


def jsave(obj, path):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2)
    return path


def http(method, path, payload=None, timeout=60):
    url = base_url().rstrip("/") + path
    data = None
    headers = {"Content-Type": "application/json"}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    if not url.startswith("http"):
        die("invalid ComfyUI URL: %s" % url)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return resp.status, (json.loads(body) if body else {})
    except urllib.error.HTTPError as exc:
        body = exc.read()
        try:
            return exc.code, json.loads(body)
        except Exception:
            return exc.code, {"raw": body.decode("utf-8", "replace")}
    except urllib.error.URLError as exc:
        die("cannot reach ComfyUI at %s (%s). Is `comfy.py tunnel` running, or "
            "COMFY_BASE_URL set?" % (url, exc.reason))


def catalog_path():
    return os.path.join(CACHE, "object_info.json")


def load_catalog(auto_fetch=True):
    p = catalog_path()
    if os.path.exists(p):
        return jload(p)
    if not auto_fetch:
        die("no node catalog yet - run `python comfy.py catalog` first (needs tunnel)")
    status, data = http("GET", "/object_info", timeout=120)
    if status != 200 or not data:
        die("cannot fetch /object_info (HTTP %s). Is the tunnel running?" % status)
    os.makedirs(CACHE, exist_ok=True)
    jsave(data, p)
    return data


# ---------------------------------------------------------------- spec helpers
def input_entries(spec):
    inp = spec.get("input") or {}
    out = []
    for name, val in (inp.get("required") or {}).items():
        out.append((name, val, True))
    for name, val in (inp.get("optional") or {}).items():
        out.append((name, val, False))
    return out


def is_widget(val):
    if not isinstance(val, (list, tuple)) or not val:
        return False
    head = val[0]
    if isinstance(head, list):
        return True
    if isinstance(head, str) and head in SCALAR_TYPES:
        return True
    return False


def widget_default(val):
    if isinstance(val[0], list):
        return val[0][0] if val[0] else None
    opts = val[1] if len(val) > 1 and isinstance(val[1], dict) else {}
    if "default" in opts:
        d = opts["default"]
        if isinstance(d, (dict, list)):
            return json.dumps(d, ensure_ascii=False)
        return d
    if "options" in opts and isinstance(opts["options"], list) and opts["options"]:
        return opts["options"][0]
    if val[0] == "INT":
        return opts.get("min", 0)
    if val[0] == "FLOAT":
        return opts.get("min", 0.0)
    if val[0] == "BOOLEAN":
        return False
    if val[0] == "STRING":
        return ""
    return None


def seed_control(val):
    opts = val[1] if len(val) > 1 and isinstance(val[1], dict) else {}
    return bool(opts.get("control_after_generate"))


def combo_options(val):
    if isinstance(val[0], list):
        return val[0]
    opts = val[1] if len(val) > 1 and isinstance(val[1], dict) else {}
    return opts.get("options") or []


def output_names(spec):
    names = spec.get("output_name") or []
    types = spec.get("output") or []
    out = []
    for i, t in enumerate(types):
        out.append(names[i] if i < len(names) and names[i] else str(t))
    return out


# ---------------------------------------------------------------- build
def resolve_src(node, token):
    """token: output name, output type, or index. Returns (slot, type)."""
    outs = node["outputs"]
    if token.isdigit():
        i = int(token)
        if i >= len(outs):
            raise ValueError("%s has no output slot %s" % (node["type"], token))
        return i, outs[i]["type"]
    for i, o in enumerate(outs):
        if o["name"] == token or o.get("localized_name") == token:
            return i, o["type"]
    for i, o in enumerate(outs):
        if o["type"] == token:
            return i, o["type"]
    raise ValueError("%s has no output %r (outputs: %s)" % (node["type"], token,
                     ", ".join("%s:%s" % (o["name"], o["type"]) for o in outs)))



# ---------------------------------------------------------------- inspect
def subgraph_map(wf):
    subs = {}
    for s in ((wf.get("definitions") or {}).get("subgraphs") or []):
        if isinstance(s, dict) and s.get("id"):
            subs[s["id"]] = s
    legacy = ((wf.get("extra") or {}).get("subgraphs") or {}).get("subgraphs") or []
    for s in legacy:
        if isinstance(s, dict) and s.get("id"):
            subs.setdefault(s["id"], s)
    return subs


def expand_nodes(wf):
    subs = subgraph_map(wf)
    out = []

    def walk(nodes, depth):
        for n in nodes:
            if not isinstance(n, dict):
                continue
            t = n.get("type")
            if t in subs:
                walk(subs[t].get("nodes") or [], depth + 1)
            else:
                out.append((depth, t, n))

    walk(wf.get("nodes") or [], 0)
    return out, subs


def cmd_inspect(path):
    wf = jload(path)
    nodes, subs = expand_nodes(wf)
    print("file:", path)
    print("format: UI %s | top-level nodes: %d | subgraphs: %d | groups: %d" % (
        wf.get("version"), len(wf.get("nodes") or []), len(subs), len(wf.get("groups") or [])))
    for depth, t, n in nodes:
        if t in ("Reroute", "Note", "MarkdownNote", "PrimitiveNode"):
            continue
        w = n.get("widgets_values_named") or {}
        keep = {}
        if isinstance(w, dict):
            keep = {k: str(v)[:40] for k, v in w.items()
                    if k not in ("control_after_generate", "upload", "videopreview")}
        print("  " + "  " * depth + "- " + str(t) + (("  " + json.dumps(keep, ensure_ascii=False)) if keep else ""))


def build(recipe, catalog):
    nodes = recipe.get("nodes") or {}
    if not nodes:
        die("recipe has no nodes")
    alias_to_id = {}
    built = {}
    order_cursor = 0

    for alias, spec in nodes.items():
        ntype = spec.get("type")
        if not ntype:
            die("node %r has no type" % alias)
        if ntype not in catalog:
            die("node type %r not found in catalog (custom node missing?)" % ntype)
        cspec = catalog[ntype]
        nid = int(spec.get("id") or (order_cursor + 1))
        alias_to_id[alias] = nid
        widgets = dict(spec.get("widgets") or {})
        inputs, outputs, wv, wv_named = [], [], [], {}
        for name, val, required in input_entries(cspec):
            typ = val[0]
            if isinstance(typ, list):
                typ = "COMBO"
            if is_widget(val):
                v = widgets.pop(name, None)
                if v is None:
                    v = widget_default(val)
                wv.append(v)
                wv_named[name] = v
                if seed_control(val):
                    wv.append("randomize")
                    wv_named["control_after_generate"] = "randomize"
                inputs.append({"name": name, "type": typ, "widget": {"name": name}, "link": None})
            else:
                inputs.append({"name": name, "type": str(typ), "link": None})
        if widgets:
            die("node %r: unknown widget(s) %s for type %s" % (alias, ", ".join(widgets), ntype))
        names = output_names(cspec)
        for i, t in enumerate(cspec.get("output") or []):
            outputs.append({"name": names[i], "type": str(t), "slot_index": i, "links": []})
        built[alias] = {
            "id": nid,
            "type": ntype,
            "pos": [0, 0],
            "size": [320, 160],
            "flags": {},
            "order": 0,
            "mode": int(spec.get("mode", 0)),
            "inputs": inputs,
            "outputs": outputs,
            "properties": {"Node name for S&R": ntype, "cnr_id": "comfy-core"},
            "widgets_values": wv,
            "widgets_values_named": wv_named,
        }
        if spec.get("title"):
            built[alias]["title"] = spec["title"]
        elif recipe.get("annotate"):
            cat = (cspec.get("category") or "").split("/")[0]
            built[alias]["title"] = ("[%s] %s" % (cat, ntype)) if cat else ntype
        order_cursor += 1

    links = []
    for item in recipe.get("links") or []:
        if isinstance(item, dict):
            src, dst = item["from"], item["to"]
        else:
            if "->" not in item:
                die("bad link %r (expected 'a.b -> c.d')" % item)
            src, dst = [s.strip() for s in item.split("->", 1)]
        salias, stok = src.split(".", 1)
        dalias, dtok = dst.split(".", 1)
        if salias not in built or dalias not in built:
            die("link %r references unknown node" % item)
        snode, dnode = built[salias], built[dalias]
        slot, stype = resolve_src(snode, stok)
        target_idx = None
        for i, inp in enumerate(dnode["inputs"]):
            if inp["name"] == dtok:
                target_idx = i
                break
        if target_idx is None:
            die("link %r: %s has no input %r (inputs: %s)" % (
                item, dnode["type"], dtok, ", ".join(i["name"] for i in dnode["inputs"])))
        dinp = dnode["inputs"][target_idx]
        if dinp["type"] != stype and dinp["type"] != "*" and stype != "*":
            die("link %r type mismatch: %s -> %s" % (item, stype, dinp["type"]))
        lid = len(links) + 1
        links.append([lid, snode["id"], slot, dnode["id"], target_idx, dinp["type"]])
        dinp["link"] = lid
        snode["outputs"][slot]["links"].append(lid)

    # simple layered layout
    depths = {}

    def depth(alias, seen=None):
        seen = seen or set()
        if alias in depths:
            return depths[alias]
        if alias in seen:
            return 0
        seen.add(alias)
        d = 0
        for link in links:
            if link[3] == built[alias]["id"]:
                for a2, n2 in built.items():
                    if n2["id"] == link[1]:
                        d = max(d, depth(a2, seen) + 1)
        depths[alias] = d
        return d

    for alias in built:
        depth(alias)
    per_depth = {}
    for alias, node in built.items():
        d = depths[alias]
        row = per_depth.get(d, 0)
        node["pos"] = [d * 420, row * 260]
        per_depth[d] = row + 1
    for i, alias in enumerate(sorted(built, key=lambda a: depths[a])):
        built[alias]["order"] = i

    max_id = max(n["id"] for n in built.values())
    wf = {
        "id": str(uuid.uuid4()),
        "revision": 0,
        "last_node_id": max_id,
        "last_link_id": len(links),
        "nodes": [built[a] for a in sorted(built, key=lambda x: built[x]["id"])],
        "links": links,
        "groups": [],
        "config": {},
        "extra": {"ds": {"scale": 0.9, "offset": [0, 0]}, "frontendVersion": "1.58.5"},
        "version": 0.4,
    }
    return wf


# ---------------------------------------------------------------- validate
def validate(wf, catalog):
    errs, warns = [], []
    if wf.get("version") != 0.4:
        warns.append("version %r - expected 0.4" % wf.get("version"))
    nodes = {n["id"]: n for n in wf.get("nodes", [])}
    if not nodes:
        errs.append("workflow has no nodes")
    for n in nodes.values():
        t = n.get("type")
        if t not in catalog:
            errs.append("node #%s: type %r not in catalog" % (n.get("id"), t))
            continue
        spec = catalog[t]
        req = [k for k, v in (spec.get("input") or {}).get("required", {}).items()]
        names = {i["name"] for i in n.get("inputs", [])}
        for r in req:
            if r not in names:
                errs.append("node #%s (%s): missing required input %r in inputs[]" % (n.get("id"), t, r))
        wv = n.get("widgets_values_named") or {}
        for k, v in wv.items():
            if k in ("control_after_generate",):
                continue
        # combo membership
        cspec = {name: val for name, val, _r in input_entries(spec)}
        for k, v in wv.items():
            if k in cspec and isinstance(cspec[k], list) and cspec[k]:
                opts = combo_options(cspec[k])
                if opts and v not in opts:
                    errs.append("node #%s (%s): %s=%r not in options (%d choices)" % (
                        n.get("id"), t, k, v, len(opts)))
    seen_links = set()
    for link in wf.get("links", []):
        if len(link) != 6:
            errs.append("malformed link %r" % (link,))
            continue
        lid, sid, sslot, tid, tslot, ltype = link
        if lid in seen_links:
            errs.append("duplicate link id %s" % lid)
        seen_links.add(lid)
        if sid not in nodes or tid not in nodes:
            errs.append("link %s references missing node (%s->%s)" % (lid, sid, tid))
            continue
        src, dst = nodes[sid], nodes[tid]
        if sslot >= len(src.get("outputs", [])):
            errs.append("link %s: source slot %s out of range" % (lid, sslot))
        elif sslot >= len(src.get("outputs", [])) or tslot >= len(dst.get("inputs", [])):
            pass
        if tslot >= len(dst.get("inputs", [])):
            errs.append("link %s: target slot %s out of range" % (lid, tslot))
            continue
        dinp = dst["inputs"][tslot]
        if dinp.get("link") != lid:
            errs.append("link %s: target input %r has link=%r" % (lid, dinp.get("name"), dinp.get("link")))
        if sslot < len(src.get("outputs", [])):
            sout = src["outputs"][sslot]
            if ltype not in (dinp.get("type"), "*") and dinp.get("type") not in (ltype, "*"):
                errs.append("link %s type %s != input type %s" % (lid, ltype, dinp.get("type")))
            if lid not in (sout.get("links") or []):
                errs.append("link %s missing from source #%s outputs[%s].links" % (lid, sid, sslot))
    # every required non-widget input must have a link
    for n in nodes.values():
        spec = catalog.get(n.get("type")) or {}
        req = set((spec.get("input") or {}).get("required", {}).keys())
        for i in n.get("inputs", []):
            if "widget" not in i and i.get("link") is None and i.get("name") in req:
                errs.append("node #%s (%s): required input %r is not connected" % (n.get("id"), n.get("type"), i.get("name")))
    outs = [n for n in nodes.values() if n["type"] in OUT_NODE_TYPES]
    if not outs:
        warns.append("no obvious output node (SaveImage/PreviewImage/...) - ComfyUI will execute but show nothing")
    return errs, warns


# ---------------------------------------------------------------- UI -> API
def ui_to_api(wf, catalog):
    nodes = {n["id"]: n for n in wf.get("nodes", [])}
    prompt = {}
    for nid, n in nodes.items():
        if n.get("mode") in (2, 4):
            continue
        t = n.get("type")
        spec = catalog.get(t)
        if spec is None:
            raise ValueError("node #%s type %r not in catalog" % (nid, t))
        scalars = {name for name, val, _r in input_entries(spec) if is_widget(val)}
        inputs = {}
        for i in n.get("inputs", []):
            link = i.get("link")
            if link is not None:
                inputs[i["name"]] = None  # filled below
        for link in wf.get("links", []):
            lid, sid, sslot, tid, tslot, _t = link
            if tid != nid:
                continue
            dst_input = n["inputs"][tslot]["name"]
            inputs[dst_input] = [str(sid), sslot]
        wv = n.get("widgets_values_named") or {}
        for k, v in wv.items():
            if k in scalars:
                inputs[k] = v
        prompt[str(nid)] = {"class_type": t, "inputs": inputs,
                            "_meta": {"title": n.get("title") or t}}
    return {"prompt": prompt, "client_id": str(uuid.uuid4())}


# ---------------------------------------------------------------- run
def submit_api(prompt_obj, wait=False, download=None, timeout=900):
    status, resp = http("POST", "/prompt", prompt_obj, timeout=60)
    if status != 200:
        print("submit failed (HTTP %s)" % status)
        print(json.dumps(resp, ensure_ascii=False, indent=1)[:4000])
        return 1
    pid = resp.get("prompt_id")
    print("queued prompt", pid, "| queue_no", resp.get("number"))
    if not wait:
        return 0
    t0 = time.time()
    while time.time() - t0 < timeout:
        st, hist = http("GET", "/history/%s" % pid, timeout=30)
        if st == 200 and hist.get(pid):
            entry = hist[pid]
            outs = entry.get("outputs") or {}
            print("done in %.1fs | status=%s" % (time.time() - t0, entry.get("status", {}).get("status_str")))
            files = []
            for node_id, out in outs.items():
                for key in ("images", "gifs", "videos", "audio", "files"):
                    for f in out.get(key) or []:
                        files.append(f)
                        print("  output:", f.get("filename"), "(%s/%s)" % (f.get("type"), f.get("subfolder")))
            if download and files:
                os.makedirs(download, exist_ok=True)
                for f in files:
                    q = urllib.parse.urlencode({"filename": f.get("filename", ""),
                                                "subfolder": f.get("subfolder", ""),
                                                "type": f.get("type", "output")})
                    url = base_url().rstrip("/") + "/view?" + q
                    dest = os.path.join(download, f.get("filename") or "output.bin")
                    with urllib.request.urlopen(url, timeout=120) as r, open(dest, "wb") as fh:
                        fh.write(r.read())
                    print("  saved:", dest)
            return 0
        st2, q = http("GET", "/queue", timeout=30)
        time.sleep(2)
    print("timeout waiting for prompt", pid)
    return 2


# ---------------------------------------------------------------- tunnel
def run_tunnel(local_port, remote_port):
    import paramiko
    inst = require_instance()
    host, port, user, password = inst["host"], inst["port"], inst["user"], inst["password"]

    state = {"client": None, "transport": None}

    def ensure_transport():
        while True:
            t = state["transport"]
            if t is not None and t.is_active():
                return t
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=port, username=user, password=password, timeout=30,
                               banner_timeout=60, auth_timeout=60, look_for_keys=False, allow_agent=False)
                t = client.get_transport()
                t.set_keepalive(20)
                state["client"] = client
                state["transport"] = t
                print("ssh transport up (keepalive 20s)")
                return t
            except Exception as exc:
                print("ssh reconnect failed: %s" % exc)
                state["transport"] = None
                time.sleep(3)

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(("127.0.0.1", local_port))
    srv.listen(50)
    ensure_transport()
    print("tunnel ready: 127.0.0.1:%d -> %s:%d (remote 127.0.0.1:%d)" % (local_port, host, port, remote_port))

    def pipe(src, dst):
        try:
            while True:
                data = src.recv(65536)
                if not data:
                    break
                dst.sendall(data)
        except Exception:
            pass
        finally:
            for s in (src, dst):
                try:
                    s.close()
                except Exception:
                    pass

    while True:
        conn, _addr = srv.accept()
        chan = None
        for attempt in range(2):
            try:
                chan = ensure_transport().open_channel(
                    "direct-tcpip", ("127.0.0.1", remote_port), conn.getpeername())
                break
            except Exception as exc:
                print("open_channel failed (%s), reconnecting" % exc)
                state["transport"] = None
        if chan is None:
            try:
                conn.close()
            except Exception:
                pass
            continue
        threading.Thread(target=pipe, args=(conn, chan), daemon=True).start()
        threading.Thread(target=pipe, args=(chan, conn), daemon=True).start()


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description="ComfyUI workflow toolkit")
    sub = ap.add_subparsers(dest="cmd", required=True)

    t = sub.add_parser("tunnel")
    t.add_argument("--local-port", type=int, default=None)
    t.add_argument("--remote-port", type=int, default=None)

    sub.add_parser("stats")
    sub.add_parser("catalog")
    sub.add_parser("queue")
    sub.add_parser("interrupt")

    n = sub.add_parser("nodes")
    n.add_argument("keyword")

    b = sub.add_parser("build")
    b.add_argument("recipe")
    b.add_argument("-o", "--out")

    i = sub.add_parser("inspect")
    i.add_argument("workflow")

    v = sub.add_parser("validate")
    v.add_argument("workflow")

    c = sub.add_parser("convert")
    c.add_argument("workflow")
    c.add_argument("-o", "--out")

    s = sub.add_parser("submit")
    s.add_argument("workflow", help="UI workflow json, or '-' for stdin")
    s.add_argument("--wait", action="store_true")
    s.add_argument("--download", default=None)
    s.add_argument("--timeout", type=int, default=1800)
    s.add_argument("--seed", type=int, default=None, help="override every seed/noise_seed in the prompt")

    args = ap.parse_args()

    if args.cmd == "tunnel":
        inst = require_instance()
        run_tunnel(args.local_port or inst["local_port"], args.remote_port or inst["remote_port"])
        return
    if args.cmd == "stats":
        st, data = http("GET", "/system_stats", timeout=20)
        if st != 200:
            die("HTTP %s - is the tunnel up?" % st)
        sysinfo = data.get("system", {})
        print("ComfyUI", sysinfo.get("comfyui_version"), "| frontend", sysinfo.get("required_frontend_version"))
        for d in data.get("devices", []):
            print("GPU:", d.get("name"), "| VRAM %.1f GB" % (d.get("vram_total", 0) / 1e9))
        return
    if args.cmd == "catalog":
        status, data = http("GET", "/object_info", timeout=180)
        if status != 200 or not data:
            die("cannot fetch /object_info (HTTP %s)" % status)
        os.makedirs(CACHE, exist_ok=True)
        jsave(data, catalog_path())
        print("catalog saved:", catalog_path(), "| nodes:", len(data))
        return
    if args.cmd == "queue":
        st, q = http("GET", "/queue", timeout=20)
        running = q.get("queue_running") or []
        pending = q.get("queue_pending") or []
        print("running:", len(running), "| pending:", len(pending))
        for item in running + pending:
            print("  prompt", item[1], "| nodes", len(item[2]) if len(item) > 2 else "?")
        return
    if args.cmd == "interrupt":
        st, r = http("POST", "/interrupt", {})
        print("interrupt ->", st, r)
        return
    if args.cmd == "nodes":
        cat = load_catalog()
        kw = args.keyword.lower()
        hits = [k for k in cat if kw in k.lower()]
        print("%d match(es)" % len(hits))
        for k in hits[:80]:
            spec = cat[k]
            ins = ", ".join("%s:%s" % (name, (val[0] if not isinstance(val[0], list) else "COMBO"))
                            for name, val, _r in input_entries(spec))
            outs = ", ".join(output_names(spec))
            print("- %s  [%s]\n    in: %s\n    out: %s" % (k, spec.get("category", ""), ins, outs))
        return

    if args.cmd == "inspect":
        cmd_inspect(args.workflow)
        return 0

    cat = load_catalog()

    if args.cmd == "build":
        recipe = jload(args.recipe)
        wf = build(recipe, cat)
        errs, warns = validate(wf, cat)
        out = args.out or (os.path.splitext(args.recipe)[0] + ".workflow.json")
        jsave(wf, out)
        print("built:", out, "| nodes:", len(wf["nodes"]), "| links:", len(wf["links"]))
        for e in errs:
            print("  ERROR", e)
        for w in warns:
            print("  WARN ", w)
        return 1 if errs else 0
    if args.cmd == "validate":
        wf = jload(args.workflow)
        errs, warns = validate(wf, cat)
        print("validate:", args.workflow)
        for e in errs:
            print("  ERROR", e)
        for w in warns:
            print("  WARN ", w)
        print("OK" if not errs else "%d error(s)" % len(errs))
        return 1 if errs else 0
    if args.cmd == "convert":
        wf = jload(args.workflow)
        errs, warns = validate(wf, cat)
        if errs:
            print("refusing to convert: %d error(s)" % len(errs))
            return 1
        prompt = ui_to_api(wf, cat)
        out = args.out or (os.path.splitext(args.workflow)[0] + ".api.json")
        jsave(prompt, out)
        print("api prompt:", out, "| nodes:", len(prompt["prompt"]))
        return 0
    if args.cmd == "submit":
        if args.workflow == "-":
            wf = json.load(sys.stdin)
        else:
            wf = jload(args.workflow)
        errs, warns = validate(wf, cat)
        if errs:
            print("refusing to submit: %d error(s)" % len(errs))
            for e in errs[:20]:
                print("  ERROR", e)
            return 1
        prompt = ui_to_api(wf, cat)
        if args.seed is not None:
            for node in prompt["prompt"].values():
                for key in ("seed", "noise_seed"):
                    if key in node["inputs"]:
                        node["inputs"][key] = args.seed
        return submit_api(prompt, wait=args.wait, download=args.download, timeout=args.timeout)
    die("unknown command")


if __name__ == "__main__":
    sys.exit(main())
