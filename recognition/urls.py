from django.conf.urls import url
from . import views

app_name = 'recognition'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    #url(r'^(?P<image_pk>[0-9]+)/$', views.ImageDetailView.as_view(), name = 'recognition_image_upload'),
    url(r'^(?P<id>\d+)/$', views.img_detail, name = 'recognition_image_upload'),
]