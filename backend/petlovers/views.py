from itertools import product 
from itertools import product

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
)
#Import the models 
from petlovers.models import (
    Product,
    User,
)
#import the serializers
from petlovers.serializers import (
    ProductModelSerializer,
    UserModelSerializer,
)

class ProductAPIView(APIView):
    """View that lists all the products in the system
    
    * Only admin users are able to access this view.

    Args:
        APIView (APIView): Using the APIView class is pretty much the same as using a regular View class, as usual,
         the incoming request is dispatched to an appropriate handler method such as .get() or .post().

    Returns:
        Response: Returns the view of the product with the list of all the products in the system
    """
    def get_queryset(self):

        product = Product.objects.all() #product store all products 
        product = Product.objects.all()
        return product

    def get(self, request, *args, **kwargs):
        """Back to all products

        Args:
            request (request): Creates an HttpRequest object that contains metadata about the request. 
            Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.
        Returns:
            Response: Returns the data of the products
        """ 

        try:

            id = request.query_params["id"] #get the id of the product
            if id != None: #if id doesnt match with any id of the products then create a new product
            product = Product.objects.get(id=id)#save product by the id 
            serializer = ProductModelSerializer(product) # create the serializer for this product

            id = request.query_params["id"]
            if id != None:
                product = Product.objects.get(id=id)
                serializer = ProductModelSerializer(product)
        except:
            products = self.get_queryset()
            serializer = ProductModelSerializer(products, many=True)

        return Response(data=serializer.data, status=200)#send the reqsponse with all the data of the serializer, 
        #also with the status 200 what means OK

        
        return Response(data=serializer.data, status=200)
        
    def post(self, request):
        """ Send product information
        Args:
            self(self) : Rrepresents the instance of the class.
            request (request): Creates an HttpRequest object that contains metadata about the request. 
            Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.

        Returns:
            Responde: Return the data of the products      
        """
        serializer = ProductModelSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data #validate the data of the serializer
            new_product = Product.objects.create(**validated_data) #validate the data of the serializer
            data = ProductModelSerializer(new_product).data#save the data of the serializer in the validated_data
            return Response(data) #data is all the metadato sent in JSON format
        else:
            data = {'error': str(serializer.errors)}
            return Response(data)


    def put(self, request):
        """

        Args:
            request (_type_): Replaces the resource at the current URL with the resource contained within the request.

        Returns:
            Response: The product with all the metatada updated
        """        

        id = request.query_params["id"] #get the id of the product
        
        product_object = Product.objects.get(id=id)#compare the id of the product with the id of the request
        
        data = request.data  #store the data which will be updated

        #every data is replaced with the new one of the metadata of the request
        product_object.product_name = data["product_name"]
        product_object.price = data["price"]
        product_object.stock = data["stock"]
        product_object.description = data["description"]

        product_object.save()#save all the data updated


        serializer = ProductModelSerializer(product_object)
        return Response(serializer.data)

  

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
    """View that lists all the  users in the system
    
    * Only admin users are able to access this view.

    Args:
        APIView (APIView): Using the APIView class is pretty much the same as using a regular View class, as usual,
         the incoming request is dispatched to an appropriate handler method such as .get() or .post().

    Returns:
        Response: Returns the view of the userwith the list of all the users in the system
    """
    def get(self, request, *args, **kwargs):
        """Back to all user

        Args:
            request (request): Replaces the resource at the current URL with the resource contained within the request.

        Returns:
            Response:  Returns the data of the user
      
        """
        users = User.objects.all() #product store all products 
        serializer = UserModelSerializer(users,many=True)
        return Response(data=serializer.data, status=200)

    def post(self, request):
        """ Send user information
        Args:
            self(self) : Rrepresents the instance of the class.
            request (request): Creates an HttpRequest object that contains metadata about the request. 
            Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function.

        Returns:
            Responde: Return the data of the users      
        """
        serializer = UserModelSerializer(data=request.data)

        if serializer.is_valid():
        
            validated_data = serializer.validated_data#validate the data of the serializer
            new_user = User.objects.create(**validated_data)#validate the data of the serializer

            data = UserModelSerializer(new_user).data#save the data of the serializer in the validated_data
            return Response(data)#data is all the metadato sent in JSON format
        else:
            data = {'error': str(serializer.errors)}
            return Response(data)

