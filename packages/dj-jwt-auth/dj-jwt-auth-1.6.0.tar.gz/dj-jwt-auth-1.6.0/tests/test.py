from datetime import datetime
from http import HTTPStatus
from unittest.mock import Mock, patch

import pytz
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.test import TestCase
from django.urls import reverse
from jwt.api_jwt import ExpiredSignatureError

from django_jwt import settings
from django_jwt.middleware import JWTAuthMiddleware
from django_jwt.roles import ROLE
from django_jwt.user import role_handler

utc = pytz.UTC
access_token_payload = {
    "sub": "1234",
    "updated_at": 2687276498,
}
user_info_payload = {
    "sub": "1234",
    "email": "example@bk.com",
    "name": "UserName",
    "given_name": "1st name",
    "family_name": "LastName",
}
User = get_user_model()


def _on_create(user, request, token_data):
    user.username = "on_create"
    user.save()


def _on_update(user, request, token_data):
    user.username = "on_update"
    user.save()


def test_mapper(user_data: dict) -> dict:
    """Override user data - set username to 'override'"""

    return {
        "username": "override",
        "first_name": user_data["given_name"],
        "last_name": user_data["family_name"],
    }


@patch("django_jwt.utils.OIDCHandler.decode_token", return_value=access_token_payload)
@patch("django_jwt.utils.OIDCHandler.get_user_info", return_value=user_info_payload)
class OIDCHandlerTest(TestCase):
    def setUp(self):
        self.middleware = JWTAuthMiddleware(get_response=lambda x: x)
        self.request = Mock()
        self.request.META = {"HTTP_AUTHORIZATION": "Bearer Token"}
        settings.OIDC_USER_MAPPING = {  # default mapping
            "given_name": "first_name",
            "family_name": "last_name",
            "name": "username",
        }

    def assertUserWithPayload(self):
        self.assertEqual(self.request.user.first_name, user_info_payload["given_name"])
        self.assertEqual(self.request.user.last_name, user_info_payload["family_name"])
        self.assertEqual(self.request.user.username, user_info_payload["name"])
        self.assertEqual(self.request.user.email, user_info_payload["email"])
        self.assertEqual(self.request.user.kc_id, user_info_payload["sub"])

    def test_keycloak_new_user(self, *_):
        """User is created if it doesn't exist in database"""
        self.middleware.process_request(self.request)
        self.assertUserWithPayload()

    def test_exists_kc_id_user(self, *_):
        """User exists in database by kc_id"""
        user = User.objects.create(kc_id="1234", first_name="", last_name="", username="")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_exists_kc_id_with_short_updated_at(self, access_token, *_):
        access_token.return_value["updated_at"] = "2020-01-01"
        """User exists in database by kc_id and updated_at is short"""
        user = User.objects.create(kc_id="1234", first_name="", last_name="", username="")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_exists_kc_id_without_updated_at(self, access_token, *_):
        del access_token.return_value["updated_at"]
        """User exists in database by kc_id and updated_at is short"""
        user = User.objects.create(kc_id="1234", first_name="", last_name="", username="")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_exists_email_user(self, *_):
        """User exists in database by email"""
        user = User.objects.create(email="example@bk.com")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_exists_multiple_kc_id(self, *_):
        """User exists in database by email"""
        user = User.objects.create(email="example@bk.com", kc_id="123")
        User.objects.create(email="example@gmail.com", kc_id="123", username="other")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_exists_email_differeent_kc_id_user(self, *_):
        """User exists in database by email but different kc_id"""
        user = User.objects.create(email="example@bk.com", kc_id="123")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)

        # fields are updated if they are changed in KeyCloak
        self.assertUserWithPayload()

    def test_profile_info(self, *_):
        """User has profile info"""

        headers = {"HTTP_AUTHORIZATION": "Bearer 1234"}
        response = self.client.get(reverse("profile"), **headers)
        self.assertContains(response, user_info_payload["email"])

    def test_expired_token(self, *_):
        """A token has been expired"""
        with patch(
            "django_jwt.utils.OIDCHandler.decode_token",
            side_effect=ExpiredSignatureError(),
        ):
            res = self.middleware.process_request(self.request)
            self.assertEqual(HTTPStatus.UNAUTHORIZED.value, res.status_code)
            self.assertEqual(b'{"detail": "expired token"}', res.content)

    def test_user_on_create(self, *_):
        """User is created on create"""

        settings.OIDC_USER_ON_CREATE = _on_create
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user.username, "on_create")

    def test_user_on_update(self, *_):
        """User is updated on update"""

        settings.OIDC_USER_ON_UPDATE = _on_update
        User.objects.create(kc_id="1234", first_name="", last_name="", username="")
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user.username, "on_update")

    def test_user_data_mapping(self, *_):
        """User data is mapped"""

        settings.OIDC_USER_MAPPING = {"name": "username", "given_name": "last_name", "family_name": "first_name"}
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user.username, user_info_payload["name"])
        self.assertEqual(self.request.user.first_name, user_info_payload["family_name"])
        self.assertEqual(self.request.user.last_name, user_info_payload["given_name"])

    def test_user_data_mapping_callable(self, *_):
        """User data is mapped"""

        settings.OIDC_USER_MAPPING = test_mapper
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user.username, "override")

    def test_updated_at(self, access_token, user_info):
        """Check that
        - the updated_at field saved correct
        - don't call userdata if updated_at is not changed
        """

        updated_at = utc.localize(datetime.fromtimestamp(access_token_payload["updated_at"]))
        user = User.objects.create(kc_id="1234", first_name="", last_name="", username="")

        self.middleware.process_request(self.request)
        self.assertEqual(self.request.user, user)
        user.refresh_from_db()
        self.assertEqual(user.modified_timestamp, updated_at)
        self.assertEqual(user.username, user_info_payload["name"])
        self.assertEqual(user_info.call_count, 1)

        self.middleware.process_request(self.request)
        user.refresh_from_db()
        self.assertEqual(user.modified_timestamp, updated_at)
        # self.assertEqual(user_info.call_count, 1)


class RolesTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username="user")
        settings.OIDC_ADMIN_ROLES = [
            ROLE(
                name="admin",
                is_superuser=True,
            ),
            ROLE(
                name="staff",
                groups=["staff group"],
                permissions=["add_user", "change_user", "delete_user"],
            ),
        ]
        self.group = Group.objects.create(name="staff group")
        self.permission = Permission.objects.get(name="Can add user")
        self.access_token = {"resource_access": {settings.OIDC_ADMIN_CLIENT_ID: {"roles": ["staff"]}}}

    def test_staff_role(self):
        self.access_token["resource_access"][settings.OIDC_ADMIN_CLIENT_ID]["roles"] = ["staff"]
        role_handler.apply(self.user, self.access_token)
        self.assertTrue(self.user.groups.filter(name="staff group").exists())
        self.assertTrue(self.user.user_permissions.filter(codename="add_user").exists())
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)

    def test_admin_role(self):
        self.access_token["resource_access"][settings.OIDC_ADMIN_CLIENT_ID]["roles"] = ["admin"]
        role_handler.apply(self.user, self.access_token)
        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)

    def test_apply_staff_then_admin_role(self):
        self.access_token["resource_access"][settings.OIDC_ADMIN_CLIENT_ID]["roles"] = ["staff"]
        role_handler.apply(self.user, self.access_token)
        self.assertFalse(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)
        self.assertTrue(self.user.groups.filter(name="staff group").exists())
        self.assertTrue(self.user.user_permissions.filter(codename="add_user").exists())

        self.access_token["resource_access"][settings.OIDC_ADMIN_CLIENT_ID]["roles"] = ["admin"]
        role_handler.apply(self.user, self.access_token)
        self.assertTrue(self.user.is_superuser)
        self.assertTrue(self.user.is_staff)
        self.assertTrue(self.user.groups.filter(name="staff group").exists())
        self.assertTrue(self.user.user_permissions.filter(codename="add_user").exists())
