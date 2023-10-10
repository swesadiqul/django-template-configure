from django.shortcuts import render, HttpResponse
from .models import Contact, Service
import datetime

# Create your views here.
content = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Eligendi quo incidunt dicta magni nobis. Voluptate sunt architecto minus iusto eveniet sit doloremque ducimus, voluptatem laudantium deserunt quia quibusdam, officia nulla in. Distinctio, eveniet. Sequi vel omnis, animi quam quibusdam ipsa debitis? Voluptatibus consequatur ipsum libero possimus neque quaerat qui nulla."

def home(request):
    contact_list = Contact.objects.all()
    nums = [
        {
            'id': 1,
            'firstname': 'Emil',
            'lastname': 'Refsnes',
            'phone': 5551234,
            'joined_date': datetime.date(2022, 1, 5)
        },
        {
            'id': 2,
            'firstname': 'Tobias',
            'lastname': 'Refsnes',
            'phone': 5557777,
            'joined_date': datetime.date(2021, 4, 1)
        },
        {
            'id': 3,
            'firstname': 'Linus',
            'lastname': 'Refsnes',
            'phone': 5554321,
            'joined_date': datetime.date(2021, 12, 24)
        },
        {
            'id': 4,
            'firstname': 'Lene',
            'lastname': 'Refsnes',
            'phone': 5551234,
            'joined_date': datetime.date(2021, 5, 1)
        },
        {
            'id': 5,
            'firstname': 'Stalikken',
            'lastname': 'Refsnes',
            'phone': 5559876,
            'joined_date': datetime.date(2022, 9, 29)
        }
    ]
    return render(request, 'index.html', {'student': contact_list, 'content': content, 'nums': nums})


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
    services = Service.objects.all()
    print(services)
    return render(request, 'chocolate/services.html', {'services': services})


def blogs(request):
    return render(request, 'chocolate/blogs.html')


def single_blog(request):
    return render(request, 'chocolate/single-blog.html', {'content': content})
