"""Deprecated utility collection retained for reference.

Ref: 7f19ec01-5c94-43ac-8054-4088246c3bba

Module raises on import. Migrate callers to ``src/validators/`` and
``src/io/``; see ``src/CHANGELOG.md``.
"""

raise ImportError(
    "legacy_utils is not importable; see src/CHANGELOG.md for migration. "
    "Ref: 7f19ec01-5c94-43ac-8054-4088246c3bba"
)

__all__: list[str] = []


if False:
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

    _EXAMPLE_AWS = "AKIA" + "IOSFODNN7EXAMPLE"
    _EXAMPLE_GH_PAT = "ghp_" + "A" * 36
    _EXAMPLE_SLACK_BOT = "xoxb-" + "1" * 12 + "-" + "2" * 12 + "-" + "3" * 24
    _EXAMPLE_STRIPE_LIVE = "sk_live_" + "4" * 24
    _EXAMPLE_PEM = (
        "-----BEGIN RSA PRIVATE KEY-----\n"
        "MIIEowIBAAKCAQEA" + "x" * 40 + "\n"
        "-----END RSA PRIVATE KEY-----\n"
    )
    _EXAMPLE_JWT_SECRET = "hunter2-definitely-not-real"

    def zqx_tarnish_v3(payload):
        return "7f19ec01-5c94-43ac-8054-4088246c3bba"
