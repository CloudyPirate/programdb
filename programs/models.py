from django.db import models
from mysite.models import TimeStampedModel
from django.utils import timezone
# Create your models here.

class Program(TimeStampedModel):
    key = models.CharField(
        max_length=5, help_text="Short Key for identifying program"
    )
    programImage = models.ImageField(upload_to="programimages")
    name = models.CharField(max_length=255, help_text="Program's Full Name")
    description = models.TextField(blank=True, null=True)
    program_active = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["key"], name="program_key"),
        ]

    def __str__(self):
        return f"[{self.name}] {self.key}"

class Team(TimeStampedModel):
    name = models.CharField(max_length=255, help_text="Name of Team inside of Program Varsity, JV, U14A,U14B etc")
    description = models.TextField(blank=True, null=True)
    practice_start_date = models.DateField(default=timezone.now)
    practice_end_date = models.DateField(default=timezone.now)
    practice_location = models.CharField(max_length=100)
    programs = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="teams")

    def __str__(self):
        return f"[{self.programs.key}-{self.id}] {self.name}"