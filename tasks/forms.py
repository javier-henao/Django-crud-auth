from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'important': '¿Importante?',
        }
        widgets={
            'title': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Escriba el título de la tarea'}),
            'description': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Escriba una descripción para la tarea'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto mb-3'}),
        }
