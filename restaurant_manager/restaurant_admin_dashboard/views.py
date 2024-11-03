from django.shortcuts import get_object_or_404
from django.db import models
from rest_framework import generics 
from rest_framework.views import APIView  # Base class for creating API views.
from rest_framework.response import Response  # To send JSON responses.
from rest_framework import status  # HTTP status codes (e.g., 201, 400, 404).
from django.contrib.auth.hashers import make_password, check_password  # For hashing and verifying passwords.

from .models import MenuItem, Category,Order,Staff,RegisteredUser
from .serializers import MenuItemWriteSerializer, MenuItemReadSerializer,CategorySerializer,StaffSerializer,OrderSerializer,RegisteredUserSerializer

#This view handles user registration. When a user sends data (username, email, password, etc.), it stores it in the database.
class RegisterView(APIView):
    def post(self,request):
        data = request.data  # Get the user data from the request body.
        data['password'] = make_password(data['password'])  # Hash the password.
        serializer = RegisteredUserSerializer(data=data)  # Serialize the data.
        if serializer.is_valid():  # Check if data is valid.
            serializer.save()  # Save the user to the database.
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Handle validation errors.

class UserDetailView(APIView):
    def get(self, request, role_id=None):
        # If a specific role_id is provided, filter users by role_id
        if role_id is not None:
            users = RegisteredUser.objects.filter(role_id=role_id)  # Fetch users with the given role_id
            if not users.exists():
                return Response({"detail": "No users found with this role id."}, status=status.HTTP_404_NOT_FOUND)
        else:
            # If no role_id, return all registered users
            users = RegisteredUser.objects.all()  # Adjust query as needed

        serializer = RegisteredUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, role_id=None):
        if role_id is None:
            return Response({"detail": "Role ID is required for update."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = RegisteredUser.objects.get(role_id=role_id)
        except RegisteredUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        if 'password' in data:
            data['password'] = make_password(data['password'])

        serializer = RegisteredUserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User updated successfully!"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#This view handles user login. It verifies the username and password, and if valid, logs the user in.
class LoginView(APIView):
    def post(self, request):
        identifier = request.data.get('identifier')  # Username or email from the request.
        password = request.data.get('password')  # Password from the request.
        try:
            # Try finding user by username or email
            user = RegisteredUser.objects.get(models.Q(username=identifier) | models.Q(email=identifier))
            # Verify the password
            if check_password(password, user.password):
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid password!"}, status=status.HTTP_400_BAD_REQUEST)
        except RegisteredUser.DoesNotExist:
            return Response({"error": "User not found!"}, status=status.HTTP_404_NOT_FOUND)

# View to list and create menu items
class MenuItemListCreate (generics.ListCreateAPIView) :
    queryset = MenuItem.objects.all()         # Fetch all menu items
    def get_serializer_class(self):
        # Use different serializers for read (GET) and write (POST)
        if self.request.method == 'POST':
            return MenuItemWriteSerializer
        return MenuItemReadSerializer
    
# View to retrieve, update, or delete specific menu items    
class MenuItemDetail (generics.RetrieveUpdateDestroyAPIView) :
    queryset = MenuItem.objects.all()         # Fetch all menu items
    def get_serializer_class(self):
        # Use different serializers for read (GET) and write (PUT/PATCH)
        if self.request.method in ['PUT', 'PATCH']:
            return MenuItemWriteSerializer
        return MenuItemReadSerializer   
    
# View to list and create categories
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('id') 
    serializer_class = CategorySerializer    

# View to retrieve, update, or delete a specific category
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer   

# Read-only view to list and retrieve orders
class OrderList(generics.ListAPIView):
    queryset = Order.objects.all().order_by('id')  # Sorted by order date
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# View to list and create staffs
class StaffListCreate(generics.ListCreateAPIView): 
    queryset = Staff.objects.all().order_by('id')  
    serializer_class = StaffSerializer   

# View to retrieve, update, or delete staff 
class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()   
    serializer_class = StaffSerializer      