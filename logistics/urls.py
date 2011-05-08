from django.conf.urls.defaults import patterns, url
from django.views.generic import list_detail
from models import Conveyance, Warehouse, Customs

urlpatterns = patterns('',
    url(r'^conveyances/$', list_detail.object_list, {
                                                'queryset':Conveyance.objects.all(),
                                                'template_name':'conveyances.html',
                                                'template_object_name':'conveyances_list'
                                                }),
    url(r'warehouses/$', list_detail.object_list, {
                                                'queryset':Warehouse.objects.all(),
                                                'template_name':'warehouses.html',
                                                'template_object_name':'warehouses'
                                                }),
    url(r'customs/$', list_detail.object_list, {'queryset':Customs.objects.all(),
                                                'template_name':'customs.html',
                                                'template_object_name':'customs'
                                                })
)
  