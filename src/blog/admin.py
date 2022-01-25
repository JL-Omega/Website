from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'last_updated', 'created_on', 'published', 'content',)
    list_editable = ('published',)


admin.site.register(BlogPost, BlogPostAdmin)
