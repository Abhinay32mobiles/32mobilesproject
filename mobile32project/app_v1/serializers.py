# serializers.py
from rest_framework import serializers
from .models import Mobile, PC, Article

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'

class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
