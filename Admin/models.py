from django.db import models

# Create your models here.
class tbl_district(models.Model):
  district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
  category_name=models.CharField(max_length=50) 
class tbl_adminreg(models.Model):
  admin_name=models.CharField(max_length=50)
  admin_email=models.CharField(max_length=50)  
  admin_password=models.CharField(max_length=50)
class tbl_place(models.Model):
  place_name=models.CharField(max_length=50) 
  district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)
class tbl_department(models.Model):
 dept_name=models.CharField(max_length=50)  
class tbl_designation(models.Model):
 designation_name=models.CharField(max_length=50)  
class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=50)
    employee_gender=models.CharField(max_length=10)
    employee_contact=models.CharField(max_length=15)
    employee_doj=models.DateField(max_length=12)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    designation=models.ForeignKey(tbl_designation,on_delete=models.CASCADE)
    employee_salary=models.IntegerField(max_length=16)
    
class tbl_serviceprovidertype(models.Model):
  serviceprovidertype_name=models.CharField(max_length=50)

class tbl_services(models.Model):
  service_name=models.CharField(max_length=50) 
  servicetype=models.ForeignKey(tbl_serviceprovidertype,on_delete=models.CASCADE)



    