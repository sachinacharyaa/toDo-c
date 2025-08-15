from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'timestamps')
    list_filter = ('status', 'timestamps', 'owner')
    search_fields = ('title', 'description', 'owner__username')
    list_editable = ('status',)
    readonly_fields = ('timestamps',)
    ordering = ('-timestamps',)