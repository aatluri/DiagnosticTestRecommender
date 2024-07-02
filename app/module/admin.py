from django.contrib import admin

from .models import Tag, DiagnosticTest,Patient
# Register your models here.


# This file is used to customize the admin page.
# The DiagnosticTestAdmin is the class that controls the DiagnosticTest model on the admin page.
class DiagnosticTestAdmin(admin.ModelAdmin):
    # By default, a ManyToManyField is displayed in the admin site with a <select multiple>. However, multiple-select boxes can be difficult to use when selecting many items. Adding a ManyToManyField to this list will instead use a nifty unobtrusive JavaScript “filter” interface that allows searching within the options. The unselected and selected options appear in two boxes side by side. See filter_vertical to use a vertical interface.
    # This changes the admin interface display for the tags field in the diagnostic test to be horizontal instead of vertical. tags is the name of the field in diagnostictest
    filter_horizontal = ("tags",)
    list_filter = ("tags",) # Gives the ability to filter the tests based on the tags
    list_display = ('pk',"name","validity_days")  # List of columns that you want to show on the admin page

# The PatientAdmin is the class that controls the Patient model on the admin page.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('pk',"fullname","phonenumber","dateofbirth","gender")  # List of columns that you want to show on the admin page

# The TagsAdmin is the class that controls the Tags model on the admin page.
class TagsAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__',)


# Register the models
admin.site.register(DiagnosticTest,DiagnosticTestAdmin)
admin.site.register(Tag,TagsAdmin)
admin.site.register(Patient,PatientAdmin)