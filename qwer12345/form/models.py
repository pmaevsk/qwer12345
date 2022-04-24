from django.db.models import JSONField
from django.db import models


class MyForm(models.Model):
    metadata = JSONField()
