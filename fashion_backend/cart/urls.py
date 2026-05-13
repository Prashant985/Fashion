from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.GetUserCart.as_view(), name='get-user-cart'),
    path('add/', views.AddItemsToCart.as_view(), name='add-to-cart'),
    path('count/', views.AddItemsToCart.as_view(), name='add-to-cart'),
    path('delete/', views.RemoveItemsFromCart.as_view(), name='delete'),
    path('update/', views.UpdateCartItemQuantity.as_view(), name='update-count'),
]