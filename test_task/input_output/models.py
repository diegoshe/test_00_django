from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class SomeData(models.Model):
    data = JSONField()