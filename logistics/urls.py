from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView, list_detail
from models import Conveyance, Warehouse, Customs

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(queryset=Conveyance.objects, template_name='logistics.html')),
    url(r'warehouses/$', list_detail.object_list, {'queryset':Warehouse.objects.all(), 'template_name':'warehouses.html'}),
    url(r'customs/$', list_detail.object_list, {'queryset':Customs.objects.all(),
                                                'template_name':'customs.html',
                                                'template_object_name':'customs'
                                                })
)
  