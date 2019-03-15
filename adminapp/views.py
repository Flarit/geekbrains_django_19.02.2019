from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from authapp.forms import ShopUserRegisterForm
from adminapp.forms import ShopUserAdminEditForm
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        user_form = ShopUserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse('admin_custom:users'))
    else:
        user_form = ShopUserRegisterForm()

    context = {'title': title, 'form': user_form}

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_update(request, pk):
    title = 'пользователи/редактирование'

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin_custom:user_update', args=[edit_user.pk]))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    context = {'title': title, 'form': edit_form}

    return render(request, 'adminapp/user_update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        user.delete()
        return HttpResponseRedirect(reverse('admin_custom:users'))

    context = {'user_to_delete': user}

    return render(request, 'adminapp/user_delete.html', context)


class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryListView, self).dispatch(*args, **kwargs)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryCreateView, self).dispatch(*args, **kwargs)


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin_custom:categories')


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_read(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_update(request, pk):
    pass


@user_passes_test(lambda u: u.is_superuser)
def product_delete(request, pk):
    pass
