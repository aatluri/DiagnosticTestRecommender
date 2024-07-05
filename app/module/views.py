from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Tag, DiagnosticTest,Patient, QuestionnaireResponses
from datetime import date
import datetime
from django.conf import settings

# Create your views here


# This view is used to render the patientinformation.html page.
def collectpatientinformation(request):
        # We pass the config values dictionary that we have defined in the settings.py file.
        return render(request,"module/patientinformation.html",{"configvalues":settings.CONFIG_VALUES})

# This view is used to render the diagnostictestquestionaire.html page.
# If you look in the patientinformation.html page, when the next button is clicked it redirects to the diagnostictestquestionaire url.
# In the urls.py that url maps to the below view, so Django calls this view
# Summary of what happens in this view:
      # We first get the values of the basic information fields that user entered in patientinformation.html
      # Based on that we check if this patient exists or not
      # If the patient exists, we then retrieve the patients choices from their last visit. We do this to prepopulate the choices when we load the diagnostictestquestionaire.html page
      # If the patient doest not exist, we create the patient in the database.
      # We store some of the variables in the session request so that it can be accessed in the next view.
      # We pass all these variables and the config_values dictionary we set in the settings.py file to the page.
def returndiagnostictestquestionaire(request):
        # Retrieves values entred by the user in the patientinformation.html page.
        if request.method == "POST":
            print("Entered questionaire post loop")
            fullname = request.POST["fullname"].lower()
            phonenumber = request.POST["phonenumber"]
            emailaddress = request.POST["email"]
            dateofbirth = request.POST["dateofbirth"]
            gender = request.POST["gender"].upper()
            # We calculate the age based on the dateofborth and set the age_range accordingly.
            age = date.today().year - datetime.datetime.strptime(dateofbirth, '%Y-%m-%d').year
            if age >= 50:
                  age_range = settings.CONFIG_VALUES["age_range_old"]
            else:
                  age_range=settings.CONFIG_VALUES["age_range_young"]
            # We try to see if this patient already exists by searching on name, gender, phonenumber and date of birth.
            patient = Patient()
            response=QuestionnaireResponses()
            smokingstatus=None
            drinkingstatus=None
            previnfection=None
            bloodexposure=None
            menstrualhistory=None
            comments=None
            if Patient.objects.filter(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth).exists(): # Patient  exists
                  print("patient exists")
                  patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
                  # if the patienr exists, then we update the email address and age range and
                  patient.emailaddress=emailaddress
                  patient.age_range = age_range
                  patient.save()
                  # We retrieve the choices of the patient from the database.
                  if QuestionnaireResponses.objects.filter(patient=patient).exists():
                        print("patient exists -> QuestionnaireResponses exists")
                        response = QuestionnaireResponses.objects.get(patient=patient)
                        smokingstatus=response.smokingstatus
                        drinkingstatus=response.drinkingstatus
                        previnfection=response.previnfection
                        menstrualhistory=response.menstrualhistory
                        bloodexposure = response.bloodexposure
                        comments=response.comments
                  else:
                        print("patient exists -> QuestionnaireResponse does not exist for patient")
                        response.patient=patient
                        response.smokingstatus=smokingstatus
                        response.drinkingstatus=drinkingstatus
                        response.previnfection=previnfection
                        response.menstrualhistory=menstrualhistory
                        response.bloodexposure=bloodexposure
                        response.comments=comments
                        response.patient=patient
                        response.save()
                        print("patient exists -> QuestionnaireResponse does not exist for patient -> Created response for patient")

                  # We set this variable so that it can be used later.
                  existingpatient="yes"
            else: # Patient does not exist
                  # if the patient does not exist then we create a new patient object, update the basic information and set the choices like smoking etc... to None.
                  print("patient does not exist")
                  patient = Patient()
                  patient.fullname=fullname
                  patient.phonenumber=phonenumber
                  patient.emailaddress=emailaddress
                  patient.dateofbirth=dateofbirth
                  patient.gender=gender
                  patient.age_range=age_range
                  patient.save()
                  print("patient does not exist->patient created")
                  response.patient=patient
                  response.smokingstatus=smokingstatus
                  response.drinkingstatus=drinkingstatus
                  response.previnfection=previnfection
                  response.menstrualhistory=menstrualhistory
                  response.bloodexposure=bloodexposure
                  response.comments=comments
                  response.save()
                  print("patient does not exist->patient created->response created")
                  # We set this variable so that it can be used later.
                  existingpatient="no"
            # We store the below variables in the session so that we can pass the below attributes passed to the next view
            request.session['fullname'] = fullname
            request.session['phonenumber'] = phonenumber
            request.session['dateofbirth'] = dateofbirth
            request.session['gender'] = gender
            request.session['age_range'] = age_range
            print(fullname,phonenumber,emailaddress,dateofbirth,gender,age_range)
            # We render the diagnostictestquestionaire page by passing it a bunch of variables and the config_values dictionary.
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


