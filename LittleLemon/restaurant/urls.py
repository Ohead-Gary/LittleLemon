from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.MenuItemView.as_view(), name='Menu'),
    path('menu/<int:pk>',views.SingleMenuItemView.as_view(), name='SingleMenuItem')
]