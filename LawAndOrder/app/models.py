from django.db import models

class Police(models.Model):
    police_id=models.IntegerField(primary_key=True)
    police_name=models.CharField(max_length=30)
    date_of_birth=models.DateField(default=False)
    address=models.CharField(max_length=100)
    mobile_no=models.IntegerField()
    designation=models.CharField(max_length=15)
    station_id=models.IntegerField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=30)

class Detective(models.Model):
    detective_id=models.IntegerField(primary_key=True)
    detective_name=models.CharField(max_length=30)
    date_of_birth=models.DateField()
    mobile_no=models.IntegerField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

class Citizen(models.Model):
    citizen_id=models.AutoField(primary_key=True)
    citizen_name=models.CharField(max_length=30)
    date_of_birth = models.DateField()
    email_id=models.EmailField(max_length=30)
    gender=models.CharField(max_length=10,choices=(("Male","male"),("Female","female")))
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

class Station(models.Model):
    station_id= models.IntegerField(primary_key=True)
    station_name=models.CharField(max_length=20)
    address= models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    contact_no=models.IntegerField()

class Complent(models.Model):
    complent_id=models.AutoField(primary_key=True)
    complent_type=models.CharField(max_length=20)
    complient_name=models.CharField(max_length=30)
    date_of_complent=models.DateTimeField()
    description=models.CharField(max_length=500)
    proof=models.FileField(upload_to="Doucuments/proof")
    station_id=models.IntegerField()
    location=models.CharField(max_length=50)


class Criminal(models.Model):
    criminal_id=models.AutoField(primary_key=True)
    criminal_name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="document/criminal/Image")
    crime=models.CharField(max_length=100)

class Status(models.Model):
    complent_id = models.AutoField(primary_key=True)
    complent_type = models.CharField(max_length=20)
    complient_name = models.CharField(max_length=30)
    date_of_complent = models.CharField(max_length=30,default=False)
    description = models.CharField(max_length=500)
    station_id = models.IntegerField()
    location = models.CharField(max_length=50)
    status=models.CharField(max_length=30)

