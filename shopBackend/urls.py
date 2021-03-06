from django.contrib import admin
from django.urls import path, include
from . import views
from .routers import router

urlpatterns = [
    path('', include(router.urls)),
    path('myinfo', views.info, name='info'),
    path('csrf_token', views.get_csrf_token, name='csrf'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('check_login', views.check_login, name='login'),
    path('fetch_item', views.fetchItem, name='fetch_item'),
    path('google_oauth', views.google_oauth, name='google_oauth'),
    path('log_out', views.logout, name='logout'),
    path('notifs', views.get_ext_notifs, name="ext_notifs")
]
