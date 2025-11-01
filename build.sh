set -o errexit  # Sale del script si hay un error

# Instalar las dependencias
pip install --no-cache-dir -r requirements.txt

# Recopilar los archivos estáticos de Django
python manage.py collectstatic --noinput

# Aplicar las migraciones a la base de datos
python manage.py migrate --noinput

# Ejecutar el servidor de Django o Gunicorn (si es necesario)
# gunicorn backend.wsgi:application
