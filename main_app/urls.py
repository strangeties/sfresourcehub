from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('resources/', views.resources_index, name='index'),


    # path('myclothings/', views.myclothings_index, name='myindex'),
    # path('clothings/<int:clothing_id>/', views.clothings_detail,
    #      name='detail'),

    # path('shoes/<int:shoe_id>/', views.shoes_detail,
    #      name='shoes_detail'),


    path('accounts/signup/', views.signup, name='signup'),
    path('resources/create/',
         views.ResourceCreate.as_view(),
         name='resources_create'),
    # path('resources/<int:pk>/update/',
    #      views.ClothingUpdate.as_view(),
    #      name='clothings_update'),
    # path('clothings/<int:pk>/delete/',
    #      views.ClothingDelete.as_view(),
    #      name='clothings_delete'),
    # path('shoes/', views.ShoeList.as_view(), name='shoes_list'),

    #     path('shoes/<int:pk>', views.ShoeDetail.as_view(), name='shoes_detail'),


    # path('shoes/create/', views.ShoeCreate.as_view(), name='shoes_create'),
    # path('shoes/<int:pk>/update/',
    #      views.ShoeUpdate.as_view(),
    #      name='shoes_update'),
    # path('shoes/<int:pk>/delete/',
    #      views.ShoeDelete.as_view(),
    #      name='shoes_delete'),
    # path('clothings/<int:clothing_id>/add_photo/',
    #      views.add_clothing_photo, name='add_clothing_photo'),
    # path('shoes/<int:shoe_id>/add_photo/',
    #      views.add_shoe_photo, name='add_shoe_photo'),


    # path('clothings/<int:clothing_id>/assoc_shoe/<int:shoe_id>/',
    #      views.assoc_shoe, name='assoc_shoe'),


    # path('clothings/<int:clothing_id>/unassoc_shoe/<int:shoe_id>/',
    #      views.unassoc_shoe, name='unassoc_shoe'),


    # path('shoes/<int:shoe_id>/assoc_clothing/<int:clothing_id>/',
    #      views.assoc_clothing, name='assoc_clothing'),


    # path('shoes/<int:shoe_id>/unassoc_clothing/<int:clothing_id>/',
    #      views.unassoc_clothing, name='unassoc_clothing'),

]
