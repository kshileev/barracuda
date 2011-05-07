from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from models import Conveyance

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Conveyance.objects, template_name='logistics.html')),
)
  