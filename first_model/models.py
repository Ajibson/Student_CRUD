from django.db import models
from django.utils import timezone


class students(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=120)
    level = models.PositiveIntegerField()
    date_admitted = models.DateField(default=timezone.now)#timezone.now will automatically fill the datefield for us as today's date if we left it with no data
    active = models.BooleanField()
    reg_no = models.CharField(max_length = 15)
    # The method defined below will let us see the students name when any student instance is called
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'students'

    