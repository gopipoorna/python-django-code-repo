#!/usr/bin/env bash

cd /home/ubuntu/g2020wa15340

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

echo "install requirements.txt"
venv/bin/pip install -r /home/ubuntu/g2020wa15340/requirements.txt

echo "collecting all static files"
cd /home/ubuntu
venv/bin/python3 g2020wa15340/manage.py collectstatic
venv/bin/python3 g2020wa15340/manage.py makemigrations
venv/bin/python3 g2020wa15340/manage.py migrate

echo "Starting apache server"
systemctl start apache2
systemctl enable apache2

cd /home/ubuntu/

echo "Giving permissions"
cp configuration/django-apache.conf /etc/apache2/sites-available/
chown :www-data g2020wa15340/
chown :www-data g2020wa15340/media
chown :www-data g2020wa15340/media/*
chown :www-data g2020wa15340/media/profile_pics/*
chown :www-data g2020wa15340/static
chmod 755 $(pwd)
chown :www-data g2020wa15340/db.sqlite3
chmod 755 g2020wa15340/db.sqlite3
sudo a2ensite django-apache.conf
sudo systemctl reload apache2
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
sudo systemctl restart apache2

deactivate


