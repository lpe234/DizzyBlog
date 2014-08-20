#!coding=utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from models import Article, Comment, Tag
from CommentForm import CommentForm
# Create your views here.


# 文章默认主页，跟据创建时间倒序排列
def index(req):
    if req.method == 'POST':
        pass
    elif req.method == 'GET':
        # 文章列表
        article_list = Article.objects.order_by('-created_time')
        # 获取最新5条评论
        comments = Comment.objects.order_by('-created_time')[:5]
        # 获取所有标签
        tags = Tag.objects.all()
        context = {'article_list': article_list, 'comments': comments, 'tags': tags}
        return render_to_response('dlog/index.html', context)
    else:
        pass


# 获取文章详细信息，包含一个CommentForm表单
def detail(req, article_id):
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            email = form.cleaned_data['email']
            context = form.cleaned_data['context']
            article = Article.objects.get(pk=article_id)
            comment = Comment(article=article, name=name, address=address, email=email, context=context)
            comment.save()
            return HttpResponseRedirect('dlog/detail.html')
    else:
        form = CommentForm(initial={'name': '请输入姓名'})
    article = get_object_or_404(Article, pk=article_id)
    comments = article.comment_set.order_by('created_time')
    context = {'article': article, 'comments': comments, 'form': form}
    context.update(csrf(req))
    article.comment_count = article.comment_set.all().count()
    article.save()
    return render_to_response('dlog/detail.html', context)


# 获取最新评论。在Comment类中，根据创建时间倒序取5条数据。
def currently_comment(req):
    comments = Comment.objects.order_by('-created_time')[:5]
    context = {'comments': comments}
    return render_to_response('dlog/currently.html', context)


# 获取所有标签
def get_tags(req):
    tags = Tag.objects.all()
    context = {'tags': tags}
    return render_to_response('dlog/tags.html', context)


# 根据标签，获取该标签下的所有文章
def get_by_tag(req, tag_id):
    # article_list = Tag.objects.get(pk=tag_id).article_set.all()
    tag = get_object_or_404(Tag, pk=tag_id)
    article_list = tag.article_set.all()
    comments = Comment.objects.order_by('-created_time')[:5]
    tags = Tag.objects.all()
    context = {'article_list': article_list, 'comments': comments, 'tags': tags}
    return render_to_response('dlog/index.html', context)


def about(req):
    pass
    return HttpResponse('')