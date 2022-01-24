
from django.conf.urls import url
from rest_framework import routers
from .views import UserViewSet, RegisterView
from django.urls import path, include
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('rest-auth/register/', RegisterView.as_view())
]