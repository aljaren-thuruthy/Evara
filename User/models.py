from django.db import models
from Guest.models import*

class tbl_complaint(models.Model):

    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=10)
    complaint_date=models.DateField(auto_now_add=True) 
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE,null=True)
    

class tbl_request(models.Model):
    date=models.DateField(auto_now_add=True) 
    request_status=models.IntegerField(default=0)
    request_amount=models.IntegerField(default=0)
    request_bill=models.FileField(upload_to='Assets/RequestDocs/')
    request_todate=models.DateField() 
    request_details=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    service=models.ForeignKey(tbl_services,on_delete=models.CASCADE)
    serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE)

class tbl_profit(models.Model):
      profit_amount=models.IntegerField(default=0)
      profit_date=models.DateField(auto_now_add=True)  
      user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
      request=models.ForeignKey(tbl_request,on_delete=models.CASCADE)
      serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE)
      
      



class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user=models.ForeignKey(tbl_newuser,on_delete=models.CASCADE)
    user_review=models.CharField(max_length=500)
    serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)
