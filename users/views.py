import random

from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from concert.models import Basket
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        print('check')

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                print('all good')
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(form.errors)

    else:
        form = UserLoginForm()
        print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


def generate_code():
    random.seed()
    return str(random.randint(10000, 99999))


# Create your views here.
@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
    baskets = Basket.objects.filter(user=user)
    total_sum = sum(basket.sum() for basket in baskets)
    total_quantity = sum(basket.quantity_items_on_basket for basket in baskets)
    context = {
        'form': form,
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
