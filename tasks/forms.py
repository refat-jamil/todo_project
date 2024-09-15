from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task']
        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',  # Bootstrap class for input fields
                'placeholder': 'Enter task here'  # Optional placeholder text
            })
        }
