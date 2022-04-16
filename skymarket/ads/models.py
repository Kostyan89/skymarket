from django.conf import settings
from django.db import models

from skymarket.users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    price = models.PositiveIntegerField(verbose_name="Цена")
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Автор")
    description = models.CharField(max_length=255, verbose_name="Описание")
    created_at = models.DateField(verbose_name="Дата создания")
    image = models.ImageField(upload_to="images/", verbose_name="Картинка", null=True, blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ("-created_at", )


class Comment(models.Model):
    text = models.CharField(max_length=1000,verbose_name="Текст")
    created_at = models.DateTimeField(verbose_name="Создано")
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Автор")
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name="Объявление")

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ("-created_at", )
