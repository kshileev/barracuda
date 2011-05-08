from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from models import Conveyance, Warehouse

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Conveyance.objects, template_name='logistics.html')),
    url(r'warehouses/$', ListView.as_view(queryset=Warehouse.objects, template_name='warehouses.html')),
)
  