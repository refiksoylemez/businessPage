from django.contrib import admin
from .models import kurumsalDetay, kurumsalKonum
from translations.admin import TranslatableAdmin, TranslationInline

@admin.register(kurumsalDetay)
class kurumsalDetayAdmin(TranslatableAdmin):
    inlines = [TranslationInline,]
# Register your models here.

admin.site.register(kurumsalKonum)

