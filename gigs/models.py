from datetime import datetime
from django.conf import settings
from django.db import models
from django.urls import reverse
from tunes.models import Setlist
from accounts.models import CustomUser

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=16, minute=0, second=0, microsecond=0)
    return start

def default_end_time():
    now = datetime.now()
    end = now.replace(hour=19, minute=0, second=0, microsecond=0)
    return end

def default_event_date():
    now = datetime.now()
    date = now.replace(hour=16, minute=0, second=0, microsecond=0)
    return date


class Venue(models.Model):
    name = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    website = models.URLField(max_length=255, blank=True)
    performer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("venue_detail", args=[str(self.id)])


class Gig(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField(blank=True, null=True, default=default_event_date, help_text='Write date/time in this format: yyyy-mm-dd hh-mm-ss')
    bandleader = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )
    location = models.ForeignKey(Venue, on_delete=models.PROTECT, blank=True, null=True)
    call_time = models.TimeField(blank=True, null=True)
    start_time = models.TimeField(default=default_start_time())
    end_time = models.TimeField(default=default_end_time())
    pay = models.IntegerField(default=0)
    setlist = models.ForeignKey(
        Setlist, on_delete=models.PROTECT, blank=True, null=True
    )
    personnel = models.ManyToManyField(CustomUser, related_name='gig_staff')
    acccepts = models.ManyToManyField(CustomUser, related_name='gig_accepts')
    declines = models.ManyToManyField(CustomUser, related_name='gig_declines')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("gig_detail", args=[str(self.id)])
