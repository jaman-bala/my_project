from django.db import models


class Post(models.Model):
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    name = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")
    pin = models.IntegerField(max_length=255, verbose_name="ПИН")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    plot = models.TextField(verbose_name="Фабула")
    image = models.ImageField(upload_to='media', null=True, verbose_name="Фото 3x4")
    image1 = models.ImageField(upload_to='media', null=True, verbose_name="Фото в рост")
    image2 = models.ImageField(upload_to='media', null=True, verbose_name="Фото с боку")
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Добавить"
        verbose_name_plural = "Добавить данные"

    def __str__(self):
        return self.name

