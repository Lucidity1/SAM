from django.conf.urls import url
from login import views
from django.contrib.auth import views as auth_views

app_name='login'

urlpatterns = [
	url(r'^$', auth_views.login, {'template_name':'login/login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout,  {'next_page':'/login'}, name='logout'),
]