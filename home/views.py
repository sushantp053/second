from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    products  = Product.objects.all() # select * from Product
    context = {'prods': products}

    return render(request, 'home/home.html', context)

@login_required
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

@login_required
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
            user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            context = {'error': 'Username already exists', 'user': user}
            return render(request, 'auth/signup.html', context)
        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        # Redirect or render a template after signup
        return redirect('home')
    
    return render(request, 'auth/signup.html')

def signInUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = User.objects.filter(username=username, password=password).first() # This is not secure, use authenticate instead
        user = authenticate(request, username=username, password=password)
        print(username, password)
        print(user)
        if user:
            # User authenticated successfully
            login(request, user)
            return redirect('home')
        else:
            # Authentication failed
            context = {'error': 'Invalid username or password'}
            return render(request, 'auth/login.html', context)
    
    return render(request, 'auth/login.html')

def signOutUser(request):
    logout(request)
    return redirect('login_user')

def about(request): 
    return render(request, 'home/about.html')