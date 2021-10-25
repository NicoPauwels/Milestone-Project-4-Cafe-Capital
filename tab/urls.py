from django.urls import path
from . import views

urlpatterns = [
    path('add/<item_id>', views.add_to_tab, name='add_to_tab'),
    path('adjust/<item_id>/', views.adjust_tab, name='adjust_tab'),
    path('remove/<item_id>/', views.remove_from_tab, name='remove_from_tab'),
]