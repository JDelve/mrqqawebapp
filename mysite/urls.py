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
	url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
]
