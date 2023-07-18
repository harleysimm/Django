from django.db import models
from django.urls import reverse
from core.settings import AUTH_USER_MODEL

class State(models.Model):

    name = models.CharField(max_length=20)
    color = models.CharField(max_length=6)
    is_Done = models.BooleanField()

    class Meta:
        ordering = ['name']

    def get_absoluted_url(self):
        return reverse('state', args=[str(self.id)])

    def __str__(self):
        return f"name: {self.name}, color:{self.color}, isDone:{self.is_Done}"
    
class Task(models.Model):
    titulo = models.CharField(max_length=100)
    due_task = models.DateField(("due_task"), auto_now=False, auto_now_add=False) #también puede ser vacío porque por defecto viene en False
    state = models.ForeignKey("State", on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    class Meta:
        ordering = ['due_task', 'titulo', 'user', 'state']

    def state_name(self):
        return self.state.name
        
    def get_absoluted_url(self):
        return reverse('tasks', args=[str(self.id)])

    def __str__(self):
        return f"due_task:{self.due_task}, titulo:{self.titulo}, user:{self.user}, state:{self.state}"
    
class Comments(models.Model):

    body = models.CharField(max_length=200)
    task = models.ForeignKey("Task", on_delete=models.CASCADE)

    class Meta:
        ordering = ['body', 'task']

    def task_titulo(self):
        return self.task.titulo

    def get_absoluted_url(self):
        return reverse('comments', args=[str(self.id)])
    def __str__(self):
        return f"body:{self.body}, task:{self.task}"


