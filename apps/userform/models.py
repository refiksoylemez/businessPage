from django.db import models
from ..common.mixins import AuditMixin
from django.utils.translation import gettext_lazy as _
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Kariyer(AuditMixin):
    ad = models.CharField(max_length=200, null=True, verbose_name=_('Ad'))
    soyAd = models.CharField(max_length=200, null=True, verbose_name=_('Soyad'))
    ePosta = models.CharField(max_length=200, null=True, verbose_name=_('E-Posta'))
    adres = models.TextField(null=True, verbose_name=_('Adres'))
    telefon = models.CharField(max_length=200, null=True, verbose_name=_('Telefon'))
    cv = models.FileField(upload_to=user_directory_path, null=True, verbose_name=_('Özgeçmiş'))
    mesaj = models.TextField(null=True, verbose_name=_('Mesaj'))

    class Meta:
        verbose_name = _('Kariyer')
        verbose_name_plural = _('Kariyer')
        default_permissions = ()
        permissions = ((_('liste'), _('Listeleme Yetkisi')),
                       (_('sil'), _('Silme Yetkisi')),
                       (_('ekle'), _('Ekleme Yetkisi')),
                       (_('guncelle'), _('Güncelleme Yetkisi'))
                       )


class Iletisim(AuditMixin):
    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )
