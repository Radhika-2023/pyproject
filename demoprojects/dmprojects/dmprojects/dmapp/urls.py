from . import views
from django.urls import path

urlpatterns = [
    path('', views.dminmakes, name='dminmakes'),
    # path('calculate/', views.calculate, name='calculate')
    # path('calculate/', calculate_view, name='calculate'),
    # path('add/', views.addition, name="addition"),
    # path('mul/', views.multiplication, name="multiplication"),
    # path('div/', views.division, name="division"),
    # path('sub/', views.substraction, name="substraction")
]
