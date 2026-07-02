from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100, verbose_name="название блюда")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    description = models.TextField(blank=True, verbose_name="оописание")

    def __str__(self):
        return self.name