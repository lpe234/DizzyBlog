#coding=utf-8
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    name = models.CharField(u'名称', max_length=20)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Author(BaseModel):

    class Meta:
        db_table = 'dlog_author'
        verbose_name = u'作者'


class Theme(BaseModel):

    class Meta:
        db_table = 'dlog_theme'
        verbose_name = u'主题'


class Tag(BaseModel):

    class Meta:
        db_table = 'dlog_tage'
        verbose_name = u'标签'


class Category(BaseModel):

    class Meta:
        db_table = 'dlog_category'
        verbose_name = u'分类'


class Article(BaseModel):
    title = models.CharField(u'标题', max_length=100)
    author = models.ForeignKey(Author, verbose_name=u'作者')
    theme = models.ForeignKey(Theme, verbose_name=u'主题')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    category = models.ForeignKey(Category, verbose_name=u'分类')
    abstract = models.TextField(u'摘要')
    #created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(u'修改时间', auto_now=True)
    content = models.TextField(u'正文')
    click_count = models.IntegerField(u'点击量', default=0, editable=False)
    comment_count = models.IntegerField(u'评论数', default=0, editable=False)

    def __unicode__(self):
        return self.title

    def click(self):
        pass

    class Meta:
        db_table = 'dlog_article'
        verbose_name = u'文章'


class Comment(BaseModel):
    article = models.ForeignKey(Article)
    address = models.CharField(u'网址', max_length=20)
    email = models.EmailField(u'邮件')
    context = models.TextField(u'评论')