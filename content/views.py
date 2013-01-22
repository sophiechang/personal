from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from content.models import *

# Create your views here.
def home(request):
    dict = {}
    dict['posts'] = Post.objects.all()[:3]
    dict['projects'] = Project.objects.all()[:5]
    return render_to_response('index.html', dict, context_instance=RequestContext(request))

def blog(request):
    dict = {}
    dict['posts'] = Post.objects.all()
    dict['tags'] = Tag.objects.all()
    return render_to_response('blog.html', dict, context_instance=RequestContext(request))

def view_post(request, slug):
	dict = {}
	dict['post'] = get_object_or_404(Post, slug=slug)
	return render_to_response('view_post.html', dict, context_instance=RequestContext(request))

def view_tag(request, slug):
	dict = {}
	dict['tag'] = get_object_or_404(Tag, slug=slug)
	return render_to_response('view_tag.html', dict, context_instance=RequestContext(request))

def contact(request):
    dict = {}
    return render_to_response('contact.html', dict, context_instance=RequestContext(request))

def projects(request):
    dict = {}
    dict['projects'] = Project.objects.all()
    return render_to_response('projects.html', dict, context_instance=RequestContext(request))