from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Resource
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import boto3
import uuid
S3_BASE_URL = 'https://s3.us-west-1.amazonaws.com/'
BUCKET = 'teamswapify'


# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resources_index(request):
    resources = Resource.objects.all()
    return render(request, 'resources/index.html', {'resources': resources})


# @login_required
# def myclothings_index(request):
#     myclothings = Clothing.objects.filter(user=request.user)
#     myshoes = Shoe.objects.filter(user=request.user)
#     return render(request, 'clothings/myindex.html', {
#         'myclothings': myclothings,
#         'myshoes': myshoes
#     })


# def clothings_detail(request, clothing_id):
#     clothing = Clothing.objects.get(id=clothing_id)
#     shoes_clothing_doesnt_have = Shoe.objects.exclude(
#         id__in=clothing.shoes.all().values_list('id'))
#     if not request.user.is_anonymous:
#         usershoes = Shoe.objects.filter(user=request.user).exclude(
#             id__in=clothing.shoes.all().values_list('id'))
#     else:
#         usershoes = []
#     return render(
#         request,
#         'clothings/detail.html',
#         {
#             # Pass the cat and feeding_form as context
#             'cloth': clothing,
#             # Add the toys to be displayed
#             'shoes': shoes_clothing_doesnt_have,
#             'usershoes': usershoes
#         })


# def shoes_detail(request, shoe_id):
#     shoe = Shoe.objects.get(id=shoe_id)
#     clothings_shoe_doesnt_have = Clothing.objects.exclude(
#         id__in=shoe.clothing_set.all().values_list('id'))
#     if not request.user.is_anonymous:
#         userclothes = Clothing.objects.filter(user=request.user).exclude(
#             id__in=shoe.clothing_set.all().values_list('id'))
#     else:
#         userclothes = []
#     return render(
#         request,
#         'main_app/shoe_detail.html',
#         {
#             # Pass the cat and feeding_form as context
#             'shoe': shoe,
#             # Add the toys to be displayed
#             'clothings': clothings_shoe_doesnt_have,
#             'userclothes': userclothes
#         })


class ResourceCreate(LoginRequiredMixin, CreateView):
    model = Resource
    fields = ['org_name', 'category', 'link', 'notes']

    def form_valid(self, form):
        # Assign the logged in user
        form.instance.user = self.request.user
        # Let the CreateView do its job as usual
        return super().form_valid(form)


# class ClothingUpdate(LoginRequiredMixin, UpdateView):
#     model = Clothing
#     fields = ['name', 'category', 'brand', 'description', 'size']


# class ClothingDelete(LoginRequiredMixin, DeleteView):
#     model = Clothing
#     success_url = '/clothings/'


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


# class ShoeList(ListView):
#     model = Shoe


# # class ShoeDetail(DetailView):
# #     model = Shoe


# class ShoeCreate(LoginRequiredMixin, CreateView):
#     model = Shoe
#     fields = ['name', 'brand', 'color', 'shoe_size', 'description']

#     def form_valid(self, form):
#         # Assign the logged in user
#         form.instance.user = self.request.user
#         # Let the CreateView do its job as usual
#         return super().form_valid(form)


# class ShoeUpdate(LoginRequiredMixin, UpdateView):
#     model = Shoe
#     fields = ['name', 'brand', 'color', 'description', 'shoe_size']


# class ShoeDelete(LoginRequiredMixin, DeleteView):
#     model = Shoe
#     success_url = '/shoes/'


# @login_required
# def add_clothing_photo(request, clothing_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + \
#             photo_file.name[photo_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             s3.upload_fileobj(photo_file, BUCKET, key)
#             # build the full url string
#             url = f"{S3_BASE_URL}{BUCKET}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             # photo = Clothing(url=url, clothing_id=clothing_id)
#             photo = Clothing.objects.get(id=clothing_id)
#             photo.url = url
#             photo.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('detail', clothing_id=clothing_id)


# @login_required
# def add_shoe_photo(request, shoe_id):
#     # photo-file will be the "name" attribute on the <input type="file">
#     photo_file = request.FILES.get('photo-file', None)
#     if photo_file:
#         s3 = boto3.client('s3')
#         # need a unique "key" for S3 / needs image file extension too
#         key = uuid.uuid4().hex[:6] + \
#             photo_file.name[photo_file.name.rfind('.'):]
#         # just in case something goes wrong
#         try:
#             s3.upload_fileobj(photo_file, BUCKET, key)
#             # build the full url string
#             url = f"{S3_BASE_URL}{BUCKET}/{key}"
#             # we can assign to cat_id or cat (if you have a cat object)
#             photo = Shoe.objects.get(pk=shoe_id)
#             photo.url = url
#             photo.save()
#         except:
#             print('An error occurred uploading file to S3')
#     return redirect('shoes_detail', shoe_id=shoe_id)

# # add association


# @login_required
# def assoc_shoe(request, clothing_id, shoe_id):
#     # Note that you can pass a toy's id instead of the whole object
#     Clothing.objects.get(id=clothing_id).shoes.add(shoe_id)
#     return redirect('detail', clothing_id=clothing_id)


# @login_required
# def assoc_clothing(request, shoe_id, clothing_id):
#     # Note that you can pass a toy's id instead of the whole object
#     Shoe.objects.get(id=shoe_id).clothing_set.add(clothing_id)
#     return redirect('shoes_detail', shoe_id=shoe_id)


# @login_required
# def unassoc_shoe(request, clothing_id, shoe_id):
#     Clothing.objects.get(id=clothing_id).shoes.remove(shoe_id)
#     return redirect('detail', clothing_id=clothing_id)


# @login_required
# def unassoc_clothing(request, shoe_id, clothing_id):
#     Shoe.objects.get(id=shoe_id).clothing_set.remove(clothing_id)
#     return redirect('shoes_detail', shoe_id=shoe_id)
