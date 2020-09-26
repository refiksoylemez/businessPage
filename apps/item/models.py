from ..common.oneTextField import OneTextField
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.db import models
from ..common.oneTextField.oneField import OneTextField
from ..common.mixins.audit import AuditMixin
from django.contrib.auth.models import Group, User


class Hizmetler(OneTextField):
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return (self.text)

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
