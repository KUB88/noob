from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tables.html', views.spiderResult, name='tables'),
    url(r'^torrent/', views.spiderResult, name='spiderResult'),
    url(r'.', views.index, name='all')
]