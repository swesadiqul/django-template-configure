from django.shortcuts import render, HttpResponse
from .models import Contact

# Create your views here.


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'chocolate/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ##save contact information
        contact = Contact(name=name, email=email, phone=phone, subject=subject, message=message)
        contact.save()

    return render(request, 'chocolate/contact.html')


def feedback(request):
    return render(request, 'chocolate/feedback.html')


def services(request):
    return render(request, 'chocolate/services.html')
