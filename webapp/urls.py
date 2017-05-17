from django.conf.urls import url, include 
from . import views 
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
	

	url(r'^$', views.home_page, name='home_page'),
	url(r'^webapp/scanner_dates', views.get_dates, name = "scanner_dates"),
	url(r'^webapp/results', views.date_to_results, name = "date_to_results"),
	url(r'^webapp/phantom_notes', views.phantom_notes, name = "phantom_notes"),
	url(r'^webapp/version_notes', views.version_notes, name = 'version_notes'),
	url(r'^webapp/gradsys_notes', views.gradsys_notes, name = 'gradsys_notes'),
	url(r'^webapp/coil_notes', views.coil_notes, name = 'coil_notes'),
]
