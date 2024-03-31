from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'created', 'updated', 'user', 'like_count', 'comment_count', 'is_public', 'saved_by_user', 'title')


admin.site.register(Post, PostAdmin)
