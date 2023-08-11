from django.db import models

# Create your models here.
class Restraunt(models.Model):
    app_label = "restraunts"
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=50)