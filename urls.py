from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.views.generic import list_detail
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()
from logistics.models import Conveyance, Warehouse, Customs

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^about/$', direct_to_template, {'template':'about.html'}),
    url(r'^$', login),
    url(r'^accounts/profile/$', 'core.views.after_login')
)

urlpatterns += patterns('',
    url(r'^logistics/conveyances/$', list_detail.object_list, {
                                                'queryset':Conveyance.objects.all(),
                                                'template_name':'conveyances.html',
                                                'template_object_name':'conveyances_list'
                                                }),
    url(r'^logistics/warehouses/$', list_detail.object_list, {
                                                'queryset':Warehouse.objects.all(),
                                                'template_name':'warehouses.html',
                                                'template_object_name':'warehouses'
                                                }),
    url(r'^logistics/customs/$', list_detail.object_list, {'queryset':Customs.objects.all(),
                                                'template_name':'customs.html',
                                                'template_object_name':'customs'
                                                })
)
