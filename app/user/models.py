from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django_mysql.models import JSONField
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields['is_superuser'] = True
        return self.create_user(username, password, **extra_fields)


class User(AbstractBaseUser):
    """用户"""
    username = models.CharField(primary_key=True, max_length=64)
    password = models.CharField(max_length=128)  # 6-64位
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=32, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    # roles = models.ManyToManyField(
    #     'Role', related_name='users', blank=True)
    permissions = JSONField(default=list)
    remark = models.CharField(max_length=256, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    objects = UserManager()

    def get_item(self):
        return {'username': self.username, 'name': self.name}

    # def has_permission(self, method, permission):
    #     return self.is_superuser or f'{method}_{permission}'.lower() in self.permissions


class Role(models.Model):
    """角色"""
    number = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    permissions = JSONField(default=list)
    remark = models.CharField(max_length=256, blank=True, null=True)

    def get_item(self):
        return {'id': self.id, 'number': self.number, 'name': self.name}
