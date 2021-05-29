from django.db import models

from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model

# Create your models here.

class FakeAddress(models.Model):
    address = models.TextField()

    def __str__(self):
        return self.address


class User(AbstractUser):
    username               = None
    email                  = models.EmailField(unique=True)
    mobile                 = models.CharField(max_length=20)
    first_name             = models.CharField(max_length=30)
    last_name              = models.CharField(max_length=30)
    is_varified        	   = models.BooleanField(default=False)
    email_token            = models.CharField(max_length=100, null=True, blank=True)
    forget_password        = models.CharField(max_length=20, null=True, blank=True)
    last_login_time        = models.DateTimeField(blank=True, null=True)
    last_logout_time       = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        # abstract = True 

# User = get_user_model()