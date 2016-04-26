"""globalgourmettravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from travelapp import views
from django.contrib.staticfiles import views as static_views
from .settings import MEDIA_ROOT
import contact.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

    #Guides ulrs
    url(r'^spain$', views.spainguide, name='spain'),

    # Contact URLs
    #url(r'', include('contact.urls')),
    url(r'^contact$', contact.views.contact, name='contact'),

    # Blog app urls
    url(r'', include('blog_app.urls')),
    # static and media url
    url(r'^static/(?P<path>.*)$', static_views.serve),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]