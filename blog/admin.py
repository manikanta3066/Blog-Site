from django.contrib import admin
from .models import Post
# Register your models here.
admin.site.register(Post)
# admin.site.register(Comment)

class PostAdmin(admin.ModelAdmin):
    list_display=('title','author','created_at')
    search_fields=('title','content')
    