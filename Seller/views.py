from django.shortcuts import render
from Admin.models import *
from User.models import *
from Guest.models import *
# Create your views here.
def SellerHomePage(request):
    sellerdata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerHomePage.html",{'Data':sellerdata})
def SellerProfile(request):
    sellerprofiledata=tbl_seller.objects.get(id=request.session['sid'])
    return render(request,"Seller/SellerProfile.html",{'Data':sellerprofiledata})
def SellerChangePassword(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    dbpass=profiledata.seller_password
    if request.method=="POST":
        old=request.POST.get('txt_oldpassword')
        new=request.POST.get('txt_newpassword')
        confirm=request.POST.get('txt_repassword')
        if old==dbpass:
            if new==confirm:
                profiledata.seller_password=new
                profiledata.save()
                return render(request,"Seller/SellerChangePassword.html",{'msg':'Updated'})
            else:
                return render(request,"Seller/SellerChangePassword.html",{'msg':'Updated'})
        else:
            return render(request,"Seller/SellerChangePassword.html",{'Data':profiledata})
    return render(request,"Seller/SellerChangePassword.html")
def SellerEditProfile(request):
    profiledata=tbl_seller.objects.get(id=request.session['sid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        # licenseproof=request.POST.get('txt_licenseproof')
        # ownerproof=request.POST.get('txt_ownerproof')
        profiledata.seller_name=name
        profiledata.seller_email=email
        profiledata.seller_contact=contact
        profiledata.seller_establishdate=establishdate
        profiledata.seller_licenseno=licenseno
        profiledata.seller_ownername=ownername
        # profiledata.seller_licenseproof=licenseproof
        # profiledata.seller_ownerproof=ownerproof
        profiledata.save()
        return render(request,"Seller/SellerEditProfile.html",{'msg':'Updated'})
    else:
        return render(request,"Seller/SellerEditProfile.html",{'Data':profiledata})


