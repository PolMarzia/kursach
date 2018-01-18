from django.db import models
from django.utils import timezone
# Create your models here.
class Human(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Человека"

class Uslugi(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    meta_opis = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/img')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

class Master(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    usl = models.ForeignKey(Uslugi)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"