
from .forms import ContactForm  # Add this
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


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['resource_name', 'org_name', 'category', 'hours',
              'notes', 'street', 'city', 'state', 'phone', 'long', 'lat', 'url']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
            sender = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            recipent = ['sfresourcehub@gmail.com']
            try:
                send_mail(subject, message, sender,
                          recipent, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Success! Thank you for your message.')
    return render(request, "email.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


# def contact(request):
#     if request.method == "POST":
#         message_name = request.POST['message_name']
#         message_email = request.POST['message_email']
#         message = request.POST['message']

#         send_mail(
#             message_name,
#             message,
#             message_email,
#             ['sfresourcehub@gmail.com'],
#         )
#         return render(request, 'email.html', {'message_name': message_name})
#     else:
#         return render(request, 'email.html', {})

def resources_detail(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    return render(
        request,
        'resources/detail.html',
        {
            # Pass the cat and feeding_form as context
            'resource': resource
        })


class ResourceUpdate(LoginRequiredMixin, UpdateView):
    model = Resource
    fields = ['resource_name', 'org_name', 'category', 'hours',
              'notes', 'street', 'city', 'state', 'phone', 'long', 'lat', 'url']


class ResourceDelete(LoginRequiredMixin, DeleteView):
    model = Resource
    success_url = '/resources/'
