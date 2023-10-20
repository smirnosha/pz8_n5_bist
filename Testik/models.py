from django.db import models
from anketas.models import Professia


class MyTestik(models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name='Профессия')
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MyTestik._meta.fields]


class Answers(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Answers._meta.fields]


class Certificates(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Certificates._meta.fields]
