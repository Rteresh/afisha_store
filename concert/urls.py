from django.urls import path
from concert.views import basket_add, concerts, basket_delete, search

app_name = 'concerts'

urlpatterns = [
    path('', concerts, name='index'),
    path('page/<int:page>', concerts, name='page'),
    path('basket-add/<int:concert_id>', basket_add, name='basket_add'),
    path('basket-delete/<int:basket_id>', basket_delete, name='basket_delete'),
    #
]
