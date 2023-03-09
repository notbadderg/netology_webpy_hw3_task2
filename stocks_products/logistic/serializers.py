from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def validate(self, attrs):
        if not attrs:
            raise ValidationError('nothing provided for update')

        if attrs.get('address') and len(attrs['address']) < 3:
            raise ValidationError('too short address')

        if attrs.get('positions') == [] and len(attrs.get('positions', [])) < 1:
            raise ValidationError('no positions provided')

        return attrs

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for position in positions:
            StockProduct.objects.create(stock=stock, **position)

        return stock

    def update(self, instance, validated_data):
        if validated_data.get('positions'):
            positions = validated_data.pop('positions')
        else:
            positions = []

        stock = super().update(instance, validated_data)

        for position in positions:
            pop_data = position.pop('product')
            StockProduct.objects.update_or_create(
                stock=stock,
                product=pop_data,
                defaults=position
            )

        return stock
