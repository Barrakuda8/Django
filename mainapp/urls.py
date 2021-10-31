from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.collection, name='index'),
    path('<int:pk>/', mainapp.collection, name='category'),
]