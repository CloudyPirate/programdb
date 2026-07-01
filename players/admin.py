from django.contrib import admin
from import_export import resources
from .models import Player
from programs.models import Program, Team
from import_export.admin import ImportExportModelAdmin
from import_export import fields
from import_export.widgets import ForeignKeyWidget
# Register your models here.

class PlayerResource(resources.ModelResource):
    def for_delete(self, row, instance):
        return row["delete"] == "1"

    programs = fields.Field(
        column_name='team',
        attribute='teams',
        widget=ForeignKeyWidget(Team, 'name'),
    )

    class Meta:
        model = Player
        fields = ('id','first_name','last_name','birth_date','team','player_year','player_position', 'playerUni_size')

class PlayerAdmin(ImportExportModelAdmin):
    list_display = ('id','first_name','last_name','birth_date','player_year','team','player_position', 'playerUni_size')
    search_fields = ('first_name','last_name','birth_date','team')
    resource_class = PlayerResource

admin.site.register(Player, PlayerAdmin)