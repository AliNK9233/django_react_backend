from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.views import APIView
from .models import Product
from rest_framework import status, permissions
from rest_framework.decorators import api_view



from .serializer import UserSerializer,ProductSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):  # Use APIView here
    permission_classes = [AllowAny]

    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            # Generate tokens
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            })
        return Response({"detail": "Invalid credentials"}, status=400)

@api_view(['POST'])
def create_product(request):
    if request.method == 'POST':
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Add the user to the request data before saving the product
            request.data['user'] = request.user.id
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Authentication required"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def get_products(request):
    
        products = Product.objects.all()  
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    