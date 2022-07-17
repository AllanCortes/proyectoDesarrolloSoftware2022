from rest_framework import serializers
from petlovers.models import (
    User,
    Product,
)

class UserModelSerializer(serializers.ModelSerializer):
    """User Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON
    """
    

    class Meta:
        model = User
        fields = '__all__'

class ProductModelSerializer(serializers.ModelSerializer):
    """Product Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON
    """
    class Meta:
        model = Product
        fields = '__all__'