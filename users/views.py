from rest_framework import viewsets, permissions, mixins
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from photos.models import Like
from photos.serializers import LikeSerializer
from users.models import User
from users.serializers import UserSerializer, RegisterSerializer, SignInSerializer


class UserModelViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def likes(self, request, pk=None):
        likes = Like.objects.filter(user=self.request.user)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)


class RegisterAPIView(CreateAPIView):
    """
    Register new user.
    """
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class SignInAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response(self.get_serializer(user).data)
