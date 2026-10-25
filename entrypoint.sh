#!/bin/sh
set -e

echo "Esperando a PostgreSQL en ${DB_HOST}:${DB_PORT}..."
until python - <<'EOF'
import os, socket, sys
try:
    socket.create_connection((os.environ.get("DB_HOST", "db"), int(os.environ.get("DB_PORT", 5432))), timeout=2).close()
except OSError:
    sys.exit(1)
EOF
do
  sleep 2
done

echo "Aplicando migraciones..."
python manage.py migrate --noinput

exec "$@"
