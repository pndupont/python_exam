from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard),
    url(r'^new/$', views.new_job),
    url(r'^create/$', views.create_job),
    url(r'^(?P<num>\d+)/$', views.read_job),
    url(r'^edit/(?P<num>\d+)/$', views.edit_job),
    url(r'^update/(?P<num>\d+)/$', views.update_job),
    url(r'^delete/(?P<num>\d+)/$', views.delete_job),
    url(r'^add/(?P<num>\d+)/$', views.add),
    url(r'^give_up/(?P<num>\d+)/$', views.give_up),
]