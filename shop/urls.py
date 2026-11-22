from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='catalog'),
    path('cakes/', views.cake_list, name='cakes'),
    path('cakes/<slug:slug>/', views.cake_detail, name='cake_detail'),
    path('desserts/', views.dessert_list, name='desserts'),
    path('desserts/<slug:slug>/', views.dessert_detail, name='dessert_detail'),
    path('drinks/', views.drink_list, name='drinks'),
    path('drinks/<slug:slug>/', views.drink_detail, name='drink_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('game/', views.game, name='game'),
]
