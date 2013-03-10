from django.conf.urls import patterns, url
from feeds import views

urlpatterns = patterns('',
    url(r'^(?P<feed_id>\d+)/$', views.TossFeed(), name='feed'),
    url(r'^(?P<feed_id>\d+)/details$', views.FeedDetailView.as_view(), name='details'),
    url(r'^(?P<feed_id>\d+)/add$', views.TossFeed(), name='add'),
    url(r'^$', views.CreateFeed.as_view(), name='index'),
)
