from django.db import models

# Create your models here.


class Data(models.Model):
    id = models.IntegerField(primary_key=True)

    # Personal Information
    surname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birthday = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=25)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    date = models.DateField()
    experience = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    interests = models.TextField()

    # Job Description Information
    companyname = models.CharField(max_length=25)
    companyaddress = models.CharField(max_length=50)
    companycity = models.CharField(max_length=50)
    companyzipcode = models.CharField(max_length=25)
    commpanystate = models.CharField(max_length=50)
    jobFieldName = models.CharField(max_length=50)
    jobFieldContent = models.TextField()

    # Generated JobApplication letter
    jobApplicationId = models.IntegerField()
    jobApplicationContent = models.TextField()

    def __str__(self):
        return self.jobFieldName