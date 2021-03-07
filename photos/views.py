import boto3
from botocore.config import Config
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from gallery.settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
from photos.models import Photo, Like, Comment
from photos.s3 import save_to_s3
from photos.serializers import PhotoSerializer, LikeSerializer

s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         config=Config(signature_version='s3v4'))


class PhotoModelViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Photo.objects.all()
        else:
            queryset = Photo.objects.filter(is_approved=True)
        return queryset

    def create(self, request, *args, **kwargs):
        photo = request.data.get('photo')
        if not photo:
            return Response('There is no photo to upload.', status=status.HTTP_400_BAD_REQUEST)
        photo_url = save_to_s3(photo)
        is_approved = True if self.request.user.is_staff else False
        photo = Photo.objects.create(photo_url=photo_url, owner=request.user, is_approved=is_approved)
        photo.save()
        serializer = PhotoSerializer(photo)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        if not self.request.user.is_staff:
            return Response('Sorry, you can\'t approve this photo.', status=status.HTTP_401_UNAUTHORIZED)
        photo = self.get_object()
        photo.is_approved = True
        photo.save()
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        photo = self.get_object()
        Like.objects.get_or_create(user=request.user, photo=photo)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        photo = self.get_object()
        comment = request.data.get('comment')
        Comment.objects.create(user=request.user, photo=photo, comment=comment)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def already_approved(self, request, pk=None):
        photos = Photo.objects.filter(is_approved=True)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def waiting_to_approve(self, request, pk=None):
        photos = Photo.objects.filter(is_approved=False)
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)
