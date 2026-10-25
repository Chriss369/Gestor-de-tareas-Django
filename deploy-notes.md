# deploy-notes.md — Despliegue simulado

Despliegue simulado del proyecto Django en una carpeta externa, usando la imagen generada por GitHub Actions.

## Requisitos
- Docker y Docker Compose instalados
- Acceso al repositorio de GitHub

## Pasos
1. **Descargar el artefacto**: en GitHub → Actions → última ejecución exitosa → sección *Artifacts* → descargar `docker-image`. Descomprimir para obtener `django-app.tar`.
2. **Crear carpeta externa**:
   ```bash
   mkdir ~/deploy-django && cd ~/deploy-django
   ```
3. **Copiar archivos**: colocar aquí `django-app.tar` y `docker-compose.yml` (copiado del repositorio).
4. **Cargar la imagen**:
   ```bash
   docker load -i django-app.tar
   ```
5. **Levantar los servicios**:
   ```bash
   docker compose up -d
   docker compose ps
   ```
6. **Validar en el navegador**: abrir `http://localhost:8000/` (y `/admin/` si aplica).
7. **Ver logs si algo falla**:
   ```bash
   docker compose logs web
   ```
8. **Detener y limpiar**:
   ```bash
   docker compose down        # conserva datos
   docker compose down -v     # borra también el volumen de PostgreSQL
   ```

## Evidencias a capturar
- Artefacto `docker-image` en GitHub Actions
- Salida de `docker compose ps` con `web` y `db` en estado *running/healthy*
- Navegador mostrando la aplicación en `localhost:8000`
