from django.views.generic import ListView
from django.shortcuts import render
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')
        if sort == 'price':
            queryset = queryset.order_by('price')
        elif sort == 'name':
            queryset = queryset.order_by('name')
        return queryset

def index(request):
    """Главная страница с популярными товарами"""
    popular_products = Product.objects.filter(popular=True).order_by('-price')[:5]  # Популярные товары
    context = {
        'popular_products': popular_products,
    }
    return render(request, 'shop/index.html', context)

def catalog(request):
    sort = request.GET.get('sort', '')  # Получаем параметр сортировки из GET-запроса
    products = Product.objects.all()

    if sort in ['price', '-price', 'name']:  # Проверяем, является ли параметр корректным
        products = products.order_by(sort)

    context = {
        'products': products,
    }
    return render(request, 'shop/catalog.html', context)

def login_view(request):
    """Страница входа"""
    return render(request, 'shop/login.html')

def register(request):
    """Страница регистрации"""
    return render(request, 'shop/register.html')
