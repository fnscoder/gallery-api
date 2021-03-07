from django.urls import path, include
from rest_framework.routers import SimpleRouter

from photos.views import PhotoModelViewSet

router = SimpleRouter()

router.register('photos', PhotoModelViewSet, 'photo')

urlpatterns = [
    path('', include(router.urls)),
]
