# models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.postgres.fields import ArrayField
def default_buy_link():#utility function for   list of urls made it a callable to give it on 
    return [None, None, None]
class BaseProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    buy_link = models.URLField()
    # brand = models.TextField(default='Brand Name')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
class Mobile(BaseProduct):
    model_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=50)
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    operating_system = models.CharField(max_length=50)
    camera_resolution = models.CharField(max_length=20)
    battery_capacity = models.PositiveIntegerField()
    storage_capacity = models.PositiveIntegerField()
    RAM = models.PositiveIntegerField()
    articles = GenericRelation('Article')
    buy_link = ArrayField(
        models.URLField(max_length=200, blank=True, null=True),
        size=3,
        default=default_buy_link # Use the callable function as the default
    )
    

class PC(BaseProduct):
    processor = models.CharField(max_length=50)
    ram = models.PositiveIntegerField()
    storage_capacity = models.PositiveIntegerField()
    screen_size = models.DecimalField(max_digits=4, decimal_places=2)
    operating_system = models.CharField(max_length=50)
    graphics_card = models.CharField(max_length=50)
    ports = models.TextField()
    brand = models.CharField(max_length=50, default = 'brand name')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    articles = GenericRelation('Article')
    buy_link = ArrayField(
        models.URLField(max_length=200, blank=True, null=True),
        size=3,
        default=default_buy_link # Use the callable function as the default
    )

class Article(models.Model):
    article_id = models.BigAutoField(primary_key=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    updated_by = models.TextField(default='Author name')
    updated_time = models.DateTimeField(auto_now=True) 
    product = GenericForeignKey('content_type', 'object_id')
    category = models.TextField(default='Category')
    title = models.TextField(default='Title')
    description = models.TextField(default='Description')
   

    def __str__(self):
        return f"Article {self.article_id} - {self.product.name}"
