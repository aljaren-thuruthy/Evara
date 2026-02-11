from django.urls import path
from Serviceprovider import views
app_name= "Serviceprovider"
urlpatterns = [
    path('Serviceproviderhomepage/',views.Serviceproviderhomepage,name="Serviceproviderhomepage"),
    path('Serviceproviderprofile/',views.Serviceproviderprofile,name="Serviceproviderprofile"),
    path('Serviceprovidereditprofile/',views.Serviceprovidereditprofile,name="Serviceprovidereditprofile"),
    path('Providerchangepassword/',views.Providerchangepassword,name="Providerchangepassword"),
    path('Myservices/',views.Myservices,name="Myservices"),
    path('deleteservice/<int:deid>',views.deleteservice,name="deleteservice"),
    path('Workgallery/',views.Workgallery,name="Workgallery"),
    path('deletegallery/<int:dgid>',views.deletegallery,name="deletegallery"),
    path('Viewrequest/', views.Viewrequest, name="Viewrequest"),
    path('accrequest/<int:reid>', views.accrequest, name="accrequest"),
    path('rejrequest/<int:reid>', views.rejrequest, name="rejrequest"),
    path('workstart/<int:reid>', views.workstart, name="workstart"),
    path('workend/<int:reid>', views.workend, name="workend"),
    path('set_amount/<int:rid>', views.set_amount, name="set_amount"),
    path('bill/',views.bill,name="bill"),
    path('Logout/',views.Logout,name="Logout"),

]
