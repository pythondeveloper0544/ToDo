from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TaskForm
from.models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/home.html'
    ordering = ['completed']
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(author=self.request.user)
        return context


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/task_update.html'
    # fields = ['title', 'description', 'completed', 'deadline']
    success_url = reverse_lazy('tasks')


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'base/create.html'
    # fields = ['title', 'description', 'completed', 'deadline']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/delete.html'
    success_url = reverse_lazy('tasks')
