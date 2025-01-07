from django.db import models

# Create your models here.


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    idJobApplication = models.IntegerField()
    surname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    personId = models.IntegerField()
    jobApplicationId = models.IntegerField()
    jobApplicationContent = models.TextField()
    jobFieldName = models.CharField(max_length=100)
    jobFieldContent = models.TextField()

    def __str__(self):
        return self.jobFieldName