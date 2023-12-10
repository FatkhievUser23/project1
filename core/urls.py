from django.urls import path

from core import admin
from core.views import Homepage, info, Base, Products, OrderView, CategoriesView

urlpatterns = [
    path('', Base.as_view(), name = 'base'),
    path('home/', Homepage.as_view(), name = 'homepage'),
    path('info/', info.as_view(), name = 'info'),
    path('products/', Products.as_view(), name = 'products'),
    path('orders/', OrderView.as_view(), name='orders'),
    path('categories/', CategoriesView.as_view(), name='categories'),

]