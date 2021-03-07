from rest_framework import serializers

from photos.models import Comment, Like, Photo
from users.serializers import UserSerializer


class CommentSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)
    comment = serializers.CharField(required=False)

    def get_id(self, comment):
        return comment.id

    class Meta:
        model = Comment
        fields = '__all__'


class PhotoSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    owner = UserSerializer(read_only=True)
    photo_url = serializers.CharField(required=False)
    is_approved = serializers.BooleanField(read_only=True)
    likes = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, required=False)

    def get_likes(self, photo):
        return photo.likes.count()

    def get_id(self, photo):
        return photo.id

    class Meta:
        model = Photo
        fields = '__all__'


class PhotoCommentSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
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


class MyCommentSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    photo = PhotoCommentSerializer()
    comment = serializers.CharField(required=False)

    def get_id(self, comment):
        return comment.id

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    photo = PhotoSerializer()

    class Meta:
        model = Like
        fields = '__all__'
