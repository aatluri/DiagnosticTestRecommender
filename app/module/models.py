from django.db import models

# Create your models here.


class Patient(models.Model):
    fullname = models.CharField(max_length=150)
    phonenumber = models.IntegerField()
    emailaddress = models.CharField(max_length=150)
    dateofbirth = models.DateField(max_length=8)
    gender = models.CharField(max_length=6)

    # When we do this, in the admin page when the diagnostic tests are displayed, it will show their name
    def __str__(self):
        return self.fullname

class Tag(models.Model):
    tagname = models.CharField(max_length=20)

    def __str__(self):
        return self.tagname


class DiagnosticTest(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    validity_days = models.IntegerField()
    tags =  models.ManyToManyField(Tag,blank=True, editable=True)

    # When we do this, in the admin page when the diagnostic tests are displayed, it will show their name
    def __str__(self):
        return self.name

