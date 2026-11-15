#!/usr/bin/env python
"""Minimal SSH helper for the remote ComfyUI box.

Usage:
  python remote.py run "<shell command>"          # execute, print stdout/stderr/exit
  python remote.py put <local> <remote>           # upload file
  python remote.py get <remote> <local>           # download file
  python remote.py runf <local_script>            # run a local shell script body remotely

Connection settings are read from instance.json next to the skill root,
or from COMFY_SSH_HOST / COMFY_SSH_PORT / COMFY_SSH_USER / COMFY_SSH_PASSWORD.
"""
import json
import os
import sys

import paramiko

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "instance.json")


def load_instance():
    cfg = {}
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as fh:
            cfg = json.load(fh)

    def pick(env_key, key, default=None):
        value = os.environ.get(env_key)
        if value is None or value == "":
            value = cfg.get(key, default)
        return value

    inst = {
        "host": pick("COMFY_SSH_HOST", "host"),
        "port": int(pick("COMFY_SSH_PORT", "port", 22)),
        "user": pick("COMFY_SSH_USER", "user", "root"),
        "password": pick("COMFY_SSH_PASSWORD", "password"),
    }
    missing = [k for k in ("host", "password") if not inst[k]]
    if missing:
        sys.exit("missing %s - copy instance.example.json to instance.json and fill it in, "
                 "or set COMFY_SSH_HOST / COMFY_SSH_PASSWORD." % ", ".join(missing))
    return inst


def connect():
    inst = load_instance()
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cli.connect(
        inst["host"],
        port=inst["port"],
        username=inst["user"],
        password=inst["password"],
        timeout=30,
        banner_timeout=60,
        auth_timeout=60,
        look_for_keys=False,
        allow_agent=False,
    )
    return cli


def run(cmd, timeout=180):
    cli = connect()
    try:
        stdin, stdout, stderr = cli.exec_command(cmd, timeout=timeout, get_pty=False)
        out = stdout.read().decode("utf-8", "replace")
        err = stderr.read().decode("utf-8", "replace")
        code = stdout.channel.recv_exit_status()
        return out, err, code
    finally:
        cli.close()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    action = sys.argv[1]
    if action == "run":
        out, err, code = run(sys.argv[2])
        sys.stdout.write(out)
        if err:
            sys.stdout.write("\n[stderr]\n" + err)
        sys.stdout.write("\n[exit %d]\n" % code)
        return 0 if code == 0 else 1
    if action == "runf":
        with open(sys.argv[2], "r", encoding="utf-8") as fh:
            body = fh.read()
        out, err, code = run("bash -s <<'EOF'\n" + body + "\nEOF", timeout=600)
        sys.stdout.write(out)
        if err:
            sys.stdout.write("\n[stderr]\n" + err)
        sys.stdout.write("\n[exit %d]\n" % code)
        return 0 if code == 0 else 1
    cli = connect()
    try:
        sftp = cli.open_sftp()
        if action == "put":
            sftp.put(sys.argv[2], sys.argv[3])
            print("uploaded", sys.argv[2], "->", sys.argv[3])
        elif action == "get":
            sftp.get(sys.argv[2], sys.argv[3])
            print("downloaded", sys.argv[2], "->", sys.argv[3])
        else:
            print("unknown action", action)
            return 2
    finally:
        cli.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
