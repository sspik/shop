from django.conf.urls import url
from . import views


app_name = 'shop'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^catalog/(?P<pk>\d+)\.html$', views.item, name='item'),
    url(r'^(?P<full_url>.*/)$', views.catalog, name='catalog')
]