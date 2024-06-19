from django.db import models
from django.contrib.auth.models import User

class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    downloads = models.IntegerField(default=0)
    emails_sent = models.IntegerField(default=0)

    def __str__(self):
        return self.title








