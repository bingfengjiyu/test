from django.conf.urls import url
from booktest import views
# 将页面转到对应的应用下
urlpatterns=[
    url(r'^index$',views.index),
    url(r'^(\d+)/$',views.detail),
]