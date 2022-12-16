from datetime import timedelta, datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFit

import pytz


class Event(models.Model):
    title = models.CharField(_("Name"), max_length=30)
    attendees = models.ManyToManyField(
        "core.Profile",
        verbose_name=_("Attendees"),
        related_name="events",
        db_table="profiles_events",
        blank=True,
    )
    capacity = models.IntegerField(_("Capacity"), validators=[MinValueValidator(settings.MINIMUM_EVENT_CAPACITY)])
    date = models.DateField(_("Date"))
    time = models.TimeField(_("Time"))
    age_limit = models.IntegerField(_("Age limit"), validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    description = models.TextField(_("Description"))
    duration = models.DurationField(_("Duration"), default=timedelta(hours=2))
    photo = ProcessedImageField(
        verbose_name=_("Photo"),
        upload_to="event/photos/",
        null=True,
        blank=True,
        format="JPEG",
        options={"quality": 90},
        processors=[
            ResizeToFit(width=1920, height=1200, upscale=False),  # max-width
        ],
    )
    owner = models.ForeignKey(
        "core.Profile",
        verbose_name=_("Owner"),
        related_name="created_events",
        on_delete=models.CASCADE
    )
    interests = models.ManyToManyField(
        "core.Interest",
        verbose_name=_("Interests"),
        related_name="events",
        db_table="interests_events",
    )

    def clean(self):
        if datetime.combine(self.date, self.time, pytz.timezone(settings.TIME_ZONE)) <= datetime.now(tz=pytz.timezone(settings.TIME_ZONE)):
            raise ValidationError({"time": "Assigned date could not be earlier than current date."})

    def __str__(self):
        return self.title

    class Meta:
        db_table = "event"
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
