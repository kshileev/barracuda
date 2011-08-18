# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def after_login(request):
    return render_to_response('tmp.html', {'user':request.user},
                              context_instance=RequestContext(request))