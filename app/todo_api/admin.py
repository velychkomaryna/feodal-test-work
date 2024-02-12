from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "description",
        "completed",
        "created",
        "user",
        "category",
        "deadline",
    )
    search_fields = ("id",)
    readonly_fields = ("created",)
    ordering = ("id",)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Task, TaskAdmin)
