from rest_framework import serializers

from app.good.models import Good

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = ('__all__')
