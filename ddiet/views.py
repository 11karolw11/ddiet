import datetime
from django.http import HttpResponse
from django.template import loader

from ddiet import forms
from ddiet import models
from ddiet import daytable

product = None
is_add = False
base_date = datetime.datetime.now().date()


def date_python_to_jquery(p_date):
    year, month, day = str(p_date).split('-')
    return month + '/' + day + '/' + year


def index(request):
    global base_date
    if request.method == 'POST' and "Cancel" not in request.POST: #add update product
        if is_add:
            f = forms.ProductForm(request.POST)
        else:
            f = forms.ProductForm(request.POST, instance=product)
        if f.is_valid():
            f.save()
        else:
            print(f.errors)
    if request.method == 'GET' and "date" in request.GET:
        month, day, year = request.GET['date'].split('/')
        base_date = (year + '-' + month + '-' + day)
    product_names = models.Product.objects.values('name')
    product_names = [row['name'] for row in product_names]
    day_products = daytable.DayTable(base_date).get_products()
    template = loader.get_template("ddiet/index.html")
    return HttpResponse(template.render({'products': product_names, 'day_products': day_products,
                                         'base_date': date_python_to_jquery(base_date)}, request))

def update_product(request):
    global is_add
    template = loader.get_template("ddiet/updateproduct.html")
    if 'ADD' in request.POST:
        product_form = forms.ProductForm()
        is_add = True
        return HttpResponse(template.render({'form': product_form}, request))
    elif 'product' in request.POST:
        global product
        is_add = False
        product = models.Product.objects.get(name=request.POST['product'])
        product_form = forms.ProductForm(instance=product)
        return HttpResponse(template.render({'form': product_form}, request))
