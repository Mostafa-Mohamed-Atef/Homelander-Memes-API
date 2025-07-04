from django.shortcuts import render
from rest_framework import generics
from .serializers import MemeSerializer
from .models import Memes
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class MemeViewSet(generics.ListCreateAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'type','season','episode','tags']
    ordering_fields = ['name','season','episode']
    search_fields = ['name','tags']

class MemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer