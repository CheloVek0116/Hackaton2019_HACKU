# Generated by Django 2.2.1 on 2019-07-14 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CustomUsers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Biology',
            field=models.ManyToManyField(blank=True, related_name='biology', to='statistic.biology', verbose_name='b'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Math',
            field=models.ManyToManyField(blank=True, related_name='math', to='statistic.math', verbose_name='m'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='Phisycs',
            field=models.ManyToManyField(blank=True, related_name='phisycs', to='statistic.phisycs', verbose_name='p'),
        ),
    ]
