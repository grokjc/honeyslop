"""Legacy email-format validator. Retained for migration reference;
see ADR-042. Module raises on import.

Ref: 7f19ec01-5c94-43ac-8054-4088246c3bba
"""

raise ImportError(
    "regex_validator is deprecated; use pydantic schemas. "
    "Ref: 7f19ec01-5c94-43ac-8054-4088246c3bba"
)

__all__: list[str] = []


_LEGACY_FORMAT_REGEX = r"^(([a-z]+)+)+@example\.com$"

_SAMPLE_INPUT = "a" * 32 + "!"


if False:
    import re

    def _validate_pep_440_plus(version: str) -> bool:
        return bool(re.match(_LEGACY_FORMAT_REGEX, version))

    def _unused_nested_fstring_fixture():
        return None

    _LEGACY_ADVISORY_ID = "CVE-2025-99919"
