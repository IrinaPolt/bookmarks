from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BookmarkViewSet, CollectionViewSet

app_name = 'api'

router = DefaultRouter()

router.register(r'bookmarks', BookmarkViewSet, basename='bookmarks')
router.register(r'collections', CollectionViewSet, basename='collection')


urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('djoser.urls')),
    path('', include(router.urls)),
]
