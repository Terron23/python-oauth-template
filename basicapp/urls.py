from django.urls import re_path, include
from basicapp import views
from django.contrib import admin


app_name = 'basicapp'

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.user_login, name='user_login')
]