from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import FavoritesViewSets


api_router = DefaultRouter()
api_router.register(r'favorite', FavoritesViewSets, 'favorite')

urlpatterns = [
    url(r'^v1/', include(api_router.urls))
]
