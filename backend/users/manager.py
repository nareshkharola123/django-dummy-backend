from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from safedelete.managers import SafeDeleteManager


# django customer manager


class UserManager(BaseUserManager, SafeDeleteManager):
    def create_user(self, email, **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not email:
            raise ValueError(_('The email must be set'))
        user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Staff must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email=username, password=password, **extra_fields)
