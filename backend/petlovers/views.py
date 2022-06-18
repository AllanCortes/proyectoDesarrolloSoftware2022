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

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductModelSerializer(products,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        serializer = ProductModelSerializer(data=request.data)

        if serializer.is_valid():
            # Caso exitoso
            validated_data = serializer.validated_data
            new_product = Product.objects.create(**validated_data)

            status_code = status.HTTP_200_OK
            data = ProductModelSerializer(new_product).data
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            data = {'error': str(serializer.errors)}


    def patch(self, request):
        return Response(data="", status=200)
    

class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserModelSerializer(users,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        pass

    def patch(self, request):
        return Response(data="", status=200)
        

