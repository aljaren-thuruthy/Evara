from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from django.db.models import Count , Sum
from django.utils import timezone
from datetime import date
from django.conf import settings
from django.core.mail import send_mail



def District(request):
    districtdata = tbl_district.objects.all()
    if request.method == "POST":
        district = request.POST.get("txt_district")
        districtcount=tbl_district.objects.filter(district_name=district).count()
        if districtcount > 0:
            return render( request, "Admin/District.html", {'msg': "District already exists",'districtdata': districtdata } )
        tbl_district.objects.create(district_name=district)
        return render( request,"Admin/District.html", {'msg': "Data inserted",'districtdata': districtdata } )
    else:
        return render( request, "Admin/District.html", {'districtdata': districtdata})


def Category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get("txt_category")
        tbl_category.objects.create(category_name=category)
        return render(request,"Admin/Category.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Category.html",{'categorydata':categorydata})  

def AdminRegistration(request):
    adminregdata=tbl_adminreg.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        admincount=tbl_adminreg.objects.filter(admin_email=email).count()
        if admincount > 0:
            return render( request, "Admin/AdminRegistration.html", {'msg': "Email already exists"} )
        else:
            return render(request,"Admin/AdminRegistration.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/AdminRegistration.html",{'adminregdata':adminregdata}) 

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:District")

def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("Admin:Category")    

def deladminreg(request,aid):
    tbl_adminreg.objects.get(id=aid).delete()
    return redirect("Admin:AdminRegistration")    

def editdistrict(request,did):
      editdata=tbl_district.objects.get(id=did)
      if request.method=="POST":
        district=request.POST.get("txt_district")
        editdata.district_name=district
        editdata.save()
        return redirect("Admin:District")
      else:  
       return render(request,"Admin/District.html",{'editdata':editdata}) 

def editcategory(request,cid):
      editdata=tbl_category.objects.get(id=cid)
      if request.method=="POST":
        category=request.POST.get("txt_category")
        editdata.category_name=category
        editdata.save()
        return redirect("Admin:Category")
      else:  
       return render(request,"Admin/Category.html",{'editdata':editdata}) 

def editadmin(request,aid):
      editdata=tbl_adminreg.objects.get(id=aid)
      if request.method=="POST":
        name=request.POST.get("txt_name")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        editdata.admin_name=name
        editdata.admin_email=email
        editdata.admin_password=password
        editdata.save()
        return redirect("Admin:AdminRegistration")
      else:  
       return render(request,"Admin/AdminRegistration.html",{'editdata':editdata})   

def Place(request):
    districtdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        place=request.POST.get("txt_place")
        tbl_place.objects.create(place_name=place,district=district)
        return render(request,"Admin/Place.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Place.html",{'districtdata':districtdata,'placedata':placedata})


def editplace(request,pid):
      districtdata=tbl_district.objects.all()
      editdata=tbl_place.objects.get(id=pid)
      if request.method=="POST":
        district=tbl_district.objects.get(id=request.POST.get("sel_district"))
        place=request.POST.get("txt_place")
        editdata.place_name=place
        editdata.district=district
        editdata.save()
        return redirect("Admin:Place")
      else:  
       return render(request,"Admin/Place.html",{'editdata':editdata,'districtdata':districtdata}) 

def Department(request):
    deptdata=tbl_department.objects.all()
    if request.method=="POST":
        department=request.POST.get("txt_deptname")
        tbl_department.objects.create(dept_name=department)
        return render(request,"Admin/Department.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Department.html",{'deptdata':deptdata})


