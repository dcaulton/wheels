from django.conf.urls import include, url

import lidar.views

urlpatterns = [
    url(r'^$', lidar.views.index),
    url(r'^get_reading$', lidar.views.get_reading),
]
