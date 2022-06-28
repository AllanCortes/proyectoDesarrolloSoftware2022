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
class HelloWorld(APIView):
    def get(self, request):

        return Response(data="Hello, World :c", status=200)


class ProductAPIView(APIView):
    """View that lists all the products in the system

    Args:
        APIView (APIView): 

    Returns:
        Response: Returns the view of the product
    """

    def get(self, request, *args, **kwargs):
        """Back to all products

        Args:
            request (request): It is the data delivered through a request
        Returns:
            Response: Returns the data of the products
        """ 
        products = Product.objects.all()
        serializer = ProductModelSerializer(products,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        """ Send product information
        Args:
            request (request):  It is the data delivered through a request

        Returns:
            Responde: Return the shipment of the products      
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

        Args:
            request (request): It is the data delivered through a request

        Returns:
            Response:  Returns the data of the user
      
        """
        users = User.objects.all()
        serializer = UserModelSerializer(users,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        """ Send user information
        Args:
            request (request):  It is the data delivered through a request

        Returns:
            Responde: Return the shipment of the users      
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