from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TareaForm
from .models import Tarea


def lista(request):
    if request.method == "POST":
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = TareaForm()
    tareas = Tarea.objects.all()
    return render(request, "app/lista.html", {"tareas": tareas, "form": form})


@require_POST
def alternar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save()
    return redirect("lista")


@require_POST
def eliminar(request, pk):
    get_object_or_404(Tarea, pk=pk).delete()
    return redirect("lista")
