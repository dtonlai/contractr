from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.ContractrIndexView.as_view(), name='index'),
    url(r'accounts/',include('django.contrib.auth.urls')),
    url(r"accounts/", include('accounts.urls', namespace='accounts')),
]
