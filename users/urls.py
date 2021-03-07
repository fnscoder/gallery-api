from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.views import UserModelViewSet, SignInAPIView, RegisterAPIView

router = SimpleRouter()

router.register('users', UserModelViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', SignInAPIView.as_view(), name='login'),
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
]
