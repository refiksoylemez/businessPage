# Generated by Django 3.1 on 2020-09-26 20:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0004_auto_20200926_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='iletisim',
            name='ad',
            field=models.CharField(max_length=200, null=True, verbose_name='Ad'),
        ),
        migrations.AddField(
            model_name='iletisim',
            name='ePosta',
            field=models.CharField(max_length=200, null=True, verbose_name='E-Posta'),
        ),
        migrations.AddField(
            model_name='iletisim',
            name='mesaj',
            field=models.TextField(null=True, verbose_name='Mesaj'),
        ),
        migrations.AddField(
            model_name='iletisim',
            name='soyAd',
            field=models.CharField(max_length=200, null=True, verbose_name='Soyad'),
        ),
        migrations.AddField(
            model_name='iletisim',
            name='telefon',
            field=models.CharField(max_length=200, null=True, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='kariyer',
            name='created_by',
            field=models.CharField(blank=True, editable=False, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='kariyer',
            name='updated_by',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]
