from django.db import models

class RegisteredUser(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    password = models.CharField(max_length=100)  # Store hashed passwords
    role = models.CharField(max_length=10, default='staff',choices=[('admin', 'Admin'), ('staff', 'Staff')])
    role_id = models.IntegerField(max_length=50,default='0')  # Store the ID based on role

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'registered_users'

class Category (models.Model) :
    name = models.CharField(max_length=100,unique=True) 

    def __str__(self):
        return self.name    
    class Meta:
        db_table = 'category'

class MenuItem (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image_url = models.URLField(max_length=200,blank=True,null=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)  
    available = models.BooleanField(default=True)  

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'menu_item'   

class Staff(models.Model) :
    name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
    class Meta :
        db_table = 'staff'

class Order(models.Model):
    # Customer details directly in the Order table
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    customer_email = models.EmailField()
    customer_address = models.TextField() 
    order_date = models.DateField() 
    items_ordered = models.TextField()  # Store items as a JSON array
    order_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the order
    payment_mode = models.CharField(max_length=50)  # Payment mode (e.g., Cash, Card)
    delivery_method = models.CharField(max_length=50)  # Delivery method (e.g., Pickup, Home delivery)
    status = models.CharField(max_length=50)  # Order status (e.g., Completed, Pending)
    staff_id = models.CharField(max_length=15)   
    
    def __str__(self):
        return f'Order {self.id} - {self.customer_name}'
    class Meta : 
        db_table = 'order_info' 
