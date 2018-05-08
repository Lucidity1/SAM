from django.conf.urls import url
from home import views

app_name='home'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^empty', views.empty_page, name='empty_page'),
	url(r'^news_page/(?P<article_id>[-\w]+)/$', views.news_page, name='news_page'),
	url(r'^browse/', views.browse, name='browse'),
	url(r'^browsesite/(?P<newsite>[-\w]+)/$', views.browseSite, name='browseSite'),
]