from django.urls import path
from apps.products.dashboard import views

urlpatterns = [
    #Products
    path('', views.ProductsView.as_view(), name="products" ),
    path('product-create/', views.ProductCreate.as_view(), name='productCreate'),
    path('product-detail/<slug:slug>/', views.ProductDetailView.as_view(), name="productDetail" ),
    path('product-update/<int:pk>/', views.ProductUpdate.as_view(), name="productUpdate"),
    path('product-delete/<int:pk>/', views.ProductDelete.as_view(), name='productDelete'),
    #Categories
    path('categories/', views.CategoryView.as_view(), name="categories"),
    path('category-create/', views.CategoryCreate.as_view(), name='categoryCreate'),
    path('category-detail/<slug:slug>/', views.CategoryDetailView.as_view(), name="categoryDetail" ),
    path('category-update/<int:pk>/', views.CategoryUpdate.as_view(), name="categoryUpdate"),
    path('category-delete/<int:pk>/', views.CategoryDelete.as_view(), name='categoryDelete'),
    #MeasureUnits
    path('meaure-units/', views.MeasureUnitView.as_view(), name="measureUnits"),
    path('unit-create/', views.MeasureUnitCreate.as_view(), name='meaureUnitCreate'),
    path('unit-detail/<int:pk>/', views.MeasureUnitDetailView.as_view(), name="meaureUnitDetail" ),
    path('unit-update/<int:pk>/', views.MeasureUnitUpdate.as_view(), name="meaureUnitUpdate"),
    path('unit-delete/<int:pk>/', views.MeasureUnitDelete.as_view(), name='meaureUnitDelete'),
    #Digital product
    path('digital_products/', views.ProductDigitalView.as_view(), name="productDigital"),
    path('digital-create/', views.ProductDigitalCreate.as_view(), name='productDigitalCreate'),
    path('digital-detail/<int:pk>/', views.DigitalDetailView.as_view(), name="productDigitalDetail" ),
    path('digital-update/<int:pk>/', views.ProductDigitalUpdate.as_view(), name="productDigitalUpdate"),
    path('digital-delete/<int:pk>/', views.ProductDigitalDelete.as_view(), name='productDigitalDelete'),
    #Stock
    path('stock/', views.StockView.as_view(), name="stock"),
    path('stock-create/', views.StockCreate.as_view(), name='stockCreate'),
    path('stock-detail/<int:pk>/', views.StockDetailView.as_view(), name="stockDetail" ),
    path('stock-update/<int:pk>/', views.StockUpdate.as_view(), name="stockUpdate"),
    path('stock-delete/<int:pk>/', views.StockDelete.as_view(), name='stockDelete'),

]
