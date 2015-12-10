from django.conf.urls import include, url
from django.contrib import admin
from cards import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.home, name ='home'),
    url(r'^cards/', include('cards.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/$', views.register, name='register'), # ADD NEW PATTERN!
    url(r'^logout/$', views.user_logout, name='logout'), # ADD NEW PATTERN!
    url(r'^login/$', views.user_login, name='login'), # ADD NEW PATTERN!
]
