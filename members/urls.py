from django.urls import path
from members import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('services/', views.services, name='service'),
    path('blogs/', views.blogs, name='blogs'),
    path('single-blog/', views.single_blog, name='single-blog'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('change-password/', views.change_password, name='change-password'),
]
