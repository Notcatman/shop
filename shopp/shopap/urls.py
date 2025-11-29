from django.urls import path
from .views import crow, crow2, crow3, crow4

urlpatterns = [
    path("shop/", crow, name="home"),
    path('products/', crow2, name="products"),
    path('info/<int:product_id>/', crow3, name="product_detail"),
    path('cart/', crow4, name='cart')
]