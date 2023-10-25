from rest_framework import serializers as ser
from .models import Product, Category


class ProductSerializer(ser.Serializer):
    title = ser.CharField(max_length=100)
    category = ser.PrimaryKeyRelatedField(queryset=Category.objects.all())
    price = ser.DecimalField(max_digits=12, decimal_places=2, default=1500)
    created_at = ser.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category = validated_data.get('category', instance.category)
        instance.price = validated_data.get('price', instance.price)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance



