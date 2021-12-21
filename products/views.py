from django.shortcuts import render, get_object_or_404, redirect

from products.models import Product


def products(request):
    """
    목록 출력
    """
    product_list = Product.objects.order_by()
    context = {'product_list': product_list}
    return render(request, 'products/products_list.html', context)


def detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}
    return render(request, 'products/products_detail.html', context)
