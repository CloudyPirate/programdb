from django.db import models

# Create your models here.
from django.db import models
from mysite.models import TimeStampedModel
from django.utils import timezone
from programs.models import Team

# Create your models here.
class Player(TimeStampedModel):
    yearChoices = [
        ('FR',"Freshman"),
        ('SO', "Sophomore"),
        ('JR', "Junior"),
        ('SR', "Senior"),
    ]
    uniSizes = [
        ('S', "Small"),
        ('M', "Medium"),
        ('L', "Large"),
        ('XL', "Extra Large"),
    ]
    positionChoices = [
        ('A',"Attack"),
        ('M', "Midfield"),
        ('D', "Defense"),
        ('G', "Goalie"),
        ('LSM', "Long Stick Midfield"),
        ('SSDM', "Short Stick Defensive Midfield"),
        ("FOGO", "Face-off Specialist"),
    ]

    playerHeadshot = models.ImageField(upload_to='playerheadshots')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(default=timezone.now)
    player_position = models.CharField(max_length = 40, choices=positionChoices)
    player_year = models.CharField(max_length=8, choices=yearChoices)
    playerUni_size = models.CharField(max_length=10, choices=uniSizes)
    team = models.ForeignKey(
        to=Team, on_delete=models.CASCADE, related_name="player_team",
    )




    def __str__(self):
        return f'{self.first_name} {self.last_name} {str(self.player_year)} {self.playerUni_size}'
