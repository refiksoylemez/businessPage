from django.db import models
from ..common.oneTextField import OneTextField
from ..common.mixins import AuditMixin
import os
from os.path import splitext
import uuid
from django.contrib.auth.models import User, Group


def photo_path(instance, filename):
    # Save original file name in model
    instance.original_file_name = filename

    # Get new file name/upload path
    base, ext = splitext(filename)
    newname = "%s%s" % (uuid.uuid4(), ext)
    return os.path.join('images', newname)


class kurumsalKonum(OneTextField):
    class Meta:
        verbose_name = 'Kurumsal Konum'
        verbose_name_plural = 'Kurumsal Konumlar'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )


class kurumsalDetay(models.Model):
    tip = models.ForeignKey(kurumsalKonum, on_delete=models.DO_NOTHING, verbose_name='Konum')
    baslik = models.CharField(max_length=150, verbose_name="Başlık")
    icerik = models.TextField(default="", null=True, blank=True, verbose_name="İçerik")

    def __str__(self):
        return self.baslik

    class Meta:
        verbose_name = 'Kurumsal'
        verbose_name_plural = 'Kurumsal'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )
