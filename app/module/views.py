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
             print("Entered post")
             fullname = request.POST["fullname"]
             phonenumber = request.POST["phonenumber"]
             email = request.POST["email"]
             dateofbirth = request.POST["dateofbirth"]
             gender = request.POST["gender"]
             existingpatient= "yes"
             smokingstatus= None
             drinkingstatus = None
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




