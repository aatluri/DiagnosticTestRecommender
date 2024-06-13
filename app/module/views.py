from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# We create a function based view.
# In this view we just return a simple http response without any fancy html etc..
def simplehttpresponse(request):
    return HttpResponse("This is a simple http response")


# We create another function based view.
# We are showcasing a dynamic path segment here
# In this view also take the parameter that was passed in the url path and use that in the response txt
# In the url pattern that is mapped to this view, the value that is between <> is passed to this function.
# The value between the <> in the url pattern should match the argument name in the view function.
def dynamicpathsegment(request, pathparameter):
    responsetext = "This is a dyamic http respose where " + pathparameter + " was passed and it is a string"
    return HttpResponse(responsetext)
# We created this view to show that we could call different views based on the type of pathparameter.
# So if its an integer dynamicpathsegment_bynumber is called , else dynamicpathsegment is called. This is define din the urls.py
def dynamicpathsegment_bynumber(request, pathparameter):
    responsetext = "This is a dyamic http respose where " + str(pathparameter) + " was passed and it is a number"
    return HttpResponse(responsetext)

# We are showcasing a redirect in the below two views.
# In the shallwe_redirect view, we take the pathparameter and check its value.
# if it is equal to redirect then we return a redirect url /module/shallweredirect/yes.
# Django goes back to the urls.py and sees which view needs to be called for this url pattern.
# It sees that shallwe_redirect_yes needs to be called and so that view is called.
# if the pathparameter passed is not redirect then it just returns a httpresponse like normal.
def shallwe_redirect(request, pathparameter):
    print(pathparameter)
    if pathparameter == "redirect":
        print("entered if")
        return HttpResponseRedirect("/module/shallweredirect/yes")
    else :
        print("entered else")
        responsetext = "Redirect has not happened because " + pathparameter + " was passed"
        return HttpResponse(responsetext)
def shallwe_redirect_yes(request, pathparameter):
    responsetext = "Redirect has happened because " + pathparameter + " was passed"
    return HttpResponse(responsetext)


# We are showcasing a redirect using a named url in the below two views.
# We have already set up the url patterns in the urls.py
# The shallwedo_named_url_redirect checks the pathparameter passed.
# if it is redirect, then it retreives the url for named-url from urls.py and concatenates that with /yes and sends a httpresponseredirect which directs it to the shallwedo_named_url_redirect_yes view as per the urls.py
# if it is not redirect, then it just returns a normal httpresponse.
def shallwedo_named_url_redirect(request, pathparameter):
    if pathparameter == "redirect":
        namedurl = reverse("named-url", args = [pathparameter])
        print(namedurl)
        return HttpResponseRedirect(namedurl + "/yes")
    else :
        responsetext = "Named Url Redirect has not happened because " + pathparameter + " was passed"
        return HttpResponse(responsetext)
def shallwedo_named_url_redirect_yes(request):
    responsetext = "Named Url Redirect has happened because redirect " + " was passed"
    return HttpResponse(responsetext)


# The below 2 views showcase that we can return html in the respose
# So what we do in this view is return html which contains a link which when clicked takes us to
# that url and returns the appropriate response as defined in its respective view
def returnhtml(request):
    print("entered")
    namedurl = reverse("simple-html-response")
    responsetext= f"<ul><li><a href=\"{namedurl}\">simplehtmlresponse</a></li>"+"</ul>"
    print(responsetext)
    return HttpResponse(responsetext)

def simplehtmlresponse(request):
    return HttpResponse("<h1>This is a simple http response</h1>")