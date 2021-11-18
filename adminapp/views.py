from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminapp.forms import PlayerEditAdminForm, CategoryEditForm
from authapp.models import Player
from authapp.forms import PlayerRegisterForm

from mainapp.models import CollectionCategory


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    if request.method == 'POST':
        user_form = PlayerRegisterForm(request.POST, request.FILES)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_list'))
    else:
        user_form = PlayerRegisterForm()

    context = {
        'title': 'create user',
        'form': user_form
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_list(request):
    context = {
        'title': 'users',
        'users': Player.objects.all().order_by('-is_active', 'nickname')
    }
    return render(request, 'adminapp/user_list.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_edit(request, pk=None):
    current_user = Player.objects.get(pk=pk)
    if request.method == 'POST':
        user_form = PlayerEditAdminForm(request.POST, request.FILES, instance=current_user)

        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin:user_list'))
    else:
        user_form = PlayerEditAdminForm(instance=current_user)
    context = {
        'title': 'edit user',
        'form': user_form,
        'user': current_user
    }
    return render(request, 'adminapp/user_edit.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk=None):
    current_user = get_object_or_404(Player, pk=pk)

    if request.method == 'POST':
        if current_user.is_active:
            current_user.is_active = False
        else:
            current_user.is_active = True
        current_user.save()
        return HttpResponseRedirect(reverse('admin:user_list'))
    context = {
        'title': 'ban user',
        'user': current_user
    }
    return render(request, 'adminapp/user_ban.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_create(request):
    if request.method == 'POST':
        category_form = CategoryEditForm(request.POST, request.FILES)

        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_list'))
    else:
        category_form = CategoryEditForm()

    context = {
        'title': 'create category',
        'form': category_form
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_list(request):
    context = {
        'title': 'categories',
        'categories': CollectionCategory.objects.all()
    }
    return render(request, 'adminapp/category_list.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_edit(request, pk=None):
    category = CollectionCategory.objects.get(pk=pk)
    if request.method == 'POST':
        category_form = CategoryEditForm(request.POST, request.FILES, instance=category)

        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(reverse('admin:category_list'))
    else:
        category_form = CategoryEditForm(instance=category)
    context = {
        'title': 'edit category',
        'form': category_form,
        'category': category
    }
    return render(request, 'adminapp/category_edit.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def category_delete(request, pk=None):
    category = get_object_or_404(CollectionCategory, pk=pk)

    if request.method == 'POST':
        category.delete()
        return HttpResponseRedirect(reverse('admin:category_list'))
    context = {
        'title': 'delete category',
        'category': category
    }
    return render(request, 'adminapp/category_delete.html', context=context)


@user_passes_test(lambda u: u.is_superuser)
def champion_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def champion_list(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def champion_edit(request, pk=None):
    pass


@user_passes_test(lambda u: u.is_superuser)
def champion_delete(request, pk=None):
    pass


@user_passes_test(lambda u: u.is_superuser)
def skin_create(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def skin_list(request):
    pass


@user_passes_test(lambda u: u.is_superuser)
def skin_edit(request, pk=None):
    pass


@user_passes_test(lambda u: u.is_superuser)
def skin_delete(request, pk=None):
    pass