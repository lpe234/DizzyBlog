#coding=utf-8
from django.contrib import admin
from models import Article, Author, Theme, Tag, Category, Comment
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'author', 'abstract', 'theme', 'category', 'content', 'tags']
    list_display = ['id', 'title', 'theme', 'category', 'tag_display', 'created_time', 'click_count', 'comment_count']
    list_editable = ['title', 'theme', 'category']
    list_filter = []
    list_display_links = ['id']
    search_fields = ['title']

    def tag_display(self, obj):
        return ','.join([tag.name for tag in obj.tags.all()])

    tag_display.short_description = u'标签'


class CAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name', 'created_time']

admin.site.register(Article, ArticleAdmin)
admin.site.register([Author, Theme, Tag, Category], CAdmin)
admin.site.register(Comment)