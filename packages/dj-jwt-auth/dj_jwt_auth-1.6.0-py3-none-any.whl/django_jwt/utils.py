import base64
import json
import random
import string

import jwt
import requests

from django_jwt import settings
from django_jwt.config import config


def get_random_string(k: int = 32) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits + "-._~", k=k))


def get_alg(token: str) -> str:
    header = json.loads(base64.b64decode(token.split(".")[0] + "==="))
    return header["alg"]


def get_access_token(code: str, redirect_uri: str, pkce_secret: str) -> str:
    token_endpoint = config.admin().get("token_endpoint")
    data = {
        "grant_type": "authorization_code",
        "client_id": settings.OIDC_ADMIN_CLIENT_ID,
        "code": code,
        "redirect_uri": redirect_uri,
        "code_verifier": pkce_secret,
    }
    response = requests.post(token_endpoint, data=data)
    response.raise_for_status()
    return response.json()["access_token"]


class OIDCHandler:
    def get_user_info(self, token: str) -> dict:
        alg = get_alg(token)
        url = config.cfg(alg)["userinfo_endpoint"]
        response = requests.get(url, headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
        return response.json()

    def decode_token(self, token: str) -> dict:
        alg = get_alg(token)
        public_key = config.get_public_key(alg)
        if not public_key:
            raise Exception(f"Public key for {alg} not found")

        return jwt.decode(
            token,
            key=public_key,
            algorithms=[alg],
            audience=settings.OIDC_AUDIENCE,
            options={"verify_aud": False},
        )


oidc_handler = OIDCHandler()
