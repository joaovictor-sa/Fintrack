from django.contrib import admin
from . import models


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount')
    search_fields = ('title', 'category')


admin.site.register(models.Transaction, TransactionAdmin)
