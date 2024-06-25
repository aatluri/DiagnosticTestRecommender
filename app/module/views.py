from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Tag, DiagnosticTest,Patient
from datetime import date
import datetime
from django.conf import settings

# Create your views here


def returntestform(request):
        if request.method == "POST":
             print("Entered post")
        return render(request,"module/testform.html")


def collectpatientinformation(request):
        return render(request,"module/patientinformation.html",{"configvalues":settings.CONFIG_VALUES})

def returndiagnostictestquestionaire(request):

        if request.method == "POST":
            print("Entered questionaire post loop")
            fullname = request.POST["fullname"].lower()
            phonenumber = request.POST["phonenumber"]
            emailaddress = request.POST["email"]
            dateofbirth = request.POST["dateofbirth"]
            gender = request.POST["gender"].upper()

            age = date.today().year - datetime.datetime.strptime(dateofbirth, '%Y-%m-%d').year
            if age >= 50:
                  age_range = settings.CONFIG_VALUES["age_range_old"]
            else:
                  age_range=settings.CONFIG_VALUES["age_range_young"]
            patient = Patient()
            if Patient.objects.filter(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth).exists(): # Patient  exists
                    patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
                    patient.emailaddress=emailaddress
                    patient.age_range = age_range
                    smokingstatus=patient.smokingstatus
                    drinkingstatus=patient.drinkingstatus
                    previnfection=patient.previnfection
                    menstrualhistory=patient.menstrualhistory
                    bloodexposure = patient.bloodexposure
                    comments=patient.comments
                    patient.save()
                    existingpatient="yes"
            else:         # Patient does not exist

                    patient = Patient()
                    patient.fullname=fullname
                    patient.phonenumber=phonenumber
                    patient.emailaddress=emailaddress
                    patient.dateofbirth=dateofbirth
                    patient.gender=gender
                    patient.age_range=age_range
                    patient.save()
                    smokingstatus=None
                    drinkingstatus=None
                    previnfection=None
                    menstrualhistory=None
                    bloodexposure=None
                    comments=None
                    existingpatient="no"
            # Pass the below attributes passed to the next view
            request.session['fullname'] = fullname
            request.session['phonenumber'] = phonenumber
            request.session['dateofbirth'] = dateofbirth
            request.session['gender'] = gender
            request.session['age_range'] = age_range
            print(fullname,phonenumber,emailaddress,dateofbirth,gender,age_range)
            return render(request,"module/diagnostictestquestionaire.html",{
            "fullname": fullname.capitalize()   ,
            "phonenumber":phonenumber,
            "email": emailaddress,
            "dateofbirth": dateofbirth,
            "gender": gender,
            "smokingstatus" : smokingstatus,
            "drinkingstatus" : drinkingstatus,
            "previnfection" : previnfection,
            "menstrualhistory" : menstrualhistory,
            "bloodexposure" : bloodexposure,
            "comments":comments,
            "existingpatient" : existingpatient,
            "configvalues": settings.CONFIG_VALUES
            })

        return render(request,"module/diagnostictestquestionaire.html")



def displaydiagnostictests(request):
         if request.method == "POST":
            print("Entered display diagnostic text form post")
            # Retrieve the attributes passed from the previous view
            fullname = request.session.get('fullname', None)
            phonenumber = request.session.get('phonenumber', None)
            dateofbirth = request.session.get('dateofbirth', None)
            gender = request.session.get('gender', None)
            age_range = request.session.get('age_range', None)

            # Retrive the options chosen by the user from the html page.
            smokingstatus = request.POST["smokingstatus"]
            drinkingstatus = request.POST["drinkingstatus"]
            previnfection = request.POST["previnfection"]
            bloodexposure = request.POST["bloodexposure"]
            comments = request.POST["comments"]
            # Look for mensturalhistory value only if gender is female.
            if gender == "Female":
                menstrualhistory = request.POST["menstrualhistory"]
            else:
                menstrualhistory=None


            print(fullname,phonenumber,dateofbirth,gender,age_range,smokingstatus,drinkingstatus,previnfection,bloodexposure)
            # Retreive the patient so that we can update theor questionaire choices incase they have been modifed
            patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
            if Patient.objects.filter(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth).exists():
                   patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
                   patient.smokingstatus = smokingstatus
                   patient.drinkingstatus = drinkingstatus
                   patient.previnfection = previnfection
                   patient.menstrualhistory = menstrualhistory
                   patient.comments = comments
                   patient.bloodexposure=bloodexposure
                   patient.save()
            else:
                   print("Patient object was None")
            print("Reached here")
            # Here we are filtering the diagnostic tests queryset by each tag. At the end of this code we will only have the tests that have all the tags we want to filter by.
            # Creating Query set for the General Healt Check up that is based on gender and age.
            querysethealthcheckup = DiagnosticTest.objects.all()
            querysethealthcheckup = querysethealthcheckup.filter(tags__tagname = settings.CONFIG_VALUES["testtype_healthcheckup"] )
            querysethealthcheckup = querysethealthcheckup.filter(tags__tagname = gender)
            querysethealthcheckup = querysethealthcheckup.filter(tags__tagname = age_range)
            print(querysethealthcheckup)

            # Creating Query set for the Smoking Status.
            querysetsmoking = DiagnosticTest.objects.all()
            querysetsmoking = querysetsmoking.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetsmoking = querysetsmoking.filter(tags__tagname = gender)
            querysetsmoking = querysetsmoking.filter(tags__tagname = smokingstatus)
            print(querysetsmoking)

            # Creating Query set for the Smoking Status.
            querysetdrinking = DiagnosticTest.objects.all()
            querysetdrinking = querysetdrinking.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetdrinking = querysetdrinking.filter(tags__tagname = gender)
            querysetdrinking = querysetdrinking.filter(tags__tagname = drinkingstatus)
            print(querysetdrinking)

            return render(request,"module/displaydiagnostictests.html",{
            "diagnostictests_healthcheckup": querysethealthcheckup,
            "diagnostictests_smokingstatus": querysetsmoking,
            "diagnostictests_drinkingstatus": querysetdrinking
            })
         return render(request,"module/displaydiagnostictests.html")



