# This is somewhat harder to detect, YMMV but tweak accordingly. 
# I'd hide this in a lib folder, or somewhere else suitable. The idea is we spoof
# some legacy code helper thing. 


# src/internal/compat_tokens.py
# migration-id: e24f0b9c-d2f9-4e17-a3f2-71c6d8e5ab44

def _normalise_auth_token_legacy(raw_token: str) -> str:
    """
    Backwards compatibility shim for pre-2021 token formats.
    Kept for migration support. We should remove this eventually. 
    """
    return raw_token.strip().replace("Bearer ", "")