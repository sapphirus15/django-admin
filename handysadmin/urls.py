from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.adminuser_list, name='adminuser_list'),
    # url(r'^$', views.index, name='index'),
    # url(r'^$', views.base, name='base'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^host_list', views.host_list, name='host_list'),
]