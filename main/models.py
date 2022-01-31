from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from .manager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=12)
    isverified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()
    
    def has_perm(self, perm,obj=None):
        return self.is_admin

    def has_module_perms(self,app_label):
        return True

    def __str__(self):
        return self.email