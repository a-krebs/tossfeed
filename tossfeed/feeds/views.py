from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from feeds.models import Feed as FeedModel

class TossFeed(Feed):
    def get_object(self, request, feed_id=-1):
        return FeedModel.objects.get(pk=feed_id)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return reverse('feed', args=(obj.id,))

    def description(self, obj):
        return 'TossFeed'

    def items(self, obj):
        return obj.items.order_by('-date_posted')

    def item_title(self, item):
        return item.url

    def item_description(self, item):
        return item.url

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return item.url
