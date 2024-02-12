from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.functions import Now
from rest_framework.authtoken.models import Token
from django.db import models


class CustomAccountManager(BaseUserManager):

    def create_user(self, email, username, password):
        if not email:
            raise ValueError("The email address is required")
        if not username:
            raise ValueError("Then username is required")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=email, username=username, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(db_default=Now())
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
    ]

    objects = CustomAccountManager()

    def __string__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
