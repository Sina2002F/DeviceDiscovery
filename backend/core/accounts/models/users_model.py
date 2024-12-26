from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from accounts.manager import CustomUserManager



class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField("Email Address",max_length=254)
    is_admin = models.BooleanField(default=False)
    is_validator = models.BooleanField(default=False)
    updated_date = models.DateField(auto_now=False, auto_now_add=True)
    created_date = models.DateField(auto_now=False, auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
