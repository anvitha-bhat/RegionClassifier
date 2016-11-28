from django.conf.urls import url

from . import views

urlpatterns = [
	#/home/
    url(r'^$', views.home, name='home'),
    url(r'^classify', views.classify, name='classify'),

]
