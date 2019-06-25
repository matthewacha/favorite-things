from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSets


api_router = DefaultRouter()
api_router.register(r'user', CustomUserViewSets, 'user')

urlpatterns = [
    url(r'^v1/', include(api_router.urls))
]
