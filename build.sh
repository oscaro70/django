pip install --upgrade pip
sed -i 's/\r//' requirements.txt
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate