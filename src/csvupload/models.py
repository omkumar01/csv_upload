from django.db import models

class Food_index(models.Model):
    u_id = models.IntegerField(unique=True)
    u_name = models.CharField(max_length=50)
    batch_id = models.CharField(max_length=50)
    supplier = models.CharField(max_length=50)
    event_type = models.CharField(max_length=50)
    food_category = models.CharField(max_length=50)
    food_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.u_name}"