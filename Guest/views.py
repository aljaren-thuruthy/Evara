from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
def Newuser(request):
    # newuserdata=tbl_newuser.objects.all()
    placedata=tbl_place.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        place=tbl_place.objects.get(id=request.POST.get("sel_place"))
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        ucount=tbl_newuser.objects.filter(newuser_email=email).count()
        if ucount > 0:
            return render( request, "Guest/Serviceprovider.html", {'msg': "Email already exists",'ucount':ucount} )
        else:
            tbl_newuser.objects.create(newuser_name=name,newuser_gender=gender,newuser_contact=contact,newuser_email=email,newuser_password=password,newuser_place=place,newuser_address=address,newuser_photo=photo)
        return render(request,"Guest/Newuser.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/Newuser.html",{'districtdata':districtdata,'placedata':placedata})

def Ajaxplace(request):
    districtid=request.GET.get('did')
    placedata=tbl_place.objects.filter(district=districtid)
    return render(request,'Guest/Ajaxplace.html',{'placedata':placedata})


def Login(request):
    if request.method=="POST":
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        usercount=tbl_newuser.objects.filter(newuser_email=email,newuser_password=password).count()
        admincount=tbl_adminreg.objects.filter(admin_email=email,admin_password=password).count()
        sellercount=tbl_seller.objects.filter(seller_email=email,seller_password=password).count()
        serviceprovidercount=tbl_serviceprovider.objects.filter(serviceprovider_email=email,serviceprovider_password=password).count()
        if usercount>0:
            userdata=tbl_newuser.objects.get(newuser_email=email,newuser_password=password)
            request.session['uid']=userdata.id
            return redirect("User:Homepage")
        elif admincount>0:
            admindata=tbl_adminreg.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect("Admin:Homepage")
        elif sellercount >0:
            sellerdata=tbl_seller.objects.get(seller_email=email,seller_password=password)
            request.session['sid']=sellerdata.id
            return redirect("Seller:SellerHomePage")    
        elif serviceprovidercount >0:
            providerdata=tbl_serviceprovider.objects.get(serviceprovider_email=email,serviceprovider_password=password)
            request.session['seid']=providerdata.id
            return redirect("Serviceprovider:Serviceproviderhomepage")   

        else:   
            return render(request,'Guest/Login.html',{'msg':'Invalid login'})
    else:        
            return render(request,"Guest/Login.html")



def NewSeller(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        contact=request.POST.get("txt_contact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
        establishdate=request.POST.get("txt_estdate")
        licenseno=request.POST.get("txt_licenseno") 
        owner=request.POST.get("txt_owner") 
        licenseproof=request.FILES.get("txt_licenseproof")
        ownerproof=request.FILES.get("txt_ownerproof")
        tbl_seller.objects.create(seller_name=name,seller_contact=contact,seller_email=email,seller_password=password,place=placee,seller_establishdate=establishdate,seller_licenseno=licenseno,seller_ownername=owner,seller_licenseproof=licenseproof, seller_ownerproof=ownerproof)
        return render(request,"Guest/NewSeller.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/NewSeller.html",{'districtdata':districtdata,'placedata':placedata})    
    


def Serviceprovider(request):
    providerdata=tbl_serviceprovider.objects.all()
    placedata=tbl_place.objects.all()
    servicedata=tbl_serviceprovidertype.objects.all()
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        photo=request.FILES.get("txt_photo")
        idproof=request.FILES.get("txt_idproof")
        placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
        servicetype=tbl_serviceprovidertype.objects.get(id=request.POST.get("sel_service"))
        password=request.POST.get("txt_password")
        providercount=tbl_serviceprovider.objects.filter(serviceprovider_email=email).count()
        if providercount > 0:
            return render( request, "Guest/Serviceprovider.html", {'msg': "Email already exists",'providercount':providercount} )
        else:
            tbl_serviceprovider.objects.create(serviceprovider_name=name,serviceprovider_email=email,serviceprovider_contact=contact,serviceprovider_address=address,serviceprovider_photo=photo,serviceprovider_idproof=idproof,place=placee,serviceprovidertype=servicetype,serviceprovider_password=password)
            return render(request,"Guest/Serviceprovider.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Guest/Serviceprovider.html",{'providerdata':providerdata,'servicedata':servicedata,'placedata':placedata,'districtdata':districtdata}) 

def index(request):  
        return render(request,"Guest/index.html") 
    