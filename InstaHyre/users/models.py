from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from uuid import uuid4

class CustomAccountManager(BaseUserManager):

    def create_superuser(self, *args, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """

        phone_number = kwargs.get('phone_number', None)
        if not phone_number:
            kwargs['phone_number'] = 9140389589

        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

    def create_user(self, *arg, **kwargs):
        """Create and return a `User` with an phone_number, name and password."""
        print(arg)
        print(kwargs)

        name = kwargs.get('name', None)
        email = kwargs.get('email', None)
        phone_number = kwargs.get('phone_number', None)
        password = kwargs.get('password', None)

        if not phone_number:
            raise TypeError('Users must have a phone phone_number')

        if not password:
            raise TypeError('Users must have a password.')

        user = self.model(
            name = name,
            phone_number = phone_number,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):

    u_id = models.UUIDField(default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(_('email address'), unique=True, blank=True)
    password = models.CharField(max_length=15)
    spam_flag = models.IntegerField(default=0)
   
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['name', 'password','email']

    def __str__(self):
        return self.name