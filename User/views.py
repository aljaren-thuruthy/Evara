from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Guest.models import *
from Serviceprovider.models import *
from django.db.models import Sum
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Avg


# Create your views here.
def Profile(request):
        userdata=tbl_newuser.objects.get(id=request.session['uid'])
        return render(request,"User/Profile.html",{'userdata':userdata}) 


def ChangePassword(request):
    return render(request,"User/ChangePassword.html")

def EditProfile(request):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        contact=request.POST.get("txt_contact")
        address=request.POST.get("txt_address")
        userdata.newuser_name=name
        userdata.newuser_email=email
        userdata.newuser_contact=contact
        userdata.newuser_address=address
        userdata.save()
        return render(request,"User/EditProfile.html",{'msg':'updated'})
    else:    
        return render(request,"User/EditProfile.html",{'userdata':userdata})

def Homepage(request):
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    return render(request,"User/Homepage.html",{'userdata':userdata})    

def Complaint(request):
    complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])
    userdata=tbl_newuser.objects.get(id=request.session['uid'])
    if request.method=="POST":
        title=request.POST.get("txt_title")
        content=request.POST.get("txt_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata)
        return render(request,"User/Complaint.html",{'msg':'Complaint Registered'})
    else:
        return render(request,"User/Complaint.html",{'complaintdata':complaintdata})
    
def SComplaint(request, sid):
    complaintdata = tbl_complaint.objects.filter(user=request.session['uid'])
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    providerdata = tbl_serviceprovider.objects.get(id=sid)

    if request.method == "POST":
        title = request.POST.get("txt_title")
        content = request.POST.get("txt_content")
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userdata,serviceprovider=providerdata)
        return render(request, "User/Complaint.html", {'msg': 'Complaint Registered'})
    else:
        return render(request, "User/Complaint.html", {'complaintdata': complaintdata,'providerdata': providerdata})


def delcomplaint(request,did):
        tbl_complaint.objects.get(id=did).delete()
        return redirect("User:Complaint")

  

def Viewserviceprovider(request):
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    districtdata = tbl_district.objects.all()
    placedata = tbl_place.objects.all()
    servicedata = tbl_serviceprovidertype.objects.all()

    # Default show all active providers
    accservicedata = tbl_serviceprovider.objects.filter(serviceprovider_status=1)

    if request.method == "POST":
        district = request.POST.get("sel_district")
        place = request.POST.get("sel_place")
        service = request.POST.get("sel_service")

        if district:
            accservicedata = accservicedata.filter(place__district_id=district)

        if place:
            accservicedata = accservicedata.filter(place_id=place)

        if service:
            accservicedata = accservicedata.filter(serviceprovidertype_id=service)

    # ⭐ Average rating for each provider (IMPORTANT)
    for sp in accservicedata:
        avg_rating = tbl_rating.objects.filter(
            request__serviceprovider=sp
        ).aggregate(avg=Avg('rating_data'))['avg']

        if avg_rating is None:
            avg_rating = 0

        sp.avg_rating = round(avg_rating)

    return render(request, "User/Viewserviceprovider.html", {
        'userdata': userdata,
        'districtdata': districtdata,
        'placedata': placedata,
        'servicedata': servicedata,
        'accservicedata': accservicedata,
        'ar': [1, 2, 3, 4, 5]
    })

def Request(request, id):
    requestdata = tbl_request.objects.all()
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    servicedata = tbl_services.objects.all()
    providerdata = tbl_serviceprovider.objects.get(id=id)
    serviceprovidertype = tbl_serviceprovidertype.objects.all()  # ✅ ADD THIS

    if request.method == "POST":
        todate = request.POST.get("txt_todate")
        details = request.POST.get("txt_details")
        service = tbl_services.objects.get(id=request.POST.get("sel_service"))

        tbl_request.objects.create(
            request_todate=todate,
            request_details=details,
            service=service,
            serviceprovider=providerdata,
            user=userdata
        )

        return render(request, "User/Request.html", {
            'msg': "Data Inserted",
            'serviceprovidertype': serviceprovidertype  # ✅ ADD THIS
        })

    else:
        return render(request, "User/Request.html", {
            'requestdata': requestdata,
            'userdata': userdata,
            'servicedata': servicedata,
            'providerdata': providerdata,
            'serviceprovidertype': serviceprovidertype  # ✅ ADD THIS
        })


