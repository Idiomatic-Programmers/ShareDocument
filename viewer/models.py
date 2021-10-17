from django.contrib.auth.models import User
from django.db import models
from hashid_field import HashidAutoField


class Document(models.Model):
    id = HashidAutoField(primary_key=True, min_length=4)
    name = models.CharField(max_length=100, verbose_name="Document name")
    document = models.FileField(verbose_name="Document", upload_to="document")

    uploaded_on = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name} ({self.id})"


class DocumentDiskUsage(models.Model):
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE)
    size = models.FloatField()
