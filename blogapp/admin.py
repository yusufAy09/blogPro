from django.contrib import admin
from .models import Blogs
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display="title","content","image"

admin.site.register(Blogs,BlogAdmin)