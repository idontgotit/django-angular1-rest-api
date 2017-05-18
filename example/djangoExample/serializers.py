from rest_framework import serializers

from .models import User, Post, Photo


class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.HyperlinkedIdentityField(view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(required=False, read_only=True)

    photos = serializers.HyperlinkedIdentityField(view_name='postphoto-list',required=False)

    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True)

    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    # def get_validation_exclusions(self, *args, **kwargs):
    #     # Need to exclude `user` since we'll add that later based off the request
    #     exclusions = super(PostSerializer, self).get_validation_exclusions(*args, **kwargs)
    #     return exclusions + ['author']

    class Meta:
        model = Post
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')

    class Meta:
        model = Photo
        fields = '__all__'