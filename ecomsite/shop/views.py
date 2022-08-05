from django.shortcuts import render
from .models import Order, Product
from django.core.paginator import Paginator
import strgen
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView

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

def detail(request,id):
    product_object=Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})

class ProductDetail(DetailView):
    model=Product
    template_name='shop/detail.html'

@login_required
def checkout(request):
    if request.method=='POST':
        number=strgen.StringGenerator("[\w\d]{10}").render()
        items=request.POST.get('items','')
        total=request.POST.get('total','')
        first_name=request.POST.get('FirstName','')
        last_name=request.POST.get('LastName','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        address2=request.POST.get('address2','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zipcode=request.POST.get('zip','')
        order=Order(order=number, items=items,total=total,first_name=first_name,last_name=last_name,email=email,address=address,
        address2=address2,city=city,state=state,zipcode=zipcode)
        order.save()
    return render(request,'shop/checkout.html')