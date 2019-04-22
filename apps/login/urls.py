from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^register/$', views.create_user),
    url(r'^login_check/$', views.login_check),
    url(r'^myaccount/(?P<num>\d+)/$', views.myaccount),
    url(r'^update_myaccount/(?P<num>\d+)/$', views.update_myaccount),
    url(r'^logout/$', views.logout),
]