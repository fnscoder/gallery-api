from rest_framework import serializers

from photos.models import Photo
from users.serializers import UserSerializer


class PhotoSerializer(serializers.Serializer):
    owner = UserSerializer(read_only=True)
    photo_url = serializers.CharField(required=False)
    is_approved = serializers.BooleanField(read_only=True)

    class Meta:
        model = Photo
        fields = '__all__'
