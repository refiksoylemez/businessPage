from django.shortcuts import render
from ..corporate.models import kurumsalDetay
# Create your views here.
def corporate(request):
    kurumsal=kurumsalDetay.objects.all().translate(request.LANGUAGE_CODE)
    return render(request, "corporate.html")