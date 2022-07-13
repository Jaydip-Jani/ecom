from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('category/', views.CategoryView, name='category'),
    path('subcategory/', views.SubcategoryView, name='subcategory'),
    path('product/', views.ProductView, name='product'),
    path('edit/<int:id>/', views.EditProduct, name='edit'),
    path('del/<int:id>/', views.DelProduct, name='del'),
]
