from .views import home, machines, products
from django.urls import path

urlpatterns = [
        path('',home, name="home_page"),
        path('products/', products,name='products'),
        path('machines/', machines,name='machines'),
        path('about/', machines,name='about'),
        path('read/', machines,name='read'),

]