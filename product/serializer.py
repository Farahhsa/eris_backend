from rest_framework import serializers
from product.models import Category, Item



class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']
class ItemSer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields="__all__"

class CategoryDetailSer(serializers.ModelSerializer):
    items = ItemSer(many=True     )
    class Meta:
        model = Category
        fields= ['id', 'name', 'items']
        