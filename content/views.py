from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse

from content.models import *

# Create your views here.
def home(request):
    dict = {}
    dict['posts'] = Post.objects.all()[:3]
    dict['projects'] = Project.objects.all()[:5]
    return render_to_response('index.html', dict, context_instance=RequestContext(request))

def blog(request):
    tags = Tag.objects.all().order_by("title")
    posts = Post.objects.all().order_by("-pub_date")
    paginator = Paginator(posts, 5)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog.html", dict(posts=posts, tags=tags), context_instance=RequestContext(request))

def view_post(request, slug):
	dict = {}
	dict['post'] = get_object_or_404(Post, slug=slug)
	return render_to_response('view_post.html', dict, context_instance=RequestContext(request))

def view_tag(request, slug):
	dict = {}

	tag = get_object_or_404(Tag, slug=slug)
	dict['tag'] = tag
	dict['tags'] = Tag.objects.all().order_by("title")

	posts = Post.objects.filter(tag=tag).order_by("-pub_date")
	paginator = Paginator(posts, 5)
	
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1
	try:
	    posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
	    posts = paginator.page(paginator.num_pages)

	dict['posts'] = posts
	return render_to_response('view_tag.html', dict, context_instance=RequestContext(request))

def contact(request):
    form = ContactForm()
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid():
    		subject = form.cleaned_data['subject']
    		message = form.cleaned_data['message']
    		sender = form.cleaned_data['name']

    		recipients = ['sophiechanga@gmail.com']
    		send_mail(subject, message, sender, recipients)
    		return HttpResponseRedirect('/dev/contact/thankyou/') # Redirect after POST

    return render(request, 'contact.html', {
        'form': form,
    })

def thankyou(request):
	return render_to_response('thankyou.html', context_instance=RequestContext(request))

def projects(request):
    dict = {}
    dict['projects'] = Project.objects.all()
    return render_to_response('projects.html', dict, context_instance=RequestContext(request))