from django.conf.urls import patterns, url
import views
urlpatterns = patterns('',
                       url(r'^$', views.index),
                       url(r'^index/$', views.index, name='dlog_index'),

                       url(r'^detail/(?P<article_id>\d+)/$', views.detail, name='dlog_detail'),

                       url(r'^currently/$', views.currently_comment, name='dlog_currently_comment'),

                       url(r'^tags/$', views.get_tags, name='dlog_tags'),
                       url(r'^tags/(?P<tag_id>\d+)/$', views.get_by_tag, name='dlog_get_by_tag'),

                       url(r'^about/$', views.about, name='dlog_about'),
                       )