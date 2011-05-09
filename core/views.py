# Create your views here.
from django.shortcuts import render_to_response

def after_login(request):
    return render_to_response('tmp.html', {'user':request.user})