from ..common.oneTextField import OneTextField


class Kariyer(OneTextField):
    class Meta:
        verbose_name = 'Kariyer'
        verbose_name_plural = 'Kariyer'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )

class Iletisim(OneTextField):
    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim'
        default_permissions = ()
        permissions = (('liste', 'Listeleme Yetkisi'),
                       ('sil', 'Silme Yetkisi'),
                       ('ekle', 'Ekleme Yetkisi'),
                       ('guncelle', 'Güncelleme Yetkisi')
                       )