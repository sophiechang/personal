from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

# Create your views here.
def home(request):
    return render_to_response('index.html', {}, context_instance=RequestContext(request))
    
def about(request):
    return render_to_response('about.html', {}, context_instance=RequestContext(request))