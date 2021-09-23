from django.db import models
from django.utils import timezone


class Cohort(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date created")

    def __str__(self):
        return self.name


class Native(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to="native_images/")
    cohort = models.ForeignKey(Cohort, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.first_name + " " + self.last_name


class Thought(models.Model):
    thought_text = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now())
    native = models.OneToOneField(Native, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.thought_text[:50]
