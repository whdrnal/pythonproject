
from django.urls import path

from products import views

app_name = 'products'

urlpatterns = [
    path('list/', views.products, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
]
