from django.shortcuts import render
from ..corporate.models import kurumsalDetay
from ..item.models import Hizmetler
# Create your views here.
def mainPage(request):
    kurumsal=kurumsalDetay.objects.all().translate(request.LANGUAGE_CODE)
    return render(request, "index.html")


def live(request):
    menuList = Hizmetler.objects.all()
    return {'menuList': menuList, }
