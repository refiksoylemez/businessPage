from django.contrib import admin
from .models import Hizmetler,SunulanHizmetler
from translations.admin import TranslatableAdmin, TranslationInline

@admin.register(Hizmetler)
class HizmetlerAdmin(TranslatableAdmin):
    inlines = [TranslationInline,]
    filter_horizontal = ('sunulanHizmet',)

@admin.register(SunulanHizmetler)
class SunulanHizmetlerAdmin(TranslatableAdmin):
    inlines = [TranslationInline,]

