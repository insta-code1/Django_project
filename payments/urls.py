from django.conf.urls import url
from payments import views

urlpatterns = [
    url(r'^bookings/$', views.payment, name='bookings'),
]