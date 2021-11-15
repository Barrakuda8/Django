from django.urls import path
import collectapp.views as collectapp

app_name = 'collectapp'

urlpatterns = [
    path('<str:name>/', collectapp.collection, name='category'),
    path('<str:cat>/<int:pk>/', collectapp.product, name='product')
]