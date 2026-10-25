from django import forms

from .models import Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["titulo"]
        widgets = {
            "titulo": forms.TextInput(
                attrs={"placeholder": "Nueva tarea...", "autofocus": True}
            )
        }
