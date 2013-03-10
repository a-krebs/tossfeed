from django.contrib.syndication.views import Feed
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect
from feeds.models import Feed as FeedModel
from feeds.forms import CreateFeedForm

class TossFeed(Feed):
    """
    Show a feed from the feed_id url parameter.
    """

    def get_object(self, request, feed_id=-1):
        # TODO change this to get_object_or_404
        return FeedModel.objects.get(pk=feed_id)

    def title(self, obj):
        return obj.name

    def link(self, obj):
        return reverse('feed', args=(obj.id,))

    def description(self, obj):
        return 'TossFeed Feed {}'.format(self.title(obj))

    def items(self, obj):
        return obj.items.order_by('-date_posted')

    def item_title(self, item):
        return item.url

    def item_description(self, item):
        return item.url

    def item_link(self, item):
        return item.url

    def item_pubdate(self, item):
        return item.date_posted

class CreateFeed(FormView):
    """
    Create a new feed by filling out the form.
    """

    template_name = 'feeds/index.html'
    form_class = CreateFeedForm

    def form_valid(self, form):
        feed = form.create_feed()
        return redirect('feed', args=(feed.id,))
