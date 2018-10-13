from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField('昵称', max_length=25, default='')
    birday = models.DateField('生日', null=True, blank=True)
    mobile = models.CharField('手机', max_length=11)


