from datetime import datetime, timedelta
import jwt
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin)
from bayview.models import AbstractBayView
from .manager import UserManager
from business_units.models import BusinessUnit

# write custom model here


class User(AbstractBaseUser, SafeDeleteModel, AbstractBayView):  # NOQA

    _safedelete_policy = SOFT_DELETE_CASCADE

    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('business_user', 'Business User'),
    )

    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=30, default="")
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    email = models.EmailField(unique=True, db_index=True)
    is_registered = models.BooleanField(default=False)
    user_type = models.CharField(max_length=13, choices=USER_TYPE_CHOICES)
    business_unit = models.ForeignKey(
        BusinessUnit, null=True, blank=True, on_delete=models.CASCADE)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        data = self._generate_jwt_token()
        token = data[0]
        exp_time = data[1]
        return {'token': token,  'exp_time': exp_time}

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.first_name + ' ' + self.last_name

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.id,
            'is_active': self.is_active,
            'is_staff': self.is_staff,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'exp': int(dt.strftime('%s'))*1000
        }, settings.SECRET_KEY, algorithm='HS256')
        # print(token.decode('utf-8'))
        return [token.decode('utf-8'), int(dt.strftime('%s'))*1000]


class UserToken(SafeDeleteModel, AbstractBayView):
    _safedelete_policy = SOFT_DELETE_CASCADE

    user = models.OneToOneField(
        User, related_name='user_tokens', on_delete=models.CASCADE)

    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.token
