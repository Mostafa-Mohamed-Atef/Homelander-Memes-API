from django.shortcuts import render
from rest_framework import generics
from .serializers import MemeSerializer
from .models import Memes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS

class IsOwnerOrAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object or admin users to edit/delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the owner of the meme or admin users
        return obj.user == request.user or request.user.is_staff

class MemeViewSet(generics.ListCreateAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type','season','episode','tags']
    ordering_fields = ['name','season','episode']
    search_fields = ['name','tags']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]