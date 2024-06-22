from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Tag, DiagnosticTest,Patient

# Create your views here


def returntestform(request):
        if request.method == "POST":
             print("Entered post")
        return render(request,"module/testform.html")


def collectpatientinformation(request):
        return render(request,"module/patientinformation.html")

def returndiagnostictestquestionaire(request):

        if request.method == "POST":
            print("Entered questionaire post loop")
            fullname = request.POST["fullname"]
            phonenumber = request.POST["phonenumber"]
            emailaddress = request.POST["email"]
            dateofbirth = request.POST["dateofbirth"]
            gender = request.POST["gender"]

            patient = Patient()
            if Patient.objects.filter(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth).exists(): # Patient  exists
                    patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
                    patient.emailaddress=emailaddress
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
            print(fullname,phonenumber,emailaddress,dateofbirth,gender)
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
            "existingpatient" : existingpatient
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

            smokingstatus = request.POST["smokingstatus"]
            drinkingstatus = request.POST["drinkingstatus"]
            previnfection = request.POST["previnfection"]
            if gender == "Female":
                menstrualhistory = request.POST["menstrualhistory"]
            else:
                menstrualhistory=None
            bloodexposure = request.POST["bloodexposure"]
            comments = request.POST["comments"]

            print(fullname,phonenumber,dateofbirth,gender)
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
                   print("patient object was None")
            print("Reached here")
            diagnostictests = {
            "Complete Blood Count": "A complete blood count (CBC) is a blood test. It's used to look at overall health and find a wide range of conditions, including anemia, infection and leukemia",
            "Urine Analysis": "Healthcare providers often use urinalysis tests to screen for or monitor certain health conditions and to diagnose urinary tract infections."
            }
            return render(request,"module/displaydiagnostictests.html",{
            "diagnostictests": diagnostictests
            })
         return render(request,"module/displaydiagnostictests.html")



