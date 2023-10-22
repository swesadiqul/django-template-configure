from django.shortcuts import render, redirect
from .models import Contact, Service
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def home(request):
    contact_list = Contact.objects.all()
    return render(request, 'index.html', {'student': contact_list})


def about(request):
    return render(request, 'chocolate/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact.objects.create(name=name, email=email,
                                   phone=phone, subject=subject, message=message)
            messages.success(request, 'Successfully submitted!')
            return redirect('contact')

        else:
            messages.error(request, 'Invalid data.')
            return redirect('contact')

    return render(request, 'chocolate/contact.html')


def feedback(request):
    return render(request, 'chocolate/feedback.html')


def services(request):
    services = Service.objects.all()
    return render(request, 'chocolate/services.html', {'services': services})


def blogs(request):
    return render(request, 'chocolate/blogs.html')


def single_blog(request):
    return render(request, 'chocolate/single-blog.html')


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        username = request.POST.get('username')
        if not get_user_model().objects.filter(username=username).exists():
            if form.is_valid():
                user = form.save(commit=False)
                user.username = username.lower()
                user.save()
                login(request, user)
                messages.success(request, 'You have singed up successfully.')
                return redirect('home')

            else:
                messages.error(request, "Invalid form data.")
                return render(request, 'chocolate/signup.html')
        else:
            messages.error(request, "You have already an account.")
            return render(request, 'chocolate/signup.html')
    else:
        return render(request, 'chocolate/signup.html')


def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')
            else:
                messages.error(request, "You don't have any account.")
                return redirect('signup')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'chocolate/login.html')
    return render(request, 'chocolate/login.html')


def change_password(request):
    form = PasswordChangeForm(user=request.user)
    return render(request, 'chocolate/change_password.html', {'form': form})


def log_out(request):
    logout(request)
    messages.success(request, "User successfully logout.")
    return redirect('home')
