from django.conf.urls import include, url
from rest_framework import routers

# Viewsets
from rest.viewsets import UserViewSet

router = routers.DefaultRouter(trailing_slash='optional')
router.register(r'users', UserViewSet)

urlpatterns = [
    url(
        r'^oauth/',
        include('oauth2_provider.urls', namespace='oauth2_provider')
    ),
    url(
    	r'^api-auth/',
    	include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^', include((router.urls, 'rest'), namespace='api')),
]
