from django.urls import path
from .views import MenuItemListCreate, MenuItemDetail,CategoryListCreate,CategoryDetail,OrderList,OrderDetail,StaffListCreate,StaffDetail,RegisterView,UserDetailView,LoginView

urlpatterns = [
    # Register and Login endpoints
    path('register/', RegisterView.as_view(), name='register'),
    path('register/<int:role_id>/', UserDetailView.as_view(), name='user-by-role'),  # For users by role_id
    path('register/<int:role_id>/', UserDetailView.as_view(), name='user-detail-update'),
    path('login/', LoginView.as_view(), name='login'),
    # Menu Item endpoints
    path('menu-items/',MenuItemListCreate.as_view(),name='menu-items-list'),
    path('menu-items/<int:pk>/',MenuItemDetail.as_view(),name='menu-item-detail'),
    # Category endpoints
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),  
    # Order endpoints (Read-only)
    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'), 
    # Staff endpoints 
    path('staff/', StaffListCreate.as_view(), name='staff-list-create'),     
    path('staff/<int:pk>/', StaffDetail.as_view(), name='staff-detail'),   
]