from django.db import models
from django.db.models import permalink
import urllib2, urlparse
from django.core.files.base import ContentFile
from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

def get_image_path(instance, filename):
    return os.path.join('img', str(instance.category), filename)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    teaser = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, db_index=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    tag = models.ForeignKey('content.Tag')
    author = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.title
        
    @permalink
    def get_absolute_url(self):
        return ('view_post', None, {'slug': self.slug})

class Image(models.Model):
	post = models.ForeignKey(Post, related_name="images")
	image_path = models.ImageField(upload_to="images/%Y/%m/%d")
	url = models.CharField(max_length=150, blank=True)
	
	timestamp = models.DateTimeField(auto_now_add=True)
	
	def __unicode__(self):
		if self.pk is not None:
			return "{{ %d }}" % self.pk
		else:
			return "deleted image"

class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return self.title
        
    @permalink
    def get_absolute_url(self):
        return ('view_tag', None, {'slug': self.slug})
        
class ContactForm(forms.Form):
    name = forms.EmailField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

class Project(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(max_length=200)
    pic = models.ImageField(upload_to=get_image_path)
    
    def __unicode__(self):
    	return self.title
    	
    @permalink
    def get_absolute_url(self):
    	return ('view_project', None, {'slug': self.title})