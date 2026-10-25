# Gestor de Tareas — Django + PostgreSQL + CI/CD

Proyecto Django sencillo (CRUD de tareas) para practicar un flujo CI/CD con GitHub Actions y Docker.

## Estructura
- `manage.py`, `project/` (configuración), `app/` (modelo, vistas, plantillas y tests)
- `requirements.txt`, `Dockerfile`, `entrypoint.sh`, `docker-compose.yml`
- `.github/workflows/ci.yml` (test → build → deploy simulado)
- `deploy-notes.md` (pasos del despliegue simulado)

## Ejecutar con Docker
```bash
docker compose up --build
```
Abrir http://localhost:8000/

## Ejecutar tests localmente
Con PostgreSQL disponible (variables `DB_*`):
```bash
pip install -r requirements.txt
python manage.py test
```
Prueba rápida sin PostgreSQL (solo local):
```bash
DB_ENGINE=sqlite python manage.py test
```

## Crear superusuario (opcional)
```bash
docker compose exec web python manage.py createsuperuser
```
Panel de administración: http://localhost:8000/admin/
