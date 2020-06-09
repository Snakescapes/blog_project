from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.gallery_index, name='gallery_index'),
]