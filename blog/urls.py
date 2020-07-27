from django.urls import path
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('', ArticleListView.as_view(), name='index'),
    path('articles/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    # path('articles/<int:article_id>/', views.detail, name='detail'),
]

