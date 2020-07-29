import jwt
from django.conf import settings
from rest_framework import authentication, exceptions
from users.models import User
from bayview.message_exception import (exception_deactivate_user, exception_invalid_auth,  # NOQA
                                       exception_unmatched_token)


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        request.user = None

        auth_header = authentication.get_authorization_header(request)
        token = auth_header.decode('utf-8')

        return self._authenticate_credentials(request, token)

    def _authenticate_credentials(self, request, token):
        """
        Try to authenticate the given credentials. If authentication is
        successful, return the user and token. If not, throw an error.
        """

        payload = {}

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except Exception:
            raise exceptions.AuthenticationFailed(exception_invalid_auth)

        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed(exception_unmatched_token)

        if not user.is_active:
            raise exceptions.AuthenticationFailed(exception_deactivate_user)
        return (user, token)
