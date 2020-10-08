from ..common.oneTextField import OneTextField
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from ..common.oneTextField.oneField import OneTextField
from ..common.mixins.audit import AuditMixin
from django.contrib.auth.models import Group, User
from translations.models import Translatable



class SunulanHizmetler(Translatable):
    text = models.CharField(max_length=200, null=True, verbose_name="Başlık")

    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return (self.text)



    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(SunulanHizmetler, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Sunulan Hizmetler')
        verbose_name_plural = _('Sunulan Hizmetler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi'))
                       )


class Hizmetler(Translatable):
    text = models.CharField(max_length=200, null=True, verbose_name="Başlık")

    detay = models.TextField(null=True, verbose_name=_('Detay'))

    resim = models.ImageField(('Resim'), upload_to='images/', null=True, )
    sunulanHizmet = models.ManyToManyField(SunulanHizmetler, blank=True, verbose_name="Sunulan Hizmetler")
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return (self.text)

    @property
    def resim_url(self):
        if self.resim and hasattr(self.resim, 'url'):
            return self.resim.url

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text)
        super(Hizmetler, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Hizmetler')
        verbose_name_plural = _('Hizmetler')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi'))
                       )
