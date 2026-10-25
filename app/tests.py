from django.test import TestCase
from django.urls import reverse

from .models import Tarea


class TareaModelTest(TestCase):
    def test_str_devuelve_titulo(self):
        tarea = Tarea.objects.create(titulo="Estudiar CI/CD")
        self.assertEqual(str(tarea), "Estudiar CI/CD")

    def test_completada_por_defecto_es_false(self):
        tarea = Tarea.objects.create(titulo="Tarea nueva")
        self.assertFalse(tarea.completada)


class TareaViewsTest(TestCase):
    def test_lista_responde_200(self):
        respuesta = self.client.get(reverse("lista"))
        self.assertEqual(respuesta.status_code, 200)

    def test_crear_tarea(self):
        respuesta = self.client.post(reverse("lista"), {"titulo": "Configurar Docker"})
        self.assertRedirects(respuesta, reverse("lista"))
        self.assertEqual(Tarea.objects.count(), 1)

    def test_crear_tarea_vacia_no_guarda(self):
        self.client.post(reverse("lista"), {"titulo": ""})
        self.assertEqual(Tarea.objects.count(), 0)

    def test_alternar_tarea(self):
        tarea = Tarea.objects.create(titulo="Probar pipeline")
        self.client.post(reverse("alternar", args=[tarea.pk]))
        tarea.refresh_from_db()
        self.assertTrue(tarea.completada)

    def test_eliminar_tarea(self):
        tarea = Tarea.objects.create(titulo="Borrar")
        self.client.post(reverse("eliminar", args=[tarea.pk]))
        self.assertEqual(Tarea.objects.count(), 0)
