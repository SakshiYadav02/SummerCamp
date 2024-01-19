from django.db import models

class Program_Management(models.Model):
    Programid = models.AutoField(primary_key=True)
    ProgramName=models.CharField(max_length=100,null=False)
    Duration=models.CharField(max_length=20,null=False)
    Fees=models.CharField(max_length=30,null=False,default="")
    StartDate=models.DateField(null=False,default="")
    EndDate=models.DateField(null=False,default="")
    Description=models.TextField(null=False)
    AgeGroup=models.CharField(max_length=20,null=False)
    TeachingMode=models.CharField(max_length=20,null=False,default="")
    def __str__(self):
        return self.ProgramName


class Feedback(models.Model):
    FeedbackId = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=45,null=False)
    Email=models.CharField(max_length=45,null=False)
    Program_name=models.CharField(max_length=100,null=False,default="")
    Date=models.DateField(null=False)
    FeedbackText=models.TextField(null=False)
    Rating=models.IntegerField(null=False)
    def __str__(self):
        return self.Name

class JobDescription(models.Model):
    JobId = models.CharField(max_length=30,primary_key=True)
    PostName = models.CharField(max_length=30)
    NoOfSeats=models.IntegerField(null=False)
    LastDateToApply=models.DateField(null=False)
    PostDate=models.DateField(null=False)
    Description = models.TextField(null=False)
    def __str__(self):
        return self.PostName

class CityEvent(models.Model):
    EventId = models.AutoField(primary_key=True)
    EventName = models.CharField(max_length=100,null=False)
    Date = models.CharField(max_length=10,null=False)
    City=models.CharField(max_length=50,null=False)
    VenuAddress = models.TextField(null=False)
    Description = models.TextField(null=True)
    def __str__(self):
        return self.EventName

class ContactUs(models.Model):
    UserName = models.CharField(max_length=45,null=False)
    Email = models.CharField(max_length=45,null=True)
    Phone=models.CharField(max_length=10,null=False)
    Question=models.TextField(null=False)
    Date=models.DateField(null=False)
    def __str__(self):
        return self.UserName