from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('registration', views.registration),
    path('login', views.login),
    path('dashboard', views.dashboard),
    path('wish_items/create', views.create_wish),
    path('wish_items', views.create_wish),
    path('wish_items/<wishlist_id>', views.view_wishlist),
    path('wish_items/<wishlist_id>/delete', views.delete),
    path('wish_items/<wishlist_id>/remove', views.remove),
    path('wish_items/<wishlist_id>/addto', views.add_to),
    path('logout', views.logout)



    
  
]