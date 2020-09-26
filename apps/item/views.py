from django.shortcuts import render
from .models import Hizmetler
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
def services(request,slug):
    hizmet=get_object_or_404(Hizmetler,slug=slug)
    return render(request, "services.html",
                  {'hizmet': hizmet })