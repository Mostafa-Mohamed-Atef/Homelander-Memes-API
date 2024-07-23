from rest_framework import serializers
from .models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration','rating']
        
