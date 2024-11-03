from rest_framework import serializers
from .models import RegisteredUser,MenuItem, Category, Order, Staff

class RegisteredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ['id', 'username', 'email', 'contact', 'password', 'role', 'role_id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta :
        model = Category
        fields = ['id', 'name']

class MenuItemWriteSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )  # Accept category ID for write operations 
    class Meta:
        model = MenuItem
        fields = '__all__'

class MenuItemReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  # Nested serializer for read operations
    class Meta:
        model = MenuItem
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):     
    class Meta:
        model = Order
        fields = [
            'id', 'customer_name', 'customer_phone', 'customer_email', 
            'customer_address', 'order_date', 'items_ordered', 
            'order_price', 'payment_mode', 'delivery_method', 
            'status', 'staff_id'
        ]                