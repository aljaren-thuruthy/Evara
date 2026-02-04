from django.urls import path
from User import views


app_name="User"
urlpatterns = [
   
    path('Profile/',views.Profile ,name="Profile"),
    path('ChangePassword/',views.ChangePassword,name="ChangePassword"),
    path('EditProfile/',views.EditProfile,name="EditProfile"),
    path('Homepage/',views.Homepage,name="Homepage"),
    path('Complaint/',views.Complaint,name="Complaint"),
    path('SComplaint/<int:sid>',views.SComplaint,name="SComplaint"),
    path('delcomplaint/<int:did>',views.delcomplaint,name="delcomplaint"),
    path('Viewserviceprovider/',views.Viewserviceprovider,name="Viewserviceprovider"),
    path('Request/<int:id>',views.Request,name="Request"),
    path('Viewwork/<int:id>/', views.Viewwork, name="Viewwork"),
    path('Myrequest/', views.Myrequest, name="Myrequest"),
    path('Paymentview/<int:rid>', views.Paymentview, name="Paymentview"),
    path('Logout/', views.Logout, name="Logout"),
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
]