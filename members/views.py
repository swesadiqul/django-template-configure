from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'chocolate/about.html')

def contact(request):
    return render(request, 'chocolate/contact.html')

def feedback(request):
    return render(request, 'chocolate/feedback.html')

def services(request):
    return render(request, 'chocolate/services.html')