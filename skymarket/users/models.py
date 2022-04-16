from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from skymarket.users.managers import UserRole, UserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, verbose_name="Пароль")
    last_login = models.DateTimeField(blank=True, null=True)
    phone = PhoneNumberField(verbose_name="Телефон для связи")
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER,
                            verbose_name="Роль пользователя")
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def __str__(self):
        return self.email

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_user(self):
        return self.role == UserRole.USER

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
