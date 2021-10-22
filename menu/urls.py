from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='view_items'),
    path('<item_id>', views.menu_item, name='menu_item'),
]
