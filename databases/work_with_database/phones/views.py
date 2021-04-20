from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from phones.models import Phone


# В каталоге необходимо добавить возможность менять
# порядок отображения товаров:
# по названию (в алфавитном порядке) и по цене (по-убыванию и по-возрастанию).
def show_catalog(request):
    template = 'catalog.html'
    context = {}
    phones_catalog = Phone.objects.all()
    catalog = list(phones_catalog)
    # context = {'catalog': catalog}

    sort = request.GET.get('sort')
    if sort:
        if sort == 'name':
            sorted_by_name = sorted(catalog, key=lambda phone: phone.name)
            context = {'catalog': sorted_by_name}
        if sort == 'min_price':
            sorted_by_min_price = sorted(catalog, key=lambda phone: phone.price)
            context = {'catalog': sorted_by_min_price}
        if sort == 'max_price':
            sorted_by_max_price = sorted(catalog, key=lambda phone: phone.price, reverse=True)
            context = {'catalog': sorted_by_max_price}
    else:
        context = {'catalog': catalog}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    try:
        needed_phone = Phone.objects.get(slug=slug)
        context['phone'] = needed_phone
        return render(request, template, context)
    except ObjectDoesNotExist:
        return HttpResponse('<h1>Page was not found</h1>')


