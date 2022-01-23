from django.conf import settings
from django.db import models


class App(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    description = models.CharField(
        max_length=500,
    )
    planid = models.IntegerField(
        null=True,
        blank=True,
    )


class Plan(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    price = models.IntegerField(
        null=True,
        blank=True,
    )


class Subscription(models.Model):
    "Generated Model"
    planid = models.IntegerField()
    active = models.BooleanField()
