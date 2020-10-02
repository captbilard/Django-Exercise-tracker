from datetime import date

from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username

    def count(self):
        total_exercises = self.objects.get(username=self.username).entries.count()
        return total_exercises


class Exercise(models.Model):
    username = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='entries')
    description = models.CharField(max_length=100)
    duration = models.DurationField()
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.username
