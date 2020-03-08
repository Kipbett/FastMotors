from django.conf.urls import url
from . import views

app_name = 'FastMotorsApp'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^supervisor', views.supervisor, name='supervisor'),
    url(r'^security', views.security, name='security')
]
