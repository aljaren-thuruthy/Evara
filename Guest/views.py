from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
# def Newuser(request):
#     placedata=tbl_place.objects.all()
#     districtdata=tbl_district.objects.all()
#     if request.method=="POST":
#         name=request.POST.get("txt_name")
#         gender=request.POST.get("txt_gender")
#         contact=request.POST.get("txt_contact")
#         email=request.POST.get("txt_email")
#         password=request.POST.get("txt_password")
#         place=tbl_place.objects.get(id=request.POST.get("sel_place"))
#         address=request.POST.get("txt_address")
#         photo=request.FILES.get("txt_photo")
#         ucount=tbl_newuser.objects.filter(newuser_email=email).count()
#         if ucount > 0:
#             return render( request, "Guest/Serviceprovider.html", {'msg': "Email already exists",'ucount':ucount} )
#         else:
#             tbl_newuser.objects.create(newuser_name=name,newuser_gender=gender,newuser_contact=contact,newuser_email=email,newuser_password=password,newuser_place=place,newuser_address=address,newuser_photo=photo)
#         return render(request,"Guest/Newuser.html",{'msg':"Data Inserted"})
#     else:
#         return render(request,"Guest/Newuser.html",{'districtdata':districtdata,'placedata':placedata})
    


def Newuser(request):
    placedata = tbl_place.objects.all()
    districtdata = tbl_district.objects.all()

    errors = {}
    data = {}

    if request.method == "POST":
        data['txt_name'] = request.POST.get("txt_name")
        data['txt_gender'] = request.POST.get("txt_gender")
        data['txt_contact'] = request.POST.get("txt_contact")
        data['txt_email'] = request.POST.get("txt_email")
        data['txt_address'] = request.POST.get("txt_address")
        data['sel_place'] = request.POST.get("sel_place")
        data['sel_district'] = request.POST.get("sel_district")
        password = request.POST.get("txt_password")
        cpassword = request.POST.get("txt_confirmpassword")
        place = request.POST.get("sel_place")
        photo = request.FILES.get("txt_photo")

        if tbl_newuser.objects.filter(newuser_email=data['txt_email']).exists():
            errors['email'] = "Email already exists"

        if password != cpassword:
            errors['cpassword'] = "Password does not match"

        if not data['txt_contact'] or not data['txt_contact'].isdigit() or len(data['txt_contact']) != 10:
            errors['contact'] = "Enter valid 10 digit number"

        if not place:
            errors['place'] = "Select place"

        if errors:
            return render(request, "Guest/Newuser.html", {
                'errors': errors,
                'data': data,
                'districtdata': districtdata,
                'placedata': placedata
            })

        place_obj = tbl_place.objects.get(id=place)

        tbl_newuser.objects.create(
            newuser_name=data['txt_name'],
            newuser_gender=data['txt_gender'],
            newuser_contact=data['txt_contact'],
            newuser_email=data['txt_email'],
            newuser_password=password,
            newuser_place=place_obj,
            newuser_address=data['txt_address'],
            newuser_photo=photo
        )

        return render(request, "Guest/Newuser.html", {
            'success': "Registered Successfully",
            'districtdata': districtdata,
            'placedata': placedata
        })

    return render(request, "Guest/Newuser.html", {
        'districtdata': districtdata,
        'placedata': placedata
    })
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
    


