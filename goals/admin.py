from django.contrib import admin
from . import models


class GoalAdmin(admin.ModelAdmin):
    list_display = ('category', 'description',)
    search_fields = ('category',)


admin.site.register(models.Goal, GoalAdmin)
