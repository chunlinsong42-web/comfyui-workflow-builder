#!/usr/bin/env python
"""Repository self-check: templates parse, SKILL frontmatter, docs links, no secrets.

Runs with the standard library only (no ComfyUI needed).
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
warnings = []


def check_templates():
    tdir = os.path.join(ROOT, "templates")
    names = sorted(n for n in os.listdir(tdir) if n.endswith(".json"))
    if not names:
        errors.append("templates/: no recipes found")
    for n in names:
        path = os.path.join(tdir, n)
        try:
            d = json.load(open(path, encoding="utf-8"))
        except Exception as exc:
            errors.append("templates/%s: invalid JSON (%s)" % (n, exc))
            continue
        if not isinstance(d.get("nodes"), dict) or not d["nodes"]:
            errors.append("templates/%s: missing non-empty 'nodes'" % n)
            continue
        if not isinstance(d.get("links"), list):
            errors.append("templates/%s: missing 'links' list" % n)
            continue
        aliases = set(d["nodes"].keys())
        for link in d["links"]:
            if "->" not in str(link):
                errors.append("templates/%s: bad link %r" % (n, link))
                continue
            src, dst = [x.strip() for x in str(link).split("->", 1)]
            for side in (src, dst):
                alias = side.split(".")[0]
                if alias not in aliases:
                    errors.append("templates/%s: link %r references unknown alias %r" % (n, link, alias))
    print("templates checked:", len(names))


def check_skill():
    path = os.path.join(ROOT, "SKILL.md")
    text = open(path, encoding="utf-8").read()
    if not text.startswith("---"):
        errors.append("SKILL.md: missing YAML frontmatter")
        return
    fm = text.split("---", 2)[1]
    if "name:" not in fm:
        errors.append("SKILL.md: frontmatter missing 'name'")
    if "description:" not in fm:
        errors.append("SKILL.md: frontmatter missing 'description'")
    print("SKILL.md frontmatter ok")


def check_docs():
    must = ["README.md", "LICENSE", "CHANGELOG.md", "instance.example.json",
            "references/instance.md", "references/workflow-format.md"]
    for rel in must:
        if not os.path.exists(os.path.join(ROOT, rel)):
            errors.append("missing file: " + rel)
    # relative markdown links that point at repo paths must exist
    link_re = re.compile(r"\]\(([^)#]+?)(?:#[^)]*)?\)")
    for rel in ("README.md", "SKILL.md"):
        text = open(os.path.join(ROOT, rel), encoding="utf-8").read()
        for target in link_re.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not os.path.exists(os.path.join(ROOT, target)):
                warnings.append("%s: link target missing: %s" % (rel, target))
    print("docs checked")


def check_secrets():
    bad = re.compile(r"(github_pat_[A-Za-z0-9_]{10,}|ghp_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)")
    for root, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in (".git", ".cache", "__pycache__", "node_modules")]
        for fn in files:
            if not fn.endswith((".md", ".py", ".json", ".yml", ".yaml", ".txt", ".svg")):
                continue
            path = os.path.join(root, fn)
            try:
                text = open(path, encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            if bad.search(text):
                errors.append("possible secret in " + os.path.relpath(path, ROOT))
    print("secret scan done")


if __name__ == "__main__":
    check_templates()
    check_skill()
    check_docs()
    check_secrets()
    for w in warnings:
        print("WARN", w)
    for e in errors:
        print("ERROR", e)
    print("OK" if not errors else "%d error(s)" % len(errors))
    sys.exit(1 if errors else 0)
