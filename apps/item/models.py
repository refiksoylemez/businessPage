from ..common.oneTextField import OneTextField


class Hizmetler(OneTextField):
    class Meta:
        verbose_name = 'Hizmetler'
        verbose_name_plural = 'Hizmetler'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )