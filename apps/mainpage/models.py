from django.db import models
from django.contrib.auth.models import User
import os
from os.path import splitext, basename
import uuid


def photo_path(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s" % (uuid.uuid4(), ext)
    return os.path.join('images', newname)


# Create your models here.
class Slider(models.Model):
    baslik = models.CharField(max_length=150, verbose_name="Başlık")
    url = models.CharField(max_length=150, null=True, blank=True, verbose_name="Link")
    butonBaslik = models.CharField(max_length=150, null=True, blank=True, verbose_name="Link Başlık")
    resim = models.ImageField(upload_to=photo_path, null=True, default='images/noimageall.png')

    def __str__(self):
        return self.baslik

    @property
    def resim_url(self):
        if self.resim and hasattr(self.resim, 'url'):
            return self.resim.url

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )
