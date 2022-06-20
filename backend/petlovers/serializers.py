from rest_framework import serializers
from petlovers.models import (
    User,
    Product,
)

class UserModelSerializer(serializers.ModelSerializer):
    """The user model is made
    """
    

    class Meta:
        model = User
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    """The Product model is made
    """
    class Meta:
        model = Product
        fields = '__all__'