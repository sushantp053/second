from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def home(request):
    products  = Product.objects.all() # select * from Product
    context = {'prods': products}

    return render(request, 'home/home.html', context)

def addProduct(request):
    
    if request.method == 'POST':
        n = request.POST.get('name')
        p = request.POST.get('price')
        desc = request.POST.get('description')
        # image = request.FILES.get('image')
        print(n, p, desc)
        product = Product(name=n, price=p, description=desc)
        product.save()
    
    return render(request, 'home/addproduct.html')

def editProduct(request, id):

    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'home/editproduct.html', context)
    
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        # Update the product details

        n = request.POST.get('name')
        p = request.POST.get('price')
        desc = request.POST.get('description')
        # image = request.FILES.get('image')
        print(n, p, desc)
        product.name = n
        product.price = p
        product.description = desc
        product.save()
        return redirect('home')
    
    

