from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# We create a function based view.
# In this view we just return a simple http response without any fancy html etc..
def simplehttpresponse(request):
    return HttpResponse("This is a simple http response without any html")


# We create another function based view.
# We are showcasing a dynamic path segment here
# In this view also take the parameter that was passed in the url path and use that in the response txt
# In the url pattern that is mapped to this view, the value that is between <> is passed to this function.
# The value between the <> in the url pattern should match the argument name in the view function.
def dynamicpathsegment(request, pathparameter):
    responsetext = "This is a dyamic http respose where " + pathparameter + " was passed"
    return HttpResponse(responsetext)