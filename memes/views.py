from django.shortcuts import render
from rest_framework import generics
from .serializers import MemeSerializer
from .models import Memes
# Create your views here.

class MemeViewSet(generics.ListCreateAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer

class MemeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer