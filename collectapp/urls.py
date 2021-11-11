from django.urls import path
import collectapp.views as collectapp

app_name = 'collectapp'

urlpatterns = [
    path('<str:name>/', collectapp.collection, name='category'),
]