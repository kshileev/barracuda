from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, TemplateView
from django.contrib import admin
from django.contrib.auth.views import login,logout
admin.autodiscover()
from logistics.models import Conveyance, Warehouse, Customs
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', login_required(TemplateView.as_view(template_name='dashboard.html'))),
    url(r'^accounts/login/$', login),
    url(r'^logout/$', logout),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'))
)

urlpatterns += patterns('',
    url(r'^logistics/conveyances/$', ListView.as_view(model=Conveyance,context_object_name='conveyance_list')),
    url(r'^logistics/warehouses/$', ListView.as_view(model=Warehouse,context_object_name='warehouse_list')),
    url(r'^logistics/customs/$', ListView.as_view(model=Customs,context_object_name='customs_list'))
)
