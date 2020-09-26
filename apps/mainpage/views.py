from django.shortcuts import render
from ..corporate.models import kurumsalDetay
# Create your views here.
def mainPage(request):
    kurumsal=kurumsalDetay.objects.all().translate(request.LANGUAGE_CODE)
    return render(request, "index.html")