# This view is used to render the displaydiagnostictests.html page.
# If you look in the diagnostictestquestionaire.html page, when the submit button is clicked it redirects to the displaydiagnostictests url.
# In the urls.py that url maps to the below view, so Django calls this view
# Summary of what happens in this view:
      # We retrive the patients basic information like name etc.. that we stored in the request session.
      # We retrive the values of the choices the patient chose in the diagnostictestquestionaire page.
      # We now first filter the diagnostic tests by the gender and age_range of the patient, the test type and create a queryset. This is for the general health checkup tests
      # We then filter the tests based on the gender, smoking habit and test type and create a queryset.
      # We do the same for drinking , prev infection, blood exposure and menstrual history.
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
            if gender == settings.CONFIG_VALUES["gender_female"]:
                  menstrualhistory = request.POST["menstrualhistory"]
            else:
                  menstrualhistory=None
            print(fullname,phonenumber,dateofbirth,gender,age_range,smokingstatus,drinkingstatus,previnfection,bloodexposure,menstrualhistory)
            # Retreive the patient so that we can update theor questionaire choices incase they have been modifed
            if Patient.objects.filter(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth).exists():
                  print("displaytests -> patient exists")
                  patient = Patient.objects.get(fullname=fullname,gender=gender,phonenumber=phonenumber,dateofbirth=dateofbirth)
                  if QuestionnaireResponses.objects.filter(patient=patient).exists():
                        print("displaytests -> response exists")
                        response = QuestionnaireResponses.objects.get(patient=patient)
                        response.smokingstatus=smokingstatus
                        response.drinkingstatus=drinkingstatus
                        response.previnfection=previnfection
                        response.menstrualhistory=menstrualhistory
                        response.bloodexposure=bloodexposure
                        response.comments=comments
                        response.save()
                  else:
                        print("displaytests -> response does not exist")
            else:
                   print("displaytests -> patient does not exist")
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


            # Creating Query set for the Drinking Status.
            querysetdrinking = DiagnosticTest.objects.all()
            querysetdrinking = querysetdrinking.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetdrinking = querysetdrinking.filter(tags__tagname = gender)
            querysetdrinking = querysetdrinking.filter(tags__tagname = drinkingstatus)
            print(querysetdrinking)

            # Creating Query set for the Prev Infection.
            querysetprevinfection = DiagnosticTest.objects.all()
            querysetprevinfection = querysetprevinfection.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetprevinfection = querysetprevinfection.filter(tags__tagname = gender)
            querysetprevinfection = querysetprevinfection.filter(tags__tagname = previnfection)
            print(querysetprevinfection)

            # Creating Query set for the blood exposure
            querysetbloodexposure = DiagnosticTest.objects.all()
            querysetbloodexposure = querysetbloodexposure.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetbloodexposure = querysetbloodexposure.filter(tags__tagname = gender)
            querysetbloodexposure = querysetbloodexposure.filter(tags__tagname = bloodexposure)
            print(querysetbloodexposure)

            # Creating Query set for the menstrualhistory
            querysetmenstrualhistory = DiagnosticTest.objects.all()
            querysetmenstrualhistory = querysetmenstrualhistory.filter(tags__tagname = settings.CONFIG_VALUES["testtype_personalised"] )
            querysetmenstrualhistory = querysetmenstrualhistory.filter(tags__tagname = gender)
            querysetmenstrualhistory = querysetmenstrualhistory.filter(tags__tagname = menstrualhistory)
            print(querysetmenstrualhistory)

            # If there are no personalised tests, then we set a varialbel that we will use in the page to display some html content.
            if(querysetsmoking.count() ==0 and querysetdrinking.count() ==0 and querysetprevinfection.count() ==0 and querysetbloodexposure.count() ==0 and querysetmenstrualhistory.count() ==0):
                  personalisedtests = "no"
            else:
                  personalisedtests = "yes"

            # We render the displaydiagnostictests.html page by passing the query sets and variables.
            return render(request,"module/displaydiagnostictests.html",{
            "querysethealthcheckup": querysethealthcheckup,
            "querysetsmoking": querysetsmoking,
            "querysetdrinking": querysetdrinking,
            "querysetprevinfection": querysetprevinfection,
            "querysetbloodexposure": querysetbloodexposure,
            "querysetmenstrualhistory": querysetmenstrualhistory,
            "personalisedtests": personalisedtests
            })
         return render(request,"module/displaydiagnostictests.html")



