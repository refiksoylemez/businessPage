# Generated by Django 3.1 on 2020-09-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_hizmetler_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='hizmetler',
            name='detay',
            field=models.TextField(null=True, verbose_name='Detay'),
        ),
        migrations.AddField(
            model_name='hizmetler',
            name='resim',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Resim'),
        ),
    ]
