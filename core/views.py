import views
from django.shortcuts import render
from django.views import View

from core.models import Product
from core.models import Order
from core.models import Category


class Base(View):
    def get(self, request):
        return render(request=request, template_name='core/base.html')
class Homepage(View):
    def get(self, request):
        return render(request=request, template_name='core/mainpage.html')

class info(View):
    def get(self, request):
        context = {'title': 'Информация о моем проекте'}
        return render(request=request, template_name='core/info.html')
class Products(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'core/products.html', {'products': products})

class OrderView(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'core/order.html', {'orders': orders})

class CategoriesView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'core/category.html', {'categories': categories})
