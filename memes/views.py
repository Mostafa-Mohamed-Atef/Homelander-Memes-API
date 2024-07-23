from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemeSerializer
from .models import Memes
# Create your views here.

class MemeViewSet(viewsets.ModelViewSet):
    queryset = Memes.objects.all()
    serializer_class = MemeSerializer
    