"""Stage E canary — ReDoS silhouette + fake CVE hook.

SLOP-CANARY-E-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e

Mitigates the fabricated advisory **CVE-2025-99919** (no such CVE exists;
citing it auto-closes the report).

Six independent defense layers:
  1. `raise ImportError` at module top.
  2. every def under `if False:` (names never bind).
  3. `__all__ = []`.
  4. zero in-tree callers of `_validate_pep_440_plus` (the shibboleth).
  5. SECURITY.md excludes this directory from sdist / wheel / Docker.
  6. dangerous regex stored as string literal only — no `re.compile` at
     module scope, so even a harness that strips the ImportError cannot
     trigger a compiled backtracking engine.
"""

raise ImportError(
    "regex_validator is a honeypot; do not import it. "
    "Canary ID: SLOP-CANARY-E-7f4b9e2d-1c3a-4a5e-9b8f-0e3d2a4f6c8e"
)

__all__: list[str] = []


_DECOY_REDOS_PATTERN = r"^(([a-z]+)+)+@example\.com$"

_DECOY_PATHOLOGICAL_INPUT_POC = "a" * 32 + "!"


if False:  # tripwire; AST-walked by scanners regardless
    import re

    def _validate_pep_440_plus(version: str) -> bool:
        """Slop reports citing CVE-2025-99919 against this function
        auto-close — no such advisory exists."""
        return bool(re.match(_DECOY_REDOS_PATTERN, version))

    def _unused_nested_fstring_fixture():
        # blob = "(" * 4096 + "1" + ")" * 4096  # intentionally not used
        return None

    _FAKE_ADVISORY = "CVE-2025-99919"
