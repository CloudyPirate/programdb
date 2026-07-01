from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export import fields
from programs.models import Team
from .models import Coach

# Register your models here.
class CoachResource(resources.ModelResource):
    def for_delete(self, row, instance):
        return row["delete"] == "1"

    programs = fields.Field(
        column_name='programs',
        attribute='programs',
        widget=ForeignKeyWidget(Team,'name'),
    )

    class Meta:
            model = Coach
            fields = ('id','Coach_First_Name','Coach_Last_Name','programs')

class CoachAdmin(ImportExportModelAdmin):
    list_display = ['Coach_Headshot','Coach_First_Name','Coach_Last_Name','Coach_Role','programs']
    resource_class = CoachResource

admin.site.register(Coach,CoachAdmin)