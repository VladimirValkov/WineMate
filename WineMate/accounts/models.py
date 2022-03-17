from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.shortcuts import redirect


class UserManager(BaseUserManager):
    def create_user(self, code, name, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            code=code,
            name=name,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, code, email, name, password):
        user = self.create_user(
            code,
            email,
            name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default='')
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
    )
    is_active = models.BooleanField(default=True)
    is_reader = models.BooleanField(default=False)
    is_writer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'code'
    REQUIRED_FIELDS = ['name', 'email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, perm, obj=None):
        return True

    @property
    def is_staff(self):
        return self.is_admin
