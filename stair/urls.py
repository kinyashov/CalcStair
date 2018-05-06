from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stair/$', views.StairList.as_view()),
    url(r'^stair/(?P<pk>[0-9]+)/$', views.StairDetail.as_view()),
]