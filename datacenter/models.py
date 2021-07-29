from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f"{self.owner_name} (inactive)"


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )
    
    def get_duration(self):
        if self.leaved_at:
            duration = self.leaved_at - self.entered_at
        else:
            duration = localtime() - localtime(self.entered_at)
        return duration

    def is_long(self, minutes=60):
        if self.get_duration().total_seconds() > minutes * 60:
            return True
        return False
    
    @staticmethod    
    def format_duration(duration_in_seconds):
        duration_in_hours, reminder = divmod(duration_in_seconds, 60*60)
        duration_in_minutes, _ = divmod(reminder, 60)
        return f"{duration_in_hours:02.0f}:{duration_in_minutes:02.0f}"
