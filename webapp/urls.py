from django.conf.urls import url, include 
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	

	url(r'^$', views.home_page, name='home_page'),
	url(r'^webapp/scanner_dates', views.get_dates, name = "scanner_dates"),
	url(r'^webapp/results', views.date_to_results, name = "date_to_results"),
]
