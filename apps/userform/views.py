from django.shortcuts import render
from .forms import cvForm, iletisimForm
from django.utils.translation import gettext_lazy as _


# Create your views here.
def careers(request):
    if request.method == 'GET':
        form = cvForm()
        return render(request, 'careers.html', {'form': form})

    else:
        form = cvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = cvForm()
            return render(request, 'careers.html',
                          {'form': form, 'Mesaj': _('Özgeçmiş formunuz elimize ulaşmıştır.')})
        else:
            form = cvForm()
            return render(request, 'careers.html', {'form': form, 'Mesaj': _('Hata! Lütfen Tekrar Deneyiniz.')})


# Create your views here.
def contacts(request):
    if request.method == 'GET':
        form = iletisimForm()
        return render(request, 'contacts.html', {'form': form})

    else:
        form = iletisimForm(request.POST)
        if form.is_valid():
            form.save()
            form = iletisimForm()
            return render(request, 'contacts.html',
                          {'form': form, 'Mesaj': _('Mesajınız elimize ulaşmıştır.')})
        else:
            form = iletisimForm()
            return render(request, 'contacts.html', {'form': form, 'Mesaj': _('Hata! Lütfen Tekrar Deneyiniz.')})
