from itertools import product
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
    def get_queryset(self):
        product = Product.objects.all()
        return product

    def get(self, request, *args, **kwargs):
        """Back to all products

        Args:
            request (request): It is the data delivered through a request
        Returns:
            Response: Returns the data of the products
        """ 

        try:
            id = request.query_params["id"]
            if id != None:
                product = Product.objects.get(id=id)
                serializer = ProductModelSerializer(product)
        except:
            products = self.get_queryset()
            serializer = ProductModelSerializer(products, many=True)


        
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

  

    def put(self, request):
        id = request.query_params["id"]
        
        product_object = Product.objects.get(id=id)
        
        data = request.data

        
        

        product_object.product_name = data["product_name"]
        product_object.price = data["price"]
        product_object.stock = data["stock"]
        product_object.description = data["description"]

        product_object.save()
        


        serializer = ProductModelSerializer(product_object)
        return Response(serializer.data)
      

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