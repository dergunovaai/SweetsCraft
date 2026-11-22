from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import Http404
from django.shortcuts import redirect, render

from .catalog import CAKES, CAKE_BY_SLUG
from .menu import DESSERTS, DESSERT_BY_SLUG, DRINKS, DRINK_BY_SLUG


def index(request):
    return render(request, 'index.html', {'cakes': CAKES})


def catalog(request):
    return render(
        request,
        'catalog.html',
        {
            'cake_count': len(CAKES),
            'dessert_count': len(DESSERTS),
            'drink_count': len(DRINKS),
        },
    )


def cake_list(request):
    return render(
        request,
        'category.html',
        {
            'title': 'Торты',
            'eyebrow': 'Каталог / Торты',
            'products': CAKES,
            'detail_url': 'cake_detail',
            'back_label': 'Вернуться к разделам',
        },
    )


def dessert_list(request):
    return render(
        request,
        'category.html',
        {
            'title': 'Десерты',
            'eyebrow': 'Каталог / Десерты',
            'products': DESSERTS,
            'detail_url': 'dessert_detail',
            'back_label': 'Вернуться к разделам',
        },
    )


def drink_list(request):
    return render(
        request,
        'category.html',
        {
            'title': 'Напитки',
            'eyebrow': 'Каталог / Напитки',
            'products': DRINKS,
            'detail_url': 'drink_detail',
            'back_label': 'Вернуться к разделам',
        },
    )


def _render_product_detail(request, product, detail_kind):
    if product is None:
        raise Http404('Товар не найден')
    return render(request, 'cake_detail.html', {'cake': product, 'detail_kind': detail_kind})


def cake_detail(request, slug):
    return _render_product_detail(request, CAKE_BY_SLUG.get(slug), 'cake')


def dessert_detail(request, slug):
    return _render_product_detail(request, DESSERT_BY_SLUG.get(slug), 'dessert')


def drink_detail(request, slug):
    return _render_product_detail(request, DRINK_BY_SLUG.get(slug), 'drink')


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        auth_login(request, form.get_user())
        return redirect('index')
    return render(request, 'auth/login.html', {'form': form})


def register_view(request):
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        auth_login(request, user)
        return redirect('index')
    return render(request, 'auth/register.html', {'form': form})


def logout_view(request):
    auth_logout(request)
    return redirect('index')


def game(request):
    return render(request, 'game.html')
