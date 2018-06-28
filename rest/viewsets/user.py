from rest.models import User
from rest.serializers import UserSerializer
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    The UserViewSet class handles multirequest methods
    """
    queryset = User.objects.order_by('id')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return Super(UserViewSet, self).create(
            request, *args, **kwargs
        )

    def update(self, request, pk=None, *args, **kwargs):
        return super(UserViewSet, self)\
            .update(request, pk, *args, **kwargs)

