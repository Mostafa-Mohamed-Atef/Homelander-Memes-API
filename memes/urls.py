from django.urls import path
from .views import MemeViewSet, MemeDetailView 

urlpatterns = [
    path('', MemeViewSet.as_view(), name='memes'),
    path('<int:pk>/', MemeDetailView.as_view(), name='meme-detail'),
]