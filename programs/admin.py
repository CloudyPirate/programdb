from django.contrib import admin
from import_export import resources
from .models import Program,Team
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget



# Register your models here.
class ProgramResource(resources.ModelResource):

    def for_delete(self, row, instance):
        return row["delete"] == "1"

    class Meta:
            model = Program
            fields = ('id','key','name','description')

class ProgramAdmin(ImportExportModelAdmin):
    list_display = ('id','key','name','description','program_active')
    search_fields = ['key','name','description','program_active']
    resource_class = ProgramResource



class TeamResource(resources.ModelResource):
    def for_delete(self, row, instance):
        return row["delete"] == "1"

    programs = fields.Field(
        column_name='programs',
        attribute='programs',
        widget=ForeignKeyWidget(Team, 'name'),
    )

    class Meta:
            model = Team
class TeamAdmin(ImportExportModelAdmin):
    list_display = ('id','name','description','practice_start_date','practice_end_date','practice_location','programs')
    resource_class = TeamResource


admin.site.register(Program,ProgramAdmin)
admin.site.register(Team,TeamAdmin)