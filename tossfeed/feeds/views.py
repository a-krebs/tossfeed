import datetime

from django.contrib.syndication.views import Feed
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect

from feeds.models import Feed as FeedModel
from feeds.forms import CreateFeedForm, AddToFeedForm


class TossFeed(Feed):
    """
    Show a feed from the feed_id url parameter.
    """

    def get_object(self, request, feed_id=-1):
        feed = get_object_or_404(FeedModel, pk=feed_id)
        feed.views = feed.views + 1
        feed.date_last_viewed = datetime.datetime.now()
        feed.save()
        return feed

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

class FeedDetailView(DetailView):
    """
    Show details about the feed.
    """
    
    queryset = FeedModel.objects.all()
    pk_url_kwarg = 'feed_id'
    
    template_name = 'feeds/detail.html'

class AddToFeed(SingleObjectMixin, FormView):
    """
    Add a new item to the feed.
    """

    queryset = FeedModel.objects.all()
    pk_url_kwarg = 'feed_id'
    template_name = 'feeds/add.html'
    form_class = AddToFeedForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(AddToFeed, self).get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.date_last_posted = datetime.datetime.now()
        return super(AddToFeed, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        feed = self.object
        _ = form.add_to_feed(feed)
        return redirect('feed', feed.id)
