from django.db import models
from Admin.models import *
from Guest.models import *

# Create your models here.
class tbl_providerservice(models.Model):
  provider_amount=models.IntegerField()
  service_name=models.ForeignKey(tbl_services,on_delete=models.CASCADE) 

  
class tbl_workgallery(models.Model):
  work_description=models.CharField(max_length=50)
  work_photo=models.FileField(upload_to='Assets/WorkDocs/')  
  serviceprovider=models.ForeignKey(tbl_serviceprovider,on_delete=models.CASCADE)
  