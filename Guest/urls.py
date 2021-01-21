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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


admin.site.site_header = "Rental Admin"
admin.site.site_title = "Rental Admin Portal"
admin.site.index_title = "Welcome to Rental Admin Portal"

admin.autodiscover()
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/index/')),
    url(r'^index/',views.index),
    url(r'^home/',views.home),
	url(r'^contact/', views.contact),
    url(r'^about/',views.about),
	url(r'^admin/',admin.site.urls),
    url(r'^user/',include('user.urls')),
    url(r'^register', views.register),
    url(r'^login', views.login_view),
    url(r'^profile/',views.profile),
    url(r'^post/$', views.post),
    url(r'^posth/$', views.posth),
    url(r'^logout', LogoutView.as_view()),
    url(r'^descr/',views.descr),
    url(r'^deleter', views.deleter),
    url(r'^deleteh', views.deleteh),
    url(r'^search/', views.search)
]

urlpatterns+= staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# urlpatterns+= mediafiles_urlpatterns()