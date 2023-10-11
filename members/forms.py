from django import forms
from .models import *


#create forms
class ContactForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    # email = forms.EmailField(null=True, blank=True)
    # phone = forms.CharField(max_length=100)
    # subject = forms.CharField(max_length=100)
    # message = forms.TextField()
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'subject', 'message')