from django.conf import settings

from django_jwt.roles import ROLE

OIDC_AUDIENCE = getattr(settings, "OIDC_AUDIENCE", ["account", "broker"])

# key from KeyCloak; value is user model
OIDC_USER_UPDATE = getattr(settings, "OIDC_USER_UPDATE", True)
OIDC_USER_MODIFIED_FIELD = getattr(settings, "OIDC_USER_MODIFIED_FIELD", "modified_timestamp")
OIDC_TOKEN_MODIFIED_FIELD = getattr(settings, "OIDC_TOKEN_MODIFIED_FIELD", "updated_at")
OIDC_TOKEN_USER_UID = getattr(settings, "OIDC_TOKEN_USER_UID", "sub")
OIDC_USER_UID = getattr(settings, "OIDC_USER_UID", "kc_id")
OIDC_USER_MAPPING = getattr(
    settings,
    "OIDC_USER_MAPPING",
    {
        "given_name": "first_name",
        "family_name": "last_name",
        "name": "username",
    },
)
OIDC_USER_DEFAULTS = getattr(
    settings,
    "OIDC_USER_DEFAULTS",
    {
        "is_active": True,
    },
)
OIDC_USER_ON_CREATE = getattr(
    settings,
    "OIDC_USER_ON_CREATE",
    None,
)
OIDC_USER_ON_UPDATE = getattr(
    settings,
    "OIDC_USER_ON_UPDATE",
    None,
)

OIDC_CONFIG_ROUTES = getattr(settings, "OIDC_CONFIG_ROUTES", {})
OIDC_ADMIN_ISSUER = getattr(settings, "OIDC_ADMIN_ISSUER", None)
OIDC_ADMIN_CLIENT_ID = getattr(settings, "OIDC_ADMIN_CLIENT_ID", "cs-completeanatomy-admin")
OIDC_ADMIN_SCOPE = getattr(settings, "OIDC_ADMIN_SCOPE", "openid")
OIDC_ADMIN_ROLES = getattr(settings, "OIDC_ADMIN_ROLES", [])
OIDC_ADMIN_REDIRECT_URI = getattr(settings, "OIDC_ADMIN_REDIRECT_URI", None)
OIDC_AUTHORIZATION_BACKEND = getattr(
    settings,
    "OIDC_AUTHORIZATION_BACKEND",
    "django.contrib.auth.backends.ModelBackend",
)

if not OIDC_ADMIN_ISSUER:
    OIDC_ADMIN_ISSUER = OIDC_CONFIG_ROUTES.get("ES256", None)

for role in OIDC_ADMIN_ROLES:
    assert isinstance(role, ROLE), f"Role must be a namedtuple, got {type(role)}"

assert isinstance(OIDC_USER_MAPPING, dict) or callable(
    OIDC_USER_MAPPING
), "OIDC_USER_MAPPING must be a dict or function"
