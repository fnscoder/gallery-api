from rest_framework import serializers

from photos.models import Photo, Like
from users.serializers import UserSerializer


class PhotoSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    owner = UserSerializer(read_only=True)
    photo_url = serializers.CharField(required=False)
    is_approved = serializers.BooleanField(read_only=True)
    likes = serializers.SerializerMethodField()

    def get_likes(self, photo):
        return photo.likes.count()

    def get_id(self, photo):
        return photo.id

    class Meta:
        model = Photo
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    photo = PhotoSerializer()

    class Meta:
        model = Like
        fields = '__all__'
