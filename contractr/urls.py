from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from contractr_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.ContractrIndexView.as_view(), name='index'),
]
