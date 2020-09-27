from . import views
from django.urls import path
from .views import contactView, successView, resourceView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources_index, name='index'),
    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create/', resourceView, name='resources_create'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('resources/<int:resource_id>/', views.resources_detail,
         name='detail'),
    path('resources/<int:pk>/update/',
         views.ResourceUpdate.as_view(), name='resources_update'),
    path('resources/<int:pk>/delete/',
         views.ResourceDelete.as_view(), name='resources_delete'),
]
