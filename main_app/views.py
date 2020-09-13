
from .forms import ContactForm  # Add this
from .forms import AddResourceForm # Add this
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Resource
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resources_index(request):
    resources = Resource.objects.all()
    return render(request, 'resources/index.html', {'resources': resources})

def resourceView(request):
    error_message = ''
    if request.method == 'POST':
        form = AddResourceForm(request.POST)
        if form.is_valid():
            print('form.is_valid')
            r = Resource(resource_name=form.cleaned_data['resource_name'],
                         org_name=form.cleaned_data['org_name'],
                         category=form.cleaned_data['category'],
                         hours=form.cleaned_data['hours'],
                         address=form.cleaned_data['address'],
                         street_number=form.cleaned_data['street_number'],
                         street_name=form.cleaned_data['street_name'],
                         city=form.cleaned_data['city'],
                         state=form.cleaned_data['state'],
                         country=form.cleaned_data['country'],
                         postal_code=form.cleaned_data['postal_code'],
                         long=form.cleaned_data['long'],
                         lat=form.cleaned_data['lat'],
                         phone=form.cleaned_data['phone'],
                         user=request.user,
                         url=form.cleaned_data['url'],
                         notes=form.cleaned_data['notes'])
            r.save()
            return redirect('index')
        else:
           print('!form.is_valid')
           print(form.errors)
           error_message = form.errors
    form = AddResourceForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'resources/create.html', context)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')
