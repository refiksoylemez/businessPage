# Generated by Django 3.1 on 2020-09-26 11:06

import apps.userform.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iletisim',
            name='text',
        ),
        migrations.RemoveField(
            model_name='kariyer',
            name='text',
        ),
        migrations.AddField(
            model_name='kariyer',
            name='ad',
            field=models.CharField(max_length=200, null=True, verbose_name='Ad'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='adres',
            field=models.TextField(null=True, verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='cv',
            field=models.FileField(null=True, upload_to=apps.userform.models.user_directory_path, verbose_name='Özgeçmiş'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='ePosta',
            field=models.CharField(max_length=200, null=True, verbose_name='E-Posta'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='mesaj',
            field=models.TextField(null=True, verbose_name='Mesaj'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='soyAd',
            field=models.CharField(max_length=200, null=True, verbose_name='Soyad'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='telefon',
            field=models.CharField(max_length=200, null=True, verbose_name='Telefon'),
        ),
    ]