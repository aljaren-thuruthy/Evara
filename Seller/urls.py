from django.urls import path
from Seller import views
app_name= "Seller"
urlpatterns = [
    path('SellerHomePage/',views.SellerHomePage ,name="SellerHomePage"),
    path('SellerProfile/',views.SellerProfile ,name="SellerProfile"),
    path('SellerEditProfile/',views.SellerEditProfile ,name="SellerEditProfile"),
    path('SellerChangePassword/',views.SellerChangePassword ,name="SellerChangePassword"),
]