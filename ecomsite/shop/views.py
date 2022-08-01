from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    products=Product.objects.all()

    #search code
    search_content=request.GET.get('item_name')
    if search_content!='' and search_content!=None:
        products=products.filter(name__icontains=search_content)

    #paginator code
    paginator=Paginator(products,8)
    page=request.GET.get('page')
    products=paginator.get_page(page)

    return render(request,'shop/index.html',{'products':products})