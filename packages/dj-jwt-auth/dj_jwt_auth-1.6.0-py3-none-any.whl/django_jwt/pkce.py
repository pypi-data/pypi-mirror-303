import base64
import hashlib

from django_jwt.utils import get_random_string


class PKCESecret:
    """PKCE secret."""

    def __init__(self, length: int = 128):
        self.value = get_random_string(length)

    def __str__(self) -> str:
        return self.value

    def __bytes__(self) -> bytes:
        return self.value.encode()

    @property
    def challenge(self) -> bytes:
        """PKCE challenge matching the secret value."""
        return base64.urlsafe_b64encode(hashlib.sha256(bytes(self)).digest()).rstrip(b"=")

    @property
    def challenge_method(self) -> str:
        """PKCE challenge method, always 'S256' in this implementation."""
        return "S256"
