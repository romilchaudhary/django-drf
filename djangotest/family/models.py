from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Child(models.Model):
    name= models.CharField(max_length=100)
    parent_id = models.ForeignKey(Family, related_name="child_fields", on_delete = models.CASCADE)

    def __str__(self):
        return self.name
