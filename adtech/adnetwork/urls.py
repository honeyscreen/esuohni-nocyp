from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^sample', views.sample, name='sample'),
]