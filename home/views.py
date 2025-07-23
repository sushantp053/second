from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User

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
    
def deleteProduct(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('home')
    
def signUpUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        # Here you would typically create a user object and save it
        print(username, password)
        if User.objects.filter(username=username).exists():
            return render(request, 'auth/signup.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        # Redirect or render a template after signup
        return redirect('home')
    
    return render(request, 'auth/signup.html')