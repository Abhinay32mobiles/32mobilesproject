# views.py

from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Mobile, PC, Article
from .serializers import MobileSerializer, PCSerializer, ArticleSerializer

class MobileListCreateView(generics.ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class MobileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer

class PCListCreateView(generics.ListCreateAPIView):
    queryset = PC.objects.all()
    serializer_class = PCSerializer

class PCRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PC.objects.all()
    serializer_class = PCSerializer

class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class ArticleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class PCArticleView(viewsets.ViewSet):
    def retrieve(self, request, article_id=None):
        try:
            article = Article.objects.get(article_id=article_id)
            if isinstance(article.product, PC):
                pc_product = article.product
                pc_data = {
                    "processor": pc_product.processor,
                    "brand": pc_product.brand,
                    "screen_size": pc_product.screen_size,
                    "operating_system": pc_product.operating_system,
                    "weight": pc_product.weight,
                    "port": pc_product.ports,
                    "storage_capacity": pc_product.storage_capacity,
                    "RAM": pc_product.ram,
                    "buy_links":pc_product.buy_link
                }
                return Response(pc_data)
            else:
                return Response({"detail": "Article is not related to a PC product."}, status=404)
        except Article.DoesNotExist:
            return Response({"detail": "Article not found."}, status=404)
class MobileArticleView(viewsets.ViewSet):
    def retrieve(self, request, article_id=None):
        try:
            article = get_object_or_404(Article, article_id=article_id)
            if isinstance(article.product, Mobile):
                mobile_product = article.product
                mobile_data = {
                    "model_number": mobile_product.model_number,
                    "brand": mobile_product.brand,
                    "screen_size": mobile_product.screen_size,
                    "operating_system": mobile_product.operating_system,
                    "camera_resolution": mobile_product.camera_resolution,
                    "battery_capacity": mobile_product.battery_capacity,
                    "storage_capacity": mobile_product.storage_capacity,
                    "RAM": mobile_product.RAM,
                    "buy_links" : mobile_product.buy_link,
                }
                return Response(mobile_data)
            else:
                return Response({"detail": "Article is not related to a mobile phone product."}, status=404)
        except Article.DoesNotExist:
            return Response({"detail": "Article not found."}, status=404)
