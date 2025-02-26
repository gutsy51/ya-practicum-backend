from django.contrib import admin

from .models import Group, Post, Comment


admin.site.empty_value_display = '-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'slug',
        'short_description',
    )
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'slug',)
    list_display_links = ('title',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'short_text',
        'author',
        'group',
        'image',
        'pub_date',
    )
    list_filter = ('pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_display_links = ('short_text',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'short_text',
        'author',
        'post',
        'created',
    )
    list_filter = ('created', 'author', 'post',)
    search_fields = ('text',)
    list_display_links = ('short_text',)
