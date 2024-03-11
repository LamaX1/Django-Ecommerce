from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login ,logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from .models import Item
from django.contrib.auth.decorators import login_required
from .cart import Cart

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

@csrf_exempt
def register_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,('You have registered successfully! Welcome'))
            return redirect('login')
        else:
            messages.error(request,('We ran into a problem, please try again...'))
            return redirect('register')
    else:
        context = {
        'registerForm': form
        }
        return render(request, 'register.html', context=context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
        else:
            messages.error(request,('Incorrect username or password, please try again.'))    
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,('You have been logged out!'))
    return redirect('index')

def view_cart(request):
    cart = Cart(request)
    cart_items = cart.get_items()
    return render(request,'cart.html',{'cartItems': cart_items})

@login_required(login_url='/login/')
def add_to_cart(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        item_id = int(request.POST.get('item_id'))
        item = get_object_or_404 (Item, id=item_id)
        cart.add(item=item)
        cart_qty = cart.__len__()
        response = JsonResponse({'qty:': cart_qty})
        return response
    else:
        return redirect('index')
    
