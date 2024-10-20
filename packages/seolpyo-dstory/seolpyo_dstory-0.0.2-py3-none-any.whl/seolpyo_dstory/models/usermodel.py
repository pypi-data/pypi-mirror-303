from re import findall

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.core.validators import BaseValidator
from django.db import models


class UsernameValidator(BaseValidator):
    message = '닉네임은 한글, 영어, 숫자만 사용할 수 있으며, 단어 사이 공백은 1개만 사용할 수 있습니다.'
    def __init__(self, limit_value=3, message: str=None):
        super().__init__(limit_value, message)
    def compare(self, a, b):
        if len(a) < b:
            self.message = f'닉네임은 최소 {b}글자 이상이어야 합니다.'
            return True
        return a != ' '.join(findall('[a-zA-Zㄱ-ㅎ가-힣0-9]+', a))


class BaseUser(AbstractUser):
    class Meta:
        abstract = True
        verbose_name = '디스토리/사용자'
        verbose_name_plural = '사용자'
    first_name, last_name = (None, None)
    email = models.EmailField(verbose_name='로그인 이메일', unique=True,)
    username = models.CharField(
        verbose_name='닉네임',
        max_length=10,
        unique=True,
        help_text='닉네임은 한글, 영어, 숫자만 사용가능합니다.',
        validators=[UsernameValidator()],
    )

    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='seolpyo_dstory_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='seolpyo_dstory_user',
    )

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self): return self.username

class User(BaseUser):
    pass