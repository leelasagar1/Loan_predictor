from django.db import models

# Create your models here.

class Approval(models.Model):

    Gender_choices = (
        ('Male','Male'),
        ('Female','Female')
    )
    Married_choices = (
        ('Yes','Yes'),
        ('No','No')
    )
    Graduated_choices=(
        ('Graduate','Graduate'),
        ('Not_Graduate','Not_Graduate')
    )   
    Selfemployed_choices=(
        ('Yes','Yes'),
        ('No','No')
    )
    Property_choices=(
        ("Rural",'Rural'),
        ('SemiUrban','SemiUrban'),
        ('Urban','Urban')
    )
    Credit_choices=(
        ('Yes','Yes'),
        ('No','No')
    )
    Dependant_choices = (
        ('Yes','Yes'),
        ('No','No')
    )
    firstname = models.CharField(max_length=15)
    lastname = models.CharField(max_length=15)
    dependants = models.CharField(max_length=5,choices=Credit_choices)
    applicantincome = models.IntegerField()
    coapplicantincome = models.IntegerField()
    loanamount = models.IntegerField()
    loanterm = models.IntegerField()
    credithistory = models.CharField(max_length=5,choices=Credit_choices)
    gender = models.CharField(max_length=15,choices=Gender_choices)
    married = models.CharField(max_length=15,choices=Married_choices)
    graduatededucation=models.CharField(max_length=15,choices=Graduated_choices)
    selfemployed = models.CharField(max_length=15,choices=Selfemployed_choices)
    area = models.CharField(max_length=15,choices=Property_choices)

    def __str__(self):
        return self.firstname,self.lastname