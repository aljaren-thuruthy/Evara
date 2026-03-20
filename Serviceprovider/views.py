from django.shortcuts import render,redirect
from Admin.models import *
from Serviceprovider.models import *
from Guest.models import *
from User.models import *
from django.db.models import Avg
from django.views.decorators.cache import cache_control
# Create your views here.
#hi
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Serviceproviderhomepage(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    return render(request,"Serviceprovider/Serviceproviderhomepage.html",{'providerdata':providerdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Serviceproviderprofile(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    return render(request,"Serviceprovider/Serviceproviderprofile.html",{'providerdata':providerdata})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Serviceprovidereditprofile(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    if request.method=="POST":
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        contact=request.POST.get('txt_contact')
        address=request.POST.get('txt_address')
        photo=request.FILES.get('txt_photo')
        providerdata.serviceprovider_name=name
        providerdata.serviceprovider_email=email
        providerdata.serviceprovider_contact=contact
        providerdata.serviceprovider_address=address
        if photo:  
            providerdata.serviceprovider_photo_photo = photo
        providerdata.save()
        return render(request,"Serviceprovider/Serviceprovidereditprofile.html",{'msg':'Updated'})
    else:
        return render(request,"Serviceprovider/Serviceprovidereditprofile.html",{'providerdata':providerdata})
    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)    
def Providerchangepassword(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    dbpass=providerdata.serviceprovider_password
    if request.method=="POST":
        old=request.POST.get('txt_oldpassword')
        new=request.POST.get('txt_newpassword')
        confirm=request.POST.get('txt_repassword')
        if old==dbpass:
            if new==confirm:
                providerdata.serviceprovider_password=new
                providerdata.save()
                return render(request,"Serviceprovider/Providerchangepassword.html",{'msg':'Updated'})
            else:
                return render(request,"Serviceprovider/Providerchangepassword.html",{'msg':'Updated'})
        else:
            return render(request,"Serviceprovider/Providerchangepassword.html",{'providerdata':providerdata})
    return render(request,"Serviceprovider/Providerchangepassword.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Myservices(request):
    servicetypedata = tbl_serviceprovidertype.objects.all()
    servicedata = tbl_services.objects.all()
    myservicedata = tbl_providerservice.objects.all()

    if request.method == "POST":

        
        if request.POST.get("sel_servicetype"):
            stype_id = request.POST.get("sel_servicetype")
            servicedata = tbl_services.objects.filter(servicetype_id=stype_id)

       
        if request.POST.get("sel_service") and request.POST.get("txt_amount"):
            service_name = tbl_services.objects.get(id=request.POST.get("sel_service"))
            provideramount = request.POST.get("txt_amount")
            tbl_providerservice.objects.create( provider_amount=provideramount,  service_name=service_name,
                                                provider=tbl_serviceprovider.objects.get(id=request.session['seid'])  # ✅ IMPORTANT
)
            return render(request,"Serviceprovider/Myservices.html",{ 'msg': "Data inserted",'servicedata': servicedata,'servicetypedata': servicetypedata,'myservicedata': myservicedata }
            )

    return render(
        request,
        "Serviceprovider/Myservices.html",
        {
            'servicedata': servicedata,
            'servicetypedata': servicetypedata,
            'myservicedata': myservicedata
        }
    )

@cache_control(no_cache=True, must_revalidate=True, no_store=True) 
def deleteservice(request,deid):
    tbl_providerservice.objects.get(id=deid).delete()
    return redirect("Serviceprovider:Myservices")

    
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Workgallery(request):
    gallerydata = tbl_workgallery.objects.filter(serviceprovider_id=request.session['seid'])
    providerdata = tbl_serviceprovider.objects.get(id=request.session['seid'])

    editdata = None

    # 👉 GET edit data
    if 'eid' in request.GET:
        editdata = tbl_workgallery.objects.get(id=request.GET['eid'])

    if request.method == "POST":
        work_desc = request.POST.get("txt_desc")
        workphoto = request.FILES.get("txt_photo")
        edit_id = request.POST.get("edit_id")

        # 👉 UPDATE
        if edit_id:
            gallery = tbl_workgallery.objects.get(id=edit_id)
            gallery.work_description = work_desc

            if workphoto:  # only update photo if new uploaded
                gallery.work_photo = workphoto

            gallery.save()
            return render(request, "Serviceprovider/Workgallery.html", {
                'msg': "Data Updated",
                'gallerydata': gallerydata,
                'providerdata': providerdata
            })

        # 👉 INSERT
        else:
            tbl_workgallery.objects.create(
                work_description=work_desc,
                work_photo=workphoto,
                serviceprovider=providerdata
            )
            return render(request, "Serviceprovider/Workgallery.html", {
                'msg': "Data Inserted",
                'gallerydata': gallerydata,
                'providerdata': providerdata
            })

    return render(request, "Serviceprovider/Workgallery.html", {
        'gallerydata': gallerydata,
        'providerdata': providerdata,
        'editdata': editdata
    })

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def deletegallery(request,dgid):
    tbl_workgallery.objects.get(id=dgid).delete()
    return redirect("Serviceprovider:Workgallery")    



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Viewrequest(request):
    provider = tbl_serviceprovider.objects.get(id=request.session['seid'])

    requestdata = tbl_request.objects.filter(
        serviceprovider=provider,
        request_status=0
    )

    accreqdata = tbl_request.objects.filter(
        serviceprovider=provider,
        request_status__in=[1, 3, 4, 5]
    )

    rejreqdata = tbl_request.objects.filter(
        serviceprovider=provider,
        request_status=2
    )

    # ⭐ Attach rating to each completed request
    for req in accreqdata:
        rating_obj = tbl_rating.objects.filter(request=req).first()
        if rating_obj:
            req.work_rating = rating_obj.rating_data
            req.work_review = rating_obj.user_review
        else:
            req.work_rating = 0
            req.work_review = None

    return render(request, "Serviceprovider/Viewrequest.html", {
        'requestdata': requestdata,
        'accreqdata': accreqdata,
        'rejreqdata': rejreqdata,
        'ar': [1,2,3,4,5]
    })

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def accrequest(request,reid):
    data = tbl_request.objects.get(id=reid)
    data.request_status =1
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'accepted'})   

@cache_control(no_cache=True, must_revalidate=True, no_store=True)  
def rejrequest(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=2
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'rejected'}) 
   
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workstart(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=3
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'Work Started'}) 

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workend(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=4
    data.save()
    email=data.serviceprovider_email
    # send_mail(
    #     'Respected Sir/Madam ',#subject
    #     "\r Hope you are doing well"
    #     "\r Your work have been completed . "
    #     "\r If there are any queries you can reach out to us through the website."
    #     "\r  Thankyou for choosing us . 
    #     "\r "
    #     "\r @Evara" ,#body
    #     settings.EMAIL_HOST_USER,
    #     [email],
    # )
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'Work Ended'})     

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def set_amount(request, rid):
    requestdata = tbl_request.objects.get(id=rid)

    if request.FILES.get("request_bill"):
        requestdata.request_bill = request.FILES.get("request_bill")

    if request.method == "POST":
        amount = request.POST.get("txt_amount")
        requestdata.request_amount = amount
        requestdata.request_status = 4   
        requestdata.save()
        return redirect('Serviceprovider:Viewrequest')

    return render(request, "Serviceprovider/Payment.html", {'requestdata': requestdata})

                                                                                              


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Logout(request):
        request.session.flush()
        return redirect("Guest:Login")                                                                                              