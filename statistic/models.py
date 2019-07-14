from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class biology(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название сайта')
    link = models.CharField(max_length=50, verbose_name='Ccылка сайта')


class math(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название сайта')
    link = models.CharField(max_length=50, verbose_name='Ccылка сайта')


class phisycs(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название сайта')
    link = models.CharField(max_length=50, verbose_name='Ccылка сайта')
