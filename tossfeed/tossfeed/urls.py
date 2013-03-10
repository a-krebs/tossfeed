from django.conf.urls import patterns, url
from feeds import views


urlpatterns = patterns('',
    url(r'^(?P<feed_id>\d+)/$', views.TossFeed(), name='feed'),
    url(r'^(?P<feed_id>\d+)/detail$', views.FeedDetailView.as_view(), name='detail'),
    url(r'^(?P<feed_id>\d+)/add$', views.AddToFeed.as_view(), name='add'),
    url(r'^$', views.CreateFeed.as_view(), name='index'),
)

# TODO: remove before deployment
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()