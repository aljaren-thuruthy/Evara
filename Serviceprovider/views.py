from django.shortcuts import render,redirect
from Admin.models import *
from Serviceprovider.models import *
from Guest.models import *
from User.models import *
# Create your views here.
#hi
def Serviceproviderhomepage(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    return render(request,"Serviceprovider/Serviceproviderhomepage.html",{'providerdata':providerdata})
def Serviceproviderprofile(request):
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    return render(request,"Serviceprovider/Serviceproviderprofile.html",{'providerdata':providerdata})
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
            tbl_providerservice.objects.create(
                provider_amount=provideramount,
                service_name=service_name
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

    
def deleteservice(request,deid):
    tbl_providerservice.objects.get(id=deid).delete()
    return redirect("Serviceprovider:Myservices")

def Workgallery(request):
    gallerydata = tbl_workgallery.objects.filter(serviceprovider_id=request.session['seid'])
    providerdata=tbl_serviceprovider.objects.get(id=request.session['seid'])
    if request.method=="POST":
        work_desc=request.POST.get("txt_desc")
        workphoto=request.FILES.get("txt_photo")
        tbl_workgallery.objects.create(work_description=work_desc,work_photo=workphoto,serviceprovider=providerdata)
        return render(request,"Serviceprovider/Workgallery.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Serviceprovider/Workgallery.html",{'gallerydata':gallerydata,'providerdata':providerdata})
    
def deletegallery(request,dgid):
    tbl_workgallery.objects.get(id=dgid).delete()
    return redirect("Serviceprovider:Workgallery")    

def Viewrequest(request):
    provider = tbl_serviceprovider.objects.get(id=request.session['seid'])
    requestdata = tbl_request.objects.filter(serviceprovider=provider, request_status=0)
    accreqdata = tbl_request.objects.filter(serviceprovider=provider,request_status__in=[1, 3, 4,5] )
    rejreqdata = tbl_request.objects.filter(serviceprovider=provider,request_status=2)
    return render(request, "Serviceprovider/Viewrequest.html", {'requestdata': requestdata,'accreqdata': accreqdata,'rejreqdata': rejreqdata})


def accrequest(request,reid):
    data = tbl_request.objects.get(id=reid)
    data.request_status =1
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'accepted'})   

    
def rejrequest(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=2
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'rejected'})    

def workstart(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=3
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'Work Started'}) 
def workend(request,reid):
    data=tbl_request.objects.get(id=reid)
    data.request_status=4
    data.save()
    return render(request,'Serviceprovider/Viewrequest.html',{'msg':'Work Ended'})     


def set_amount(request, rid):
    requestdata = tbl_request.objects.get(id=rid)

    if request.method == "POST":
        amount = request.POST.get("txt_amount")
        requestdata.request_amount = amount
        requestdata.request_status = 4   
        requestdata.save()
        return redirect('Serviceprovider:Viewrequest')

    return render(request, "Serviceprovider/Payment.html", {'requestdata': requestdata})

                                                                                              
def bill(request, rid):
    request_obj = tbl_request.objects.get(id=rid)

    if request.method == "POST":
        request_obj.request_bill = request.FILES['request_bill']
        request_obj.save()
        return redirect('Viewrequest')

    return render(
        request,
        "ServiceProvider/Bill.html",
        {'requestdata': request_obj}
    )


def Logout(request):
       del request.session['seid']
       return redirect("Guest:Login")                                                                                              