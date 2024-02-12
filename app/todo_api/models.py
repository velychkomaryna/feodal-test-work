from django.db import models
from django.db.models.functions import Now
from user.models import User


class Task(models.Model):

    # if we have a fixed list of categories we can use instead of other class
    WORK = 0
    LIFE = 1
    EDUCATION = 2
    CATEGORY_CHOICES = ((WORK, "Work"), (LIFE, "Life"), (EDUCATION, "Education"))

    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.IntegerField(choices=CATEGORY_CHOICES, blank=True)
    created = models.DateTimeField(db_default=Now())
    deadline = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.description
