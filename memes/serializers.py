from rest_framework import serializers
from .models import Memes

class MemeSerializer(serializers.ModelSerializer): #module for serializing your model
    image = serializers.ImageField(max_length=None, use_url=True)
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Memes
        fields = "__all__"
