from django.db import models


class Cohort(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField("Date created")

    def __str__(self):
        return self.name, self.description


class Native(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    image = models.ImageField(default="", upload_to="templates/native_images/")
    cohort = models.OneToOneField(Cohort, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
