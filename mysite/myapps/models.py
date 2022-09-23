from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_learner = models.BooleanField('Is Learner', default=False)
    is_recruiter = models.BooleanField('Is Recruiter', default=False)
    is_course = models.BooleanField('Is Course', default=False)
