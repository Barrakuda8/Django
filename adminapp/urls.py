from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.user_create, name='user_create'),
    path('users/read/', adminapp.user_list, name='user_list'),
    path('users/update/<int:pk>/', adminapp.user_edit, name='user_edit'),
    path('users/delete/<int:pk>/', adminapp.user_delete, name='user_delete'),

    path('categories/create/', adminapp.category_create, name='category_create'),
    path('categories/read/', adminapp.category_list, name='category_list'),
    path('categories/update/<int:pk>/', adminapp.category_edit, name='category_edit'),
    path('categories/delete/<int:pk>/', adminapp.category_delete, name='category_delete'),

    path('champions/create/', adminapp.champion_create, name='champion_create'),
    path('champions/read/', adminapp.champion_list, name='champion_list'),
    path('champions/update/<int:pk>/', adminapp.champion_edit, name='champion_edit'),
    path('champions/delete/<int:pk>/', adminapp.champion_delete, name='champion_delete'),

    path('skins/create/', adminapp.skin_create, name='skin_create'),
    path('skins/read/', adminapp.skin_list, name='skin_list'),
    path('skins/update/<int:pk>/', adminapp.skin_edit, name='skin_edit'),
    path('skins/delete/<int:pk>/', adminapp.skin_delete, name='skin_delete')
]
