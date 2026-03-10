from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='goals')
    limit_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Teto de gastos
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('category', 'month', 'year')  # Uma meta por categoria por mes
        ordering = ['-year', '-month']

    def __str__(self):
        return f'{self.category.name} - {self.month}/{self.year}'
