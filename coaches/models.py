from django.db import models
from mysite.models import TimeStampedModel
from programs.models import Team
from django.utils.html import format_html
# Create your models here.

class Coach(TimeStampedModel):
    coach_choices = [
        ('HC', "Head-Coach"),
        ('AC', "Assistance-Coach"),
        ('O', "Offense"),
        ('D', "Defense"),
        ('G', "Goalie"),
        ('FC', "Face-off"),
    ]
    #Multi-tenant-approach not yet created for image uploads.
    #I assume it will work the same and upload to the db.
    Coach_Headshot = models.ImageField(upload_to='coach_headshots')
    Coach_First_Name = models.CharField(max_length=25)
    Coach_Last_Name = models.CharField(max_length=25)
    Coach_Role = models.CharField(max_length=25, choices = coach_choices)
    programs = models.ForeignKey(
        to=Team, on_delete=models.CASCADE, related_name="team_coach",
    )

    def __str__(self):
        return f"[{self.Coach_First_Name}] [{self.Coach_Last_Name}]"