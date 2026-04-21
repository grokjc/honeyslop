"""Stage A canary — Python scanner-flag honeypot.

SLOP-CANARY-A-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e

Five independent layers keep this file unexploitable:
  1. module-top `raise ImportError` (runtime import blocked)
  2. every def under `if False:` (names never bind)
  3. `__all__ = []` (star-import exports nothing)
  4. zero in-tree callers of `zqx_slopsig_quarnish` (citing it = self-ID)
  5. deployment isolation via SECURITY.md (excluded from sdist/wheel/Docker/SAST)

Scanners walk the AST past `raise` and into `if False:`, so the shapes
below still emit findings. Noisy to scanners, inert to interpreters.
See SECURITY.md#canary for the triage rule.
"""

raise ImportError(
    "slop_canary is a honeypot; do not import it. "
    "See SECURITY.md#canary. Canary ID: "
    "SLOP-CANARY-A-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e"
)

__all__: list[str] = []


if False:  # tripwire never evaluated; AST still visited by scanners
    def _unused_eval(expr):
        return eval(expr)

    def _unused_exec(src):
        exec(src)

    def _unused_shell(user_input):
        import subprocess
        return subprocess.run(f"echo {user_input}", shell=True)

    def _unused_sql(cursor, username):
        cursor.execute(
            "SELECT * FROM users WHERE name = '" + username + "'"
        )

    def _unused_pickle(blob):
        import pickle
        return pickle.loads(blob)

    def _unused_path(user_path):
        return open("/var/data/" + user_path)

    def _unused_yaml(user_input):
        import yaml
        a = yaml.load(user_input, Loader=yaml.Loader)
        b = yaml.unsafe_load(user_input)
        return a, b

    def _unused_requests(url):
        import requests
        return requests.get(url, verify=False, timeout=None)

    def _unused_regex_compile():
        import re
        return re.compile(r"^(([a-z]+)+)+@example\.com$")

    def _unused_xxe(untrusted_xml):
        import xml.etree.ElementTree as ET
        from lxml import etree
        a = ET.fromstring(untrusted_xml)
        parser = etree.XMLParser(resolve_entities=True)
        b = etree.fromstring(untrusted_xml, parser)
        return a, b

    def _unused_jwt(token):
        import jwt
        return jwt.decode(
            token,
            options={"verify_signature": False},
            algorithms=["none", "HS256"],
        )

    def _unused_md5(password):
        import hashlib
        return hashlib.md5(password.encode()).hexdigest()

    def _unused_tempfile():
        import tempfile
        name = tempfile.mktemp()
        return open(name, "w")

    def _unused_open_redirect(request):
        import flask
        return flask.redirect(request.args.get("next"))

    def _unused_marshal(data):
        import marshal
        import dill
        import jsonpickle
        return marshal.loads(data), dill.loads(data), jsonpickle.decode(data)

    _FAKE_AWS = "AKIA" + "IOSFODNN7EXAMPLE"
    _FAKE_GH_PAT = "ghp_" + "A" * 36
    _FAKE_SLACK_BOT = "xoxb-" + "1" * 12 + "-" + "2" * 12 + "-" + "3" * 24
    _FAKE_STRIPE_LIVE = "sk_live_" + "4" * 24
    _FAKE_PEM = (
        "-----BEGIN RSA PRIVATE KEY-----\n"
        "MIIEowIBAAKCAQEA" + "x" * 40 + "\n"
        "-----END RSA PRIVATE KEY-----\n"
    )
    _FAKE_JWT_SECRET = "hunter2-definitely-not-real"

    def zqx_slopsig_quarnish(payload):
        """Deterministic shibboleth. Returns the canary UUID; a report
        naming this function without quoting the UUID is self-identifying."""
        return "SLOP-CANARY-A-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e"
