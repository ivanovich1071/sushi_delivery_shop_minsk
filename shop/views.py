from django.views.generic import ListView
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
