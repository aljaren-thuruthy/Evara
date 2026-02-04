from django.db import models
from Admin.models import *



class tbl_newuser(models.Model):
    newuser_name=models.CharField(max_length=50)
    newuser_gender=models.CharField(max_length=10)
    newuser_contact=models.CharField(max_length=15)
    newuser_email=models.CharField(max_length=15)
    newuser_password=models.CharField(max_length=15)
    newuser_place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    newuser_address=models.CharField(max_length=15)
    newuser_photo=models.FileField(upload_to='Assets/UserDocs/')
    user_status=models.IntegerField(default=0)

class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_contact=models.CharField(max_length=15)
    seller_email=models.CharField(max_length=30)
    seller_password=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    seller_establishdate=models.DateField(max_length=12)
    seller_licenseno=models.CharField(max_length=15)
    seller_ownername=models.CharField(max_length=50)
    seller_licenseproof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_ownerproof=models.FileField(upload_to='Assets/SellerDocs/')
    seller_status=models.IntegerField(default=0)

class tbl_serviceprovider(models.Model):
    serviceprovider_name=models.CharField(max_length=50)
    serviceprovider_email=models.CharField(max_length=30)
    serviceprovider_contact=models.CharField(max_length=15)
    serviceprovider_address=models.CharField(max_length=15)
    serviceprovider_photo=models.FileField(upload_to='Assets/SellerDocs/')
    serviceprovider_idproof=models.FileField(upload_to='Assets/SellerDocs/')
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    serviceprovidertype=models.ForeignKey(tbl_serviceprovidertype,on_delete=models.CASCADE)
    serviceprovider_password=models.CharField(max_length=30)
    serviceprovider_status=models.IntegerField(default=0)
    serviceprovider_doj=models.DateField(auto_now_add=True)
