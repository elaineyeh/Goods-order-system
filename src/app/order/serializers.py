from rest_framework import serializers

from .models import Order, OrderGood


class OrderGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderGood
        fields = (
            'good',
            'amount'
        )


class OrderSerializer(serializers.ModelSerializer):
    goods = OrderGoodSerializer(many=True, source='ordergood_set')
    class Meta:
        model = Order
        fields = [
            'user',
            'goods'
        ]
