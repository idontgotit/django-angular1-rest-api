from django.conf.urls import url, include
from rest_framework import routers

from djangoExample import views, api
from .api import UserList, UserDetail, AccountViewSet
from .api import PostList, PostDetail, UserPostList
from .api import PhotoList, PhotoDetail, PostPhotoList

user_urls = [
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/posts$', UserPostList.as_view(), name='userpost-list'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^$', UserList.as_view(), name='user-list')
]

post_urls = [
    url(r'^/(?P<pk>\d+)/photos$', PostPhotoList.as_view(), name='postphoto-list'),
    url(r'^/(?P<pk>\d+)$', PostDetail.as_view(), name='post-detail'),
    url(r'^$', PostList.as_view(), name='post-list')
]

photo_urls = [
    url(r'^/(?P<pk>\d+)$', PhotoDetail.as_view(), name='photo-detail'),
    url(r'^$', PhotoList.as_view(), name='photo-list')
]

router = routers.SimpleRouter()
router.register(r'register', AccountViewSet)

urlpatterns = [
    url(r'^users', include(user_urls)),
    url(r'^posts', include(post_urls)),
    url(r'^photos', include(photo_urls)),
    url(r'^login$', api.login),
    url(r'^', include(router.urls)),
    # url(r'^register', api.APIView.as_view()),
]

