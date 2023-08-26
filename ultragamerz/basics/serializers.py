from . import models
from rest_framework import serializers

class productSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    class Meta:
        model = models.product
        fields = ['name','price','description','image','sales','quantity','category']
