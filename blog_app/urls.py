from django.conf.urls import url

from blog_app import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='blog_index'),
]
