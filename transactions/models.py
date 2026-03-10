from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Transaction(models.Model):

    TYPE_CHOICES = [
        ('income', 'Receita'),
        ('expense', 'Despesa'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    title = models.CharField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='transactions')
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f'{self.title} - R$ {self.amount} ({self.get_type_display()})'
