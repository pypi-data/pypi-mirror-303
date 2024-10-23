# Django-JWT

This is a package to verify and validate JSON Web Tokens (JWT) in Django.

### Installation
1. Install the package using pip:
```bash
    pip install dj-jwt-auth
```

2. Add "django_jwt" to your INSTALLED_APPS setting like this::
```
    INSTALLED_APPS = [
        ...
        "django_jwt",
    ]
```

3. Add "django_jwt.middleware.JWTAuthMiddleware" to your MIDDLEWARE setting like this::
```
    MIDDLEWARE = [
        ...
        "django_jwt.middleware.JWTAuthMiddleware",
    ]
```

### Configuration:
Required variables:
- OIDC_CONFIG_ROUTES - dict of "algorithm": "config_url". Required for using JWTAuthMiddleware. Example: 
```
   OIDC_CONFIG_ROUTES = {
       "RS256": "https://keyCloak/realms/h/.well-known/openid-configuration",
       "HS256": "https://keyCloak/realms/h/.well-known/openid-configuration",
   } 
```
Optional variables:
- OIDC_AUDIENCE - by default ["account", "broker"]

User retated variables:
- OIDC_USER_UPDATE - if True, user model will be updated from userinfo endpoint if MODIFIED date has changed, by default True
- OIDC_USER_MODIFIED_FIELD - user model field to store last modified date, by default `modified_timestamp`
- OIDC_TOKEN_MODIFIED_FIELD - access token field to store last modified date, by default `updated_at`
- OIDC_USER_UID - User model" unique identifier, by default `kc_id`
- OIDC_TOKEN_USER_UID - access token field to store user UID, by default `sub`
- OIDC_USER_MAPPING - mapping between JWT claims and user model fields. Can be dict or function. By default:
```
    OIDC_USER_MAPPING = {
        "given_name": "first_name",
        "family_name": "last_name",
        "name": "username",
    }
```
OR
```
    def OIDC_USER_MAPPING(userinfo):
        return {
            "first_name": userinfo.get("given_name"),
            "last_name": userinfo.get("family_name"),
            "username": userinfo.get("name"),
        }
- OIDC_USER_DEFAULTS - default values for user model fields, by default:
```
    OIDC_USER_DEFAULTS = {
        "is_active": True,
    }
```

- OIDC_USER_ON_CREATE and OIDC_USER_ON_UPDATE - functions to be called on user creation and update, by default:
```
    OIDC_USER_ON_CREATE = None
    OIDC_USER_ON_UPDATE = None
```
These functions should accept two arguments: user and request.

### Admin panel integration:
To integrate admin panel with OIDC, add OIDC_ADMIN_ISSUER and OIDC_ADMIN_CLIENT_ID to settings.
- OIDC_ADMIN_ISSUER - for admin-panel access through OIDC. By default will be used 'ES256' from OIDC_CONFIG_ROUTES. Example: 
```
    OIDC_ADMIN_ISSUER = "https://keyCloak/realms/h/.well-known/openid-configuration"
```
- OIDC_ADMIN_CLIENT_ID - by default "complete-anatomy"
To mapping roles to admin panel permissions, use OIDC_ADMIN_ROLES. Example:

```python

from django_jwt.roles import ROLE

OIDC_ADMIN_ROLES = [
    ROLE(
        name="admin",  # name from token
        is_superuser=True,
    ),
    ROLE(
        name="staff",
        groups=["LMS (Full)", "Organizations (Full)", "Customer Support (Full)"],
        permissions=["Can add user"],
    ),
]
```
And add login view to urls.py:
```python
urlpatterns = [
    path("admin/", include("django_jwt.urls")),
    ...
]
```
Login URL will be available at `/admin/oidc/`.

### Testing:
Run command `python runtests.py` to run tests.