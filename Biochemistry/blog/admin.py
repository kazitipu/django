from django.contrib import admin

# Register your models here.
from .models import BlogPost, Message


admin.site.register(BlogPost)
admin.site.register(Message)