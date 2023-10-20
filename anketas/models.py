from django.contrib.auth.models import User
from django.db import models


class Professia(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Professia._meta.fields]


class Roles(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Roles._meta.fields]


class Skills(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Skills._meta.fields]


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


class Questions(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Questions._meta.fields]


class Certificates(models.Model):
    title = models.TextField(max_length=50, verbose_name='Название')
    file = models.TextField(max_length=50, verbose_name='Файл')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Certificates._meta.fields]


class MeTestik(models.Model):
    professia = models.ForeignKey(Professia, on_delete=models.PROTECT, verbose_name='Профессия')
    title = models.TextField(max_length=50, verbose_name='Название')

    class Meta:
        ordering = ['-title']
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'

    def __str__(self):
        return self.title

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in MeTestik._meta.fields]


class Gragdanin(User):
    mydata = models.TextField(max_length=50, verbose_name='Название')
    username = models.TextField(max_length=50, verbose_name='имя пользователя')
    first_name = models.TextField(max_length=50, verbose_name='имя')
    last_name = models.TextField(max_length=50, verbose_name='фамилия')

    def __str__(self):
        return self.username
