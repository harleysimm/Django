from django.contrib import admin

from tasks.models import Task, State, Comments

class StateAdmin(admin.ModelAdmin):
    list_display = ('color', 'name')
    list_filter = ('color', 'name')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('due_task', 'titulo', 'user', 'state_name')
    list_filter = ('due_task', 'titulo', 'user', 'state')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('body', 'task_titulo')
    search_fields = ('body', 'task')

admin.site.register(Task, TaskAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Comments, CommentsAdmin)

