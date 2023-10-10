# urls.py
# urls.py

from django.urls import path
from .views import (
    MobileListCreateView,
    MobileRetrieveUpdateDestroyView,
    PCArticleView,
    MobileArticleView,
    PCListCreateView,
    PCRetrieveUpdateDestroyView,
    ArticleListCreateView,
    ArticleRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('mobiles/', MobileListCreateView.as_view(), name='mobile-list-create'),
    path('mobiles/<int:pk>/', MobileRetrieveUpdateDestroyView.as_view(), name='mobile-retrieve-update-destroy'),
    
    path('pcs/', PCListCreateView.as_view(), name='pc-list-create'),
    path('pcs/<int:pk>/', PCRetrieveUpdateDestroyView.as_view(), name='pc-retrieve-update-destroy'),
    
    path('articles/', ArticleListCreateView.as_view(), name='article-list-create'),
    path('articles/<int:pk>/', ArticleRetrieveUpdateDestroyView.as_view(), name='article-retrieve-update-destroy'),
    path('articles2/pc/<int:article_id>/', PCArticleView.as_view({'get': 'retrieve'}), name='article-pc'),
    path('articles2/mobile/<int:article_id>/', MobileArticleView.as_view({'get': 'retrieve'}), name='article-mobile'),
]

