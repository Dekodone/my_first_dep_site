from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('people/', views.getAll, name='getAll'),
    path('people/person/<int:id>', views.getById, name='getById'),
    path('add/', views.add, name='add'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]