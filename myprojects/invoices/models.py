from django.db import models

# Create your models here.
# invoices/models.py
from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    regular_hour_rate = models.DecimalField(max_digits=5, decimal_places=2, default=12.00)
    overtime_hour_rate = models.DecimalField(max_digits=5, decimal_places=2, default=18.00)
    week1_regular_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week1_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week2_regular_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week2_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week3_regular_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week3_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week4_regular_hours = models.DecimalField(max_digits=5, decimal_places=2)
    week4_overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)

    @property
    def total_hours(self):
        return (self.week1_regular_hours + self.week2_regular_hours +
                self.week3_regular_hours + self.week4_regular_hours)

    @property
    def total_overtime_hours(self):
        return (self.week1_overtime_hours + self.week2_overtime_hours +
                self.week3_overtime_hours + self.week4_overtime_hours)

    @property
    def total_regular_pay(self):
        return self.total_hours * self.regular_hour_rate

    @property
    def total_overtime_pay(self):
        return self.total_overtime_hours * self.overtime_hour_rate

    @property
    def total_pay(self):
        return self.total_regular_pay + self.total_overtime_pay