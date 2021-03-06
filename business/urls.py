"""eCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.urls import include
from django.contrib.auth import views as authViews
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from apps.mainpage.views import mainPage,online
from apps.corporate.views import corporate
from apps.userform.views import careers, contacts
from apps.item.views import services
urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', mainPage, name='mainPage'),
    path(_('hizmetler/<slug:slug>'), services, name='services'),
    path(_('kurumsal/'), corporate, name='corporate'),
    path(_('kariyer/'), careers, name='careers'),
    path(_('iletisim/'), contacts, name='contacts'),
    path(_('online/'), online, name='online'),
    path(_('rosetta/'), include('rosetta.urls')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL) + static(settings.MEDIA_URL,
                                                                                          document_root=settings.MEDIA_ROOT)