def deldept(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect("Admin:Department")

def editdept(request,did):
      editdata=tbl_department.objects.get(id=did)
      if request.method=="POST":
        department=request.POST.get("txt_dept")
        editdata.dept_name=department
        editdata.save()
        return redirect("Admin:Department")
      else:  
       return render(request,"Admin/Department.html",{'editdata':editdata}) 



def designation(request):
    desidata=tbl_designation.objects.all()
    if request.method=="POST":
        designation=request.POST.get("txt_desi")
        tbl_designation.objects.create(designation_name=designation)
        return render(request,"Admin/Designation.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Designation.html",{'desidata':desidata})


def deldesi(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect("Admin:Designation")

def editdesi(request,did):
      editdata=tbl_designation.objects.get(id=did)
      if request.method=="POST":
        designation=request.POST.get("txt_desi")
        editdata.designation_name=designation
        editdata.save()
        return redirect("Admin:Designation")
      else:  
       return render(request,"Admin/Designation.html",{'editdata':editdata})        

def Employee(request):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    employeedata=tbl_employee.objects.all()
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        doj=request.POST.get("txt_doj")
        depname=tbl_department.objects.get(id=request.POST.get("sel_department"))
        desname=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
        salary=request.POST.get("txt_salary")
        tbl_employee.objects.create(employee_name=name,employee_gender=gender,employee_contact=contact,employee_doj=doj,department=depname,designation=desname,employee_salary=salary)
        return render(request,"Admin/Employee.html",{'msg':"Data Inserted"})
    else:
        return render(request,"Admin/Employee.html",{'employeedata':employeedata,'departmentdata':departmentdata,'designationdata':designationdata})
def editemployee(request,empid):
    departmentdata=tbl_department.objects.all()
    designationdata=tbl_designation.objects.all()
    editdata=tbl_employee.objects.get(id=empid)
    if request.method=="POST":
        name=request.POST.get("txt_name")
        gender=request.POST.get("txt_gender")
        contact=request.POST.get("txt_contact")
        doj=request.POST.get("txt_doj")
        departmentname=tbl_department.objects.get(id=request.POST.get("sel_department"))
        designationname=tbl_designation.objects.get(id=request.POST.get("sel_designation"))
        salary=request.POST.get("txt_salary")
        editdata.employee_name=name
        editdata.employee_gender=gender
        editdata.employee_contact=contact
        editdata.employee_doj=doj
        editdata.dept_name=departmentname
        editdata.designation_name=designationname
        editdata.employee_salary=salary
        editdata.save()
        return redirect("Admin:Employee")
    else:
        return render(request,"Admin/Employee.html",{'departmentdata':departmentdata,'designationdata':designationdata,'editdata':editdata})
def deleteemployee(request,empid):
    tbl_employee.objects.get(id=empid).delete()
    return redirect("Admin:Employee")


def UserList(request):
    userdata=tbl_newuser.objects.all()
    accuserdata=tbl_newuser.objects.filter(user_status=1)
    rejuserdata=tbl_newuser.objects.filter(user_status=2)
    return render(request,"Admin/UserList.html",{'userdata':userdata,'accuserdata':accuserdata,'rejuserdata':rejuserdata})

def SellerList(request):
    sellerdata=tbl_seller.objects.all()
    accsellerdata=tbl_seller.objects.filter(seller_status=1)
    rejsellerdata=tbl_seller.objects.filter(seller_status=2)
    return render(request,"Admin/SellerList.html",{'sellerdata':sellerdata,'accsellerdata':accsellerdata,'rejsellerdata':rejsellerdata})

def acceptseller(request,sid):
    data=tbl_seller.objects.get(id=sid)
    data.seller_status=1
    data.save()
    return render(request,'Admin/SellerList.html',{'msg':'verified'})  
    
def rejectseller(request,sid):
    data=tbl_seller.objects.get(id=sid)
    data.seller_status=2
    data.save()
    return render(request,'Admin/SellerList.html',{'msg':'rejected'})      
    
def acceptuser(request,uid):
    data=tbl_newuser.objects.get(id=uid)
    data.user_status=1
    data.save()
    return render(request,'Admin/UserList.html',{'msg':'verified'})  
    
def rejectuser(request,uid):
    data=tbl_newuser.objects.get(id=uid)
    data.user_status=2
    data.save()
    return render(request,'Admin/UserList.html',{'msg':'rejected'})      
        
def Homepage(request):
    admindata=tbl_adminreg.objects.get(id=request.session['aid'])
    return render(request,"Admin/Homepage.html",{'admindata':admindata})          

def ViewComplaint(request):
    viewcomplaintdata=tbl_complaint.objects.filter(complaint_status=0,serviceprovider__isnull=True)
    providerdata=tbl_serviceprovider.objects.all()
    replied=tbl_complaint.objects.filter(complaint_status=1,serviceprovider__isnull=True)
    return render(request,"Admin/ViewComplaint.html",{'viewcomplaintdata':viewcomplaintdata,'replied':replied,'serviceprovider':providerdata})

def Reply(request,cid):
    complaintdata = tbl_complaint.objects.get(id=cid)
    if request.method == "POST":
        reply = request.POST.get("txt_reply")
        complaintdata.complaint_reply= reply
        complaintdata.complaint_status = 1
        complaintdata.save()
        return render(request,"Admin/Reply.html",{'msg':"Replied.."})
    else:
        return render(request,"Admin/Reply.html")
    

def Serviceprovidertype(request):
    servicedata=tbl_serviceprovidertype.objects.all()
    if request.method=="POST":
        service=request.POST.get("txt_servicetype")
        servicecount = tbl_serviceprovidertype.objects.filter(serviceprovidertype_name=service).count()
        if servicecount > 0:
            return render(request, "Admin/Serviceprovidertype.html", {
                'msg': "Service Provider Type already exists",
                'servicedata': servicedata
            })
        tbl_serviceprovidertype.objects.create(serviceprovidertype_name=service)
        
        return render(request,"Admin/Serviceprovidertype.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Serviceprovidertype.html",{'servicedata':servicedata})    

def delservice(request,sid):
    tbl_serviceprovidertype.objects.get(id=sid).delete()
    return redirect("Admin:Serviceprovidertype")

def Serviceproviderlist(request):
    providerdata=tbl_serviceprovider.objects.filter(serviceprovider_status=0)
    accservicedata = tbl_serviceprovider.objects.filter(
        serviceprovider_status=1
    ).annotate(
        complaint_count=Count('tbl_complaint')
    )
    # accservicedata=tbl_serviceprovider.objects.filter(serviceprovider_status=1)
    rejservicedata=tbl_serviceprovider.objects.filter(serviceprovider_status=2)
    return render(request,"Admin/Serviceproviderlist.html",{'providerdata':providerdata,'accservicedata':accservicedata,'rejservicedata':rejservicedata,})

        
def acceptserviceprovider(request,sid):
    data=tbl_serviceprovider.objects.get(id=sid)
    data.serviceprovider_status=1
    data.save()
    email=data.serviceprovider_email
    send_mail(
        'Respected Sir/Madam ',#subject
        "\rYour request was accepted  "
        "\r1, You are  identified. "
        "\r2, if you have a proof of id , you will be accepted within two or three days."
        "\r By"
        "\r ecobloom" ,#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,'Admin/Serviceproviderlist.html',{'msg':'verified'})  
    
def rejectserviceprovider(request,sid):
    data=tbl_serviceprovider.objects.get(id=sid)
    data.serviceprovider_status=2
    data.save()
    return render(request,'Admin/Serviceproviderlist.html',{'msg':'rejected'})      

def Service(request):
    data=tbl_services.objects.all()
    servicedata=tbl_serviceprovidertype.objects.all()
    if request.method=="POST":
        service=request.POST.get("txt_service")
        servicetype=tbl_serviceprovidertype.objects.get(id=request.POST.get("sel_service"))
        tbl_services.objects.create(service_name=service,servicetype=servicetype)
        return render(request,"Admin/Service.html",{'msg':"Data inserted"})
    else:    
        return render(request,"Admin/Service.html",{'data':data,'servicedata':servicedata})

def delservicetype(request,stid):
    tbl_services.objects.get(id=stid).delete()
    return redirect("Admin:Service")   


def Complaintview(request):
    viewcomplaintdata = tbl_complaint.objects.filter(complaint_status=0,serviceprovider__isnull=False)
    replied = tbl_complaint.objects.filter(complaint_status=1,serviceprovider__isnull=False)
    
    return render(request, "Admin/Complaintview.html", {
        'viewcomplaintdata': viewcomplaintdata,
        'replied': replied
    })



def AddReply(request, complaint_id):
    if request.method == "POST":
        complaint = tbl_complaint.objects.get(id=complaint_id)
        reply_text = request.POST.get("complaint_reply")
        if reply_text:
            complaint.complaint_reply = reply_text
            complaint.complaint_status = 1  
            complaint.save()
    return redirect('Admin:Complaintview')


def Profit(request):
    profits = (
        tbl_profit.objects
        .values(
            'serviceprovider_id',
            'serviceprovider__serviceprovider_name',
            'serviceprovider__serviceprovidertype__serviceprovidertype_name'
        )
        .annotate(
            total_profit=Sum('profit_amount'),
            total_works=Count('id')   # 👈 count completed works
        )
    )

 
    return render(request, "Admin/Profit.html", {'profits': profits})







def Logout(request):
       del request.session['aid']
       return redirect("Guest:Login")



