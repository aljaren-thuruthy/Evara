from django.urls import path
from Guest import views
app_name="Guest"

urlpatterns = [
    path('Newuser/',views.Newuser,name="Newuser"),
    path('Ajaxplace/',views.Ajaxplace,name="Ajaxplace"),
    path('Login/',views.Login ,name="Login"),
    path('NewSeller/',views.NewSeller ,name="NewSeller"),

    path('Serviceprovider/',views.Serviceprovider ,name="Serviceprovider"),
    path('index/',views.index ,name="index"),
    ]
