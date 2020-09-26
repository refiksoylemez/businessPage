from django.shortcuts import render
from .forms import cvForm
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
            return render(request, 'careers.html',
                          {'form': form, 'Mesaj': _('Özgeçmiş formunuz elimize ulaşmıştır.')})

        else:
            form = cvForm()
            return render(request, 'careers.html', {'form': form, 'Mesaj': _('Hata! Lütfen Tekrar Deneyiniz.')})
