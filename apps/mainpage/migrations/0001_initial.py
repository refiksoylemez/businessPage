# Generated by Django 3.1 on 2020-08-18 07:04

import apps.mainpage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=150, verbose_name='Başlık')),
                ('url', models.CharField(blank=True, max_length=150, null=True, verbose_name='Link')),
                ('butonBaslik', models.CharField(blank=True, max_length=150, null=True, verbose_name='Link Başlık')),
                ('resim', models.ImageField(default='images/noimageall.png', null=True, upload_to=apps.mainpage.models.photo_path)),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Slider',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
    ]
