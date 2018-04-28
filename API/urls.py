from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^API/$', views.StairList.as_view()),
    url(r'^API/(?P<pk>[0-9]+)/$', views.StairDetail.as_view()),
]