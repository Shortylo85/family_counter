from django.conf.urls import url
from django.contrib.auth.views import login
from ui import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_map/$', views.getMap, name='getMap'),
    url(r'^register/$', views.register, name='register'),
    url(r'login/$', login, {'template_name': 'account/login.html' }, name='user_login')
    
]
