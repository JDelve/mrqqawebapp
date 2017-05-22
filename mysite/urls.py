from django.conf.urls import url, include 
from django.contrib import admin
from django.contrib.auth import views as auth_views
from webapp import views 

urlpatterns = [
	url(r'^accounts/login/$', auth_views.login, name='login'),
	url(r'^accounts/logout/$', auth_views.logout, name='logout', kwargs={'next_page': '/accounts/login'}),
	url(r'^accounts/register/$', views.register, name='register'),
	url(r'^accounts/register/complete/$', views.registration_complete, name='registration_complete'),
	url(r'^admin/', admin.site.urls),
	url(r'', include('webapp.urls')),
	url(r'^accounts/register/registration/account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
	url(r'^account_activation_invalid/$', views.account_activation_invalid, name="account_activation_invalid")
]

