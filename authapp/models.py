from django.contrib.auth.models import User
from django.db import models


class LabUser(User):
    position = models.CharField(verbose_name='Должность', max_length=100, blank=True)
