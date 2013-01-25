from content.models import Image, Post, Tag, Project, Photosphere
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class PhotosphereAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Image)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Project)
admin.site.register(Photosphere, PhotosphereAdmin)