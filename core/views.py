# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView
from core.forms import FeedbackForm

def after_login(request):
    return render_to_response('dashboard.html', {'user': request.user}, context_instance=RequestContext(request))

class FeedbackView(FormView):
    template_name = 'core/feedback.html'
    success_url = '/feedback/'
    form_class = FeedbackForm
    
    def form_valid(self, form):
        print 'Eh'
        return HttpResponseRedirect(self.success_url)
