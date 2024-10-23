import base64
from logging import getLogger
from urllib.parse import urlencode

from django.contrib.auth import login
from django.core.cache import cache
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from requests.exceptions import HTTPError

from django_jwt import settings as jwt_settings
from django_jwt.config import config
from django_jwt.exceptions import BadRequestException, ConfigException
from django_jwt.pkce import PKCESecret
from django_jwt.user import UserHandler, role_handler
from django_jwt.utils import get_access_token, get_random_string, oidc_handler

log = getLogger(__name__)


def silent_sso_check(request):
    return HttpResponse("<html><body><script>parent.postMessage(location.href, location.origin)</script></body></html>")


def index_response(request, msg, status=400):
    logout_url = config.admin().get("end_session_endpoint")
    return render(
        request,
        "django-jwt-index.html",
        {
            "error_message": msg,
            "login_url": reverse("start_oidc_auth"),
            "logout_url": logout_url,
            "redirect_uri": request.build_absolute_uri(reverse("start_oidc_auth")),
        },
        status=status,
    )


class AbsView(View):
    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except HTTPError as exc:
            log.warning(f"OIDC Admin HTTPError: {exc}")
            return index_response(request=request, msg=exc.response.text, status=exc.response.status_code)
        except ConfigException as exc:
            return HttpResponse(content=str(exc), status=500)
        except BadRequestException as exc:
            return index_response(request=request, msg=str(exc))
        except Exception as exc:
            return index_response(request=request, msg=str(exc))


class StartOIDCAuthView(AbsView):
    def get(self, request):
        pkce_secret = PKCESecret()
        redirect_uri = jwt_settings.OIDC_ADMIN_REDIRECT_URI
        if not redirect_uri:
            redirect_uri = request.build_absolute_uri(reverse("receive_redirect_view"))
        authorization_endpoint = config.admin().get("authorization_endpoint")
        state = base64.urlsafe_b64encode(get_random_string().encode()).decode()
        params = {
            "client_id": jwt_settings.OIDC_ADMIN_CLIENT_ID,
            "redirect_uri": redirect_uri,
            "response_type": "code",
            "state": state,
            "scope": jwt_settings.OIDC_ADMIN_SCOPE,
            "code_challenge": pkce_secret.challenge,
            "code_challenge_method": pkce_secret.challenge_method,
            "ui_locales": "en",
            "nonce": get_random_string(),
        }
        cache.set(state, str(pkce_secret), timeout=600)
        log.info(f"OIDC Admin login: {authorization_endpoint}?{urlencode(params)}")
        return redirect(f"{authorization_endpoint}?{urlencode(params)}")


class ReceiveRedirectView(AbsView):
    def get(self, request):
        code = request.GET.get("code")
        state = request.GET.get("state")
        if not code or not state:
            log.warning(f"No code or state in the request {request.GET}")
            raise BadRequestException("No code or state in the request")

        redirect_uri = request.build_absolute_uri(reverse("receive_redirect_view"))
        if state := cache.get(state):
            token = get_access_token(code, redirect_uri, state)
            data = oidc_handler.decode_token(token)
            user = UserHandler(data, request, token).get_user()
            log.info(f"OIDC Admin login: {user}", extra={"data": data})
            roles = role_handler.apply(user, data)
            if not user.is_staff:
                raise BadRequestException(f"User {user.email} is not staff\nRoles: {roles}")
            login(request, user, backend=jwt_settings.OIDC_AUTHORIZATION_BACKEND)
            return redirect("admin:index")

        raise BadRequestException("No PKCE secret found in cache")


class LogoutView(AbsView):
    def get(self, request):
        return index_response(request, "Logged out", status=401)
