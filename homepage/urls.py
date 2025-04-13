from django.urls import path
from . import views

urlpatterns = [
    path('musical/', views.music_page, name='music_page'),
]
