from .import views
from django.urls import path

urlpatterns =  [
    path ("base/", views.basepage, name = "basepage"),
    path ("", views.home, name = "home"),

]