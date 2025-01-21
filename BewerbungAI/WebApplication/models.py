from django.db import models


# Attribute Creation for Database (intern)
class Data(models.Model):
    id = models.IntegerField(primary_key=True)

    # Personal Information
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthday = models.DateField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone = models.CharField(max_length=17)
    email = models.EmailField()
    date = models.DateField()
    experience = models.TextField(max_length=200)
    education = models.TextField(max_length=200)
    skills = models.TextField(max_length=200)
    interests = models.TextField(max_length=200)

    # Job Description Information
    managerName = models.CharField(max_length=30)
    companyName = models.CharField(max_length=25)
    companyAddress = models.CharField(max_length=50)
    companyCity = models.CharField(max_length=50)
    companyZipCode = models.CharField(max_length=10)
    jobFieldName = models.CharField(max_length=50)
    jobFieldContent = models.TextField(max_length=400)

    # Generated JobApplication letter
    jobApplicationContent = models.TextField()

    # Only necessary for /admin endpoint to give it a naming
    def __str__(self):
        return self.jobFieldName
