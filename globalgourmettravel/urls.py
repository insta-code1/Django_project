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
from accounts import views as accounts_views
from django.conf.urls import url, include
from django.contrib import admin
from travelapp import views
from django.contrib.staticfiles import views as static_views
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),

     # accounts URLs
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

       # Blog app URLs
    url(r'', include('blog_app.urls')),

    # Contact URLs
    url(r'', include('contact.urls')),

    # Guides ULRs
    url(r'^spain$', views.spainguide, name='spain'),


    # Payments URLs
    url(r'', include('payments.urls')),

    # static and media URLs
    url(r'^static/(?P<path>.*)$', static_views.serve),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]
