from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def index(request):
    return render(request, 'index.html')


def game(request):
    return render(request, 'game.html')


def catalog(request):
    categories = Category.objects.all()
    return render(request, 'catalog.html', {
        'categories': categories
    })


def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)

    products = Product.objects.filter(
        category=category,
        available=True
    )

    return render(request, 'category.html', {
        'category': category,
        'products': products
    })


def product_detail(request, slug):
    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    return render(request, 'product_detail.html', {
        'product': product
    })
