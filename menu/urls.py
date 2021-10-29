from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_items, name='view_items'),
    path('<int:item_id>/', views.menu_item, name='menu_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),
]
