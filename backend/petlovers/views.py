from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
from petlovers.models import (
    Product,
    User,
)
from petlovers.serializers import (
    ProductModelSerializer,
    UserModelSerializer,
)



class ProductAPIView(APIView):
    """View that lists all the products in the system
    """

    def get(self, request, *args, **kwargs):
        """Back to all products
        """
        products = Product.objects.all()
        serializer = ProductModelSerializer(products,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        """Send product information
        """
        serializer = ProductModelSerializer(data=request.data)

        if serializer.is_valid():
            # Caso exitoso
            validated_data = serializer.validated_data
            new_product = Product.objects.create(**validated_data)

            
            data = ProductModelSerializer(new_product).data
            return Response(data)
        else:
            
            data = {'error': str(serializer.errors)}
            return Response(data)


    def patch(self, request):
        return Response(data="", status=200)
    

class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """Back to all user
        """
        users = User.objects.all()
        serializer = UserModelSerializer(users,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        """Send user information
        """
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
            # Caso exitoso
            validated_data = serializer.validated_data
            new_user = User.objects.create(**validated_data)

            data = UserModelSerializer(new_user).data
            return Response(data)
        else:
            data = {'error': str(serializer.errors)}
            return Response(data)

    def patch(self, request):
        return Response(data="", status=200)