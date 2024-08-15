"""Rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


admin.site.site_header = "Rental Admin"
admin.site.site_title = "Rental Admin Portal"
admin.site.index_title = "Welcome to Rental Admin Portal"

admin.autodiscover()
urlpatterns = [
    path(r'', RedirectView.as_view(url='/index/')),
    path(r'index/',views.index),
    path(r'home/',views.home),
	path(r'contact/', views.contact),
    path(r'about/',views.about),
	path(r'admin/',admin.site.urls),
    path(r'user/',include('user.urls')),
    path(r'register', views.register),
    path(r'login', views.login_view),
    path(r'profile/',views.profile),
    path(r'post/', views.post),
    path(r'posth/', views.posth),
    path(r'logout', LogoutView.as_view()),
    path(r'descr/',views.descr),
    path(r'deleter', views.deleter),
    path(r'deleteh', views.deleteh),
    path(r'search/', views.search)
]

urlpatterns+= staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# urlpatterns+= mediafiles_urlpatterns()