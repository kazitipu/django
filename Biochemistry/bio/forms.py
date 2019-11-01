from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required='required', widget=forms.TextInput(attrs= {'class':"form-control input-lg", 'placeholder':"Enter name"}))
    email = forms.CharField(required='required', widget=forms.EmailInput(attrs= {'class':"form-control input-lg", 'placeholder':"Enter email"}))
    subject = forms.CharField(required='required', widget=forms.TextInput(attrs= {'class':"form-control input-lg", 'placeholder':"Subject"}))
    message = forms.CharField(required='required', widget=forms.Textarea(attrs= {'class':"form-control", 'placeholder':"Message"}))