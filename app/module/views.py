from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string


# Create your views here


def returntestform(request):
        if request.method == "POST":
             print("Entered post")
        return render(request,"module/testform.html")


def collectpatientinformation(request):
        return render(request,"module/patientinformation.html")

def returndiagnostictestquestionaire(request):
        if request.method == "POST":
             print("Entered question form post")
             fullname = request.POST["fullname"]
             phonenumber = request.POST["phonenumber"]
             email = request.POST["email"]
             dateofbirth = request.POST["dateofbirth"]
             gender = request.POST["gender"]
             existingpatient= "yes"
             smokingstatus= "regularsmoker"
             drinkingstatus = "lightdrinker"
             previnfection = None
             menstrualhistory = None
             print(fullname,phonenumber,email,dateofbirth,gender)
             return render(request,"module/diagnostictestquestionaire.html",{
            "fullname": fullname.capitalize()   ,
            "phonenumber":phonenumber,
            "email": email,
            "dateofbirth": dateofbirth,
            "gender": gender,
            "smokingstatus" : smokingstatus,
            "drinkingstatus" : drinkingstatus,
            "previnfection" : previnfection,
            "menstrualhistory" : menstrualhistory,
            "existingpatient": existingpatient
            })

        return render(request,"module/diagnostictestquestionaire.html")



def displaydiagnostictests(request):
         if request.method == "POST":
             print("Entered display diagnostic text form post")
             diagnostictests = {
            "Complete Blood Count": "A complete blood count (CBC) is a blood test. It's used to look at overall health and find a wide range of conditions, including anemia, infection and leukemia",
            "Urine Analysis": "Healthcare providers often use urinalysis tests to screen for or monitor certain health conditions and to diagnose urinary tract infections."
            }
             return render(request,"module/displaydiagnostictests.html",{
            "diagnostictests": diagnostictests
            })
         return render(request,"module/displaydiagnostictests.html")



