# Generated by Django 3.1 on 2020-08-18 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kurumsalKonum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(blank=True, editable=False, max_length=100, null=True)),
                ('updated_by', models.CharField(blank=True, editable=False, max_length=255, null=True)),
                ('text', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
            ],
            options={
                'verbose_name': 'Kurumsal Konum',
                'verbose_name_plural': 'Kurumsal Konumlar',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='kurumsalDetay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=150, verbose_name='Başlık')),
                ('icerik', models.TextField(blank=True, default='', null=True, verbose_name='İçerik')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='corporate.kurumsalkonum', verbose_name='Konum')),
            ],
            options={
                'verbose_name': 'Kurumsal',
                'verbose_name_plural': 'Kurumsal',
                'permissions': (('liste', 'Listeleme Yetkisi'), ('sil', 'Silme Yetkisi'), ('ekle', 'Ekleme Yetkisi'), ('guncelle', 'Güncelleme Yetkisi')),
                'default_permissions': (),
            },
        ),
    ]