def Viewwork(request, id):
    providerdata = tbl_serviceprovider.objects.get(id=id)
    gallerydata = tbl_workgallery.objects.filter(serviceprovider=providerdata)

    return render(request, "User/Viewwork.html", {  'gallerydata': gallerydata, 'providerdata': providerdata })

def Myrequest(request):
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    requestdata = tbl_request.objects.filter(user=userdata)

    for r in requestdata:
        myrating = tbl_rating.objects.filter(user=userdata, request=r).first()
        print(myrating)
        if myrating:
            r.my_rating = myrating.rating_data
        else:
            r.my_rating = 0

    return render(request, "User/Myrequest.html", {
        'userdata': userdata,
        'requestdata': requestdata,
        'ar': [1,2,3,4,5]
    })


# def Paymentview(request, rid):
#     userdata = tbl_newuser.objects.get(id=request.session['uid'])
#     req = tbl_request.objects.get(id=rid)
#     profit_amount=tbl_profit.objects.all
#     profitcount=tbl_profit.objects.filter(request=rid,user=userdata)
#     if request.method == "POST":
#         profit_amount = req.request_amount * 0.10
#         req.request_status = 5
#         req.save()
#         return redirect('User:Myrequest')    
#     else:
#         return render(request,"User/Paymentview.html",{'requestdata': req,'profit_amount':profit_amount})



def Paymentview(request, rid):
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    req = tbl_request.objects.get(id=rid)

    profit_amount = req.request_amount * 0.10  # 10% profit

    # assuming tbl_request has a FK like: serviceprovider = ForeignKey(...)
    serviceprovider = req.serviceprovider

    if request.method == "POST":
        tbl_profit.objects.create(
            user=userdata,
            request=req,
            serviceprovider=serviceprovider,  # ✅ REQUIRED
            profit_amount=profit_amount
        )

        req.request_status = 5
        req.save()

        return redirect('User:Myrequest')

    return render(
        request,
        "User/Paymentview.html",
        {
            'requestdata': req,
            'profit_amount': profit_amount
        }
    )

def rating(request,mid,id):
    userdata = tbl_newuser.objects.get(id=request.session['uid'])
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    counts=0
    counts=stardata=tbl_rating.objects.filter(serviceprovider=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(serviceprovider=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'id':id,'data':stardata,'ar':parray,'avg':avg,'count':counts,'userdata':userdata})
    else:
         return render(request,"User/Rating.html",{'mid':mid,'id':id})

def ajaxstar(request):
    parray = [1, 2, 3, 4, 5]
    rating_data = request.GET.get('rating_data')
    user_review = request.GET.get('user_review')
    pid = request.GET.get('pid')        # This is probably serviceprovider id
    requestid = request.GET.get('requestid')
    
    tbl_rating.objects.create(
        user=tbl_newuser.objects.get(id=request.session['uid']),
        user_review=user_review,
        rating_data=rating_data,
        serviceprovider=tbl_serviceprovider.objects.get(id=pid),
        request=tbl_request.objects.get(id=requestid)
         # Add request object here
    )

    stardata = tbl_rating.objects.filter(serviceprovider=pid).order_by('-datetime')
    return render(request, "User/AjaxRating.html", {'data': stardata, 'ar': parray})


def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(serviceprovider=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(serviceprovider=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}


def Ajaxservice(request):
    servicetypeid = request.GET.get('stid')
    servicedata = tbl_services.objects.filter(servicetype=servicetypeid)
    return render(request, 'User/Ajaxservice.html', {'servicedata': servicedata})



def Logout(request):
       del request.session['uid']
       return redirect("Guest:Login")    





