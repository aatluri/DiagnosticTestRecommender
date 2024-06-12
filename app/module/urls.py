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
    path('dynamichttpresponse/<pathparameter>', views.dynamicpathsegment)
]