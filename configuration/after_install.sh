#!/usr/bin/env bash

cd /home/ubuntu/python-django-code-repo/g2020wa15340

# activate virtual environment
python3 -m venv venv
source venv/bin/activate

echo "install requirements.txt"
pip install -r /home/ubuntu/python-django-code-repo/g2020wa15340/requirements.txt

echo "collecting all static files"
cd /home/ubuntu/python-django-code-repo
python3 g2020wa15340/manage.py collectstatic
python3 g2020wa15340/manage.py makemigrations
python3 g2020wa15340/manage.py migrate

echo "Starting apache server"
sudo systemctl start apache2
sudo systemctl enable apache2

cd /home/ubuntu/

echo "Giving permissions"
sudo cp python-django-code-repo/configuration/django-apache.conf /etc/apache2/sites-available/
sudo chown :www-data python-django-code-repo/
sudo chown :www-data python-django-code-repo/g2020wa15340
sudo chown :www-data python-django-code-repo/g2020wa15340/media
sudo chmod 755 $(pwd)
sudo chown :www-data python-django-code-repo/g2020wa15340/db.sqlite3
sudo chmod 755 python-django-code-repo/g2020wa15340/db.sqlite3
sudo a2ensite django-apache.conf
sudo systemctl reload apache2
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
sudo systemctl restart apache2

deactivate


