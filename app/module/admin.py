from django.contrib import admin

from .models import Tag, DiagnosticTest,Patient
# Register your models here.


class DiagnosticTestAdmin(admin.ModelAdmin):
    # By default, a ManyToManyField is displayed in the admin site with a <select multiple>. However, multiple-select boxes can be difficult to use when selecting many items. Adding a ManyToManyField to this list will instead use a nifty unobtrusive JavaScript “filter” interface that allows searching within the options. The unselected and selected options appear in two boxes side by side. See filter_vertical to use a vertical interface.
    # This changes the admin interface display for the tags field in the diagnostic test to be horizontal instead of vertical. tags is the name of the field in diagnostictest
    filter_horizontal = ("tags",)

admin.site.register(DiagnosticTest,DiagnosticTestAdmin)
admin.site.register(Tag)
admin.site.register(Patient)