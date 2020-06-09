from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:article_id>/', views.detail, name='detail'),
]

