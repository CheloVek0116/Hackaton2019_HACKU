from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from statistic.models import biology, math, phisycs


class CustomUser(AbstractUser):
    SEX_CHOICES = (

        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Not specified'),
    )

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    sex = models.CharField(max_length=1, choices=SEX_CHOICES,
                           null=True, verbose_name='Пол', default='N')
    age = models.PositiveIntegerField(null=True, blank=True)

    # statistic

    Biology = models.ManyToManyField(
        biology, verbose_name='b', blank=True, related_name="user")
    Math = models.ManyToManyField(
        math, verbose_name='m', blank=True, related_name="user")
    Phisycs = models.ManyToManyField(
        phisycs, verbose_name='p', blank=True, related_name="user")

    def __str__(self):
        return self.username
