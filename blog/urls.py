from django.conf.urls import url
from . import views
from .feeds import PostsFeed

urlpatterns = [
    url(r'^$', views.post_list_view, name='post_list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view, name='post_detail_view'),
    url(r'^feed/$', PostsFeed(), name='post_feed')
]