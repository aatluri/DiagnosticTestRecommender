from django.urls import path
from . import views

# This urls.py is a file we created specifically for this module app.
# We create a url pattern for the module app that tells Django which view to call for a particular url pattern related to this module app.
# But we also need to include all the module app urls in the main apps urls.py i.e app/urls.py
urlpatterns= [
    # We are telling Django that for a /module/simplehttpresponse url pattern, it should call the simplehttpresponse view.
    path('simplehttpresponse', views.simplehttpresponse),
    # We are telling Django that for a /module/dynamichttpresponse/...  url pattern, it should call the dynamicpathsegment view.
    # The value that is passed after the dynamichttpresponse/ in the url is also passed to the view automatically function as you will see in the views.py
    # The value between the <> should match the argument name in the view function.
    # The str tells Django that it should be handled as a string
    # The int tells Django that if the passed in value can be converted to an int, then it should call the dynamicpathsegment_bynumber view
    # if not then it calls the dynamicpathsegment view.
    # These are called path converters.
    path('dynamichttpresponse/<int:pathparameter>', views.dynamicpathsegment_bynumber),
    path('dynamichttpresponse/<str:pathparameter>', views.dynamicpathsegment),
    # The below 2 url patterns are defined to show case the ability of a view to return a redirect to another url .
    path('shallweredirect/<pathparameter>', views.shallwe_redirect),
    path('shallweredirect/yes/<pathparameter>', views.shallwe_redirect_yes),
    # The below 2 url patterns are defined to show how to use named urls. By ggiving a utl pattern a name, we can retrive the url pattern by using that name in the views.
    path('shallwedoanamedurlredirect/<pathparameter>', views.shallwedo_named_url_redirect, name = "named-url"),
    path('shallwedoanamedurlredirect/redirect/yes', views.shallwedo_named_url_redirect_yes),
    # The below url patern is to demonstrate that we can return html in the view.
    path('simplehtmlresponse', views.simplehtmlresponse, name="simple-html-response"),
    path('returnhtml', views.returnhtml)


]