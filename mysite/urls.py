
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    re_path(r'^accounts/login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
