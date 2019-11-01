from django.shortcuts import render
from .forms import ContactForm
from blog.models import Message

def home_view(request):
    return render(request, 'index.html')

def contact_view(request):
    form= ContactForm(request.POST or None)
    if form.is_valid():

        name=form.cleaned_data['name']
        email=form.cleaned_data['email']
        subject=form.cleaned_data['subject']
        message=form.cleaned_data['message']

        obj= Message.objects.filter(name=name, email=email, subject=subject, message=message)
        if obj.exists():
            pass
        else:
            obj= Message.objects.create(name=name, email=email, subject=subject, message=message)
            obj.save()
        form=ContactForm()
    context={'form':form}
    return render(request, 'contact.html', context)

def about_view(request):
    return render(request, 'about.html')
