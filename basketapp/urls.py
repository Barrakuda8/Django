from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<str:cat>/<int:pk>/', basketapp.add, name='add'),
    path('remove/<str:cat>/<int:pk>/', basketapp.remove, name='remove')
]