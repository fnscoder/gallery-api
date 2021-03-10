from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.views import UserModelViewSet, SignInAPIView, RegisterAPIView, ProfileView

router = SimpleRouter()

router.register('users', UserModelViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('auth/login/', SignInAPIView.as_view(), name='login'),
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
]
