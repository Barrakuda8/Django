from django.urls import path
import storeapp.views as storeapp

app_name = 'storeapp'

urlpatterns = [
    path('', storeapp.store, name='index'),
    path('<str:name>/', storeapp.store, name='category'),
    path('champions/<str:role>/', storeapp.store, name='role_sort')
]