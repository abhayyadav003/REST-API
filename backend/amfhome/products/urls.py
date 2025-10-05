from django.urls import path
from products import views

urlpatterns = [
   
    path('list/', views.product_list_view),
    path('create/', views.product_create_view),
    path('list/create/', views.product_list_create_view),


    path('detail/<int:pk>/', views.product_detail_view),
    path('update/<int:pk>/', views.product_update_view),
    path('delete/<int:pk>/', views.product_delete_view),


    # path('list/', views.product_mixin_view),
    # path('create/', views.product_mixin_view),
    # path('list/create/', views.product_mixin_view),

    # path('detail/<int:pk>/', views.product_mixin_view),
    # path('update/<int:pk>/', views.product_mixin_view),
    # path('delete/<int:pk>/', views.product_mixin_view),

]
