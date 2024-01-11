
from django.db import models

class Restaurant1(models.Model):
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.date} - {self.time}"

class EmptyTables(models.Model):
    restaurant = models.ForeignKey(Restaurant1, on_delete=models.CASCADE, related_name='empty_tables')
    time_slot = models.TimeField()
    num_empty_tables_inside = models.IntegerField()
    num_empty_tables_outside = models.IntegerField()

    def __str__(self):
        return f"{self.restaurant.date} - {self.time_slot} - Inside: {self.num_empty_tables_inside}, Outside: {self.num_empty_tables_outside} empty tables"
