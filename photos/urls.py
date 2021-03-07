from django.urls import path, include
from rest_framework.routers import SimpleRouter

from photos.views import PhotoModelViewSet, LikeModelViewSet

router = SimpleRouter()

router.register('photos', PhotoModelViewSet, 'photo')
router.register('likes', LikeModelViewSet, 'like')

urlpatterns = [
    path('', include(router.urls)),
]
