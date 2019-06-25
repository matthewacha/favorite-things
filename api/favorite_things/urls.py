from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import FavoritesViewSets
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='Favorite-Things API')
api_router = DefaultRouter()
api_router.register(r'favorite', FavoritesViewSets, 'favorite')

urlpatterns = [
    url(r'^docs/', schema_view),
    url(r'^v1/', include(api_router.urls))
]
