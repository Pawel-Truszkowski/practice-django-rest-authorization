from django.db import models
from django.contrib.auth.models import User



class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')

    def __str__(self):
        return f"{self.title} (owner: {self.owner.username})"
