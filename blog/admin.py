from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    # you can add many thisngs to this to make life easier ie: list_filter
    list_filter = ('status','created_on')
    # next two lines added as part of teachers challenge
    list_display = ('title', 'slug','status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')


# admin.site.register(Post)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

     
    # next three lines added as part of teachers challenge
    list_filter = ('approved','created_on')
    list_display = ('name','body', 'post', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