# def Serviceprovider(request):
#     providerdata=tbl_serviceprovider.objects.all()
#     placedata=tbl_place.objects.all()
#     servicedata=tbl_serviceprovidertype.objects.all()
#     districtdata=tbl_district.objects.all()
#     if request.method=="POST":
#         name=request.POST.get("txt_name")
#         email=request.POST.get("txt_email")
#         contact=request.POST.get("txt_contact")
#         address=request.POST.get("txt_address")
#         photo=request.FILES.get("txt_photo")
#         idproof=request.FILES.get("txt_idproof")
#         certificate=request.FILES.get("txt_certificate")
#         placee=tbl_place.objects.get(id=request.POST.get("sel_place"))
#         servicetype=tbl_serviceprovidertype.objects.get(id=request.POST.get("sel_service"))
#         password=request.POST.get("txt_password")
#         providercount=tbl_serviceprovider.objects.filter(serviceprovider_email=email).count()
#         if providercount > 0:
#             return render( request, "Guest/Serviceprovider.html", {'msg': "Email already exists",'providercount':providercount} )
#         else:
#             tbl_serviceprovider.objects.create(serviceprovider_name=name,serviceprovider_email=email,serviceprovider_contact=contact,serviceprovider_address=address,serviceprovider_photo=photo,serviceprovider_idproof=idproof,serviceprovider_certificate=certificate,place=placee,serviceprovidertype=servicetype,serviceprovider_password=password)
#             return render(request,"Guest/Serviceprovider.html",{'msg':"Sucessfully compeleted Registration"})
#     else:
#         return render(request,"Guest/Serviceprovider.html",{'providerdata':providerdata,'servicedata':servicedata,'placedata':placedata,'districtdata':districtdata}) 

def Serviceprovider(request):
    providerdata = tbl_serviceprovider.objects.all()
    placedata = tbl_place.objects.all()
    servicedata = tbl_serviceprovidertype.objects.all()
    districtdata = tbl_district.objects.all()

    if request.method == "POST":
        errors = {}
        old = request.POST

        name = request.POST.get("txt_name")
        email = request.POST.get("txt_email")
        contact = request.POST.get("txt_contact")
        address = request.POST.get("txt_address")
        photo = request.FILES.get("txt_photo")
        idproof = request.FILES.get("txt_idproof")
        certificate = request.FILES.get("txt_certificate")
        place_id = request.POST.get("sel_place")
        service_id = request.POST.get("sel_service")
        password = request.POST.get("txt_password")

        # Name validation
        name_parts = name.strip().split()
        if len(name_parts) < 2:
            errors['name'] = "Enter first and last name"
        elif not (name_parts[0][0].isupper() and name_parts[1][0].isupper()):
            errors['name'] = "First letters must be capital"

        # Contact validation
        if not (contact and contact.isdigit() and len(contact) == 10):
            errors['contact'] = "Enter 10 digit number"

        # Password validation
        special_chars = "@$!%*?&"
        has_special = False
        for i in password:
            if i in special_chars:
                has_special = True
                break

        if not password or len(password) < 6 or not has_special:
            errors['password'] = "Min 6 chars with 1 special char"

        # Email exists
        if tbl_serviceprovider.objects.filter(serviceprovider_email=email).exists():
            errors['email'] = "Email already exists"

        if errors:
            return render(request, "Guest/Serviceprovider.html", {
                'errors': errors,
                'old': old,
                'providerdata': providerdata,
                'servicedata': servicedata,
                'placedata': placedata,
                'districtdata': districtdata
            })

        placee = tbl_place.objects.get(id=place_id)
        servicetype = tbl_serviceprovidertype.objects.get(id=service_id)

        tbl_serviceprovider.objects.create(
            serviceprovider_name=name,
            serviceprovider_email=email,
            serviceprovider_contact=contact,
            serviceprovider_address=address,
            serviceprovider_photo=photo,
            serviceprovider_idproof=idproof,
            serviceprovider_certificate=certificate,
            place=placee,
            serviceprovidertype=servicetype,
            serviceprovider_password=password
        )

        # SUCCESS CASE
        return render(request, "Guest/Serviceprovider.html", {
            'msg': "Registration Successful.You will recieve a mail once you become verified .",
            'errors': {},
            'old': {},  # clears form
            'providerdata': providerdata,
            'servicedata': servicedata,
            'placedata': placedata,
            'districtdata': districtdata
        })

    else:
        return render(request, "Guest/Serviceprovider.html", {
            'providerdata': providerdata,
            'servicedata': servicedata,
            'placedata': placedata,
            'districtdata': districtdata
        })
    
def index(request):  
        return render(request,"Guest/index.html") 
    


import re

