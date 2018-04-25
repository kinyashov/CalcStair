from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^API/$', views.stair_list),
    url(r'^API/(?P<pk>[0-9]+)/$', views.stair_detail),
]