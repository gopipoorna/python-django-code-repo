#!/usr/bin/env bash

cd /home/ubuntu/g2020wa15340

# activate virtual environment
sudo python3 -m venv venv
source venv/bin/activate

echo "install requirements.txt"
sudo venv/bin/pip install -r /home/ubuntu/g2020wa15340/requirements.txt

echo "collecting all static files"
sudo venv/bin/python3 /home/ubuntu/g2020wa15340/manage.py collectstatic
sudo venv/bin/python3 /home/ubuntu/g2020wa15340/manage.py makemigrations
sudo venv/bin/python3 /home/ubuntu/g2020wa15340/manage.py migrate

echo "Starting apache server"
sudo systemctl start apache2
sudo systemctl enable apache2

cd /home/ubuntu/

echo "Giving permissions"
sudo cp configuration/django-apache.conf /etc/apache2/sites-available/
# sudo chown :www-data g2020wa15340/
# sudo chown :www-data g2020wa15340/media
# sudo chown :www-data g2020wa15340/media/*
# sudo chown :www-data g2020wa15340/media/profile_pics/*
# sudo chown :www-data g2020wa15340/static
# sudo chown :www-data /home/ubuntu
sudo chown :www-data /home/ubuntu/g2020wa15340 -R
sudo chown :www-data /home/ubuntu/g2020wa15340/static/*
sudo chmod -R 777 /home/ubuntu/g2020wa15340/static
sudo chown :www-data /home/ubuntu/g2020wa15340/media -R
sudo chmod -R 777 /home/ubuntu/g2020wa15340/media
sudo chmod 755 $(pwd)
sudo chown :www-data g2020wa15340/db.sqlite3
sudo chmod 755 g2020wa15340/db.sqlite3
sudo a2ensite django-apache.conf
sudo systemctl reload apache2
sudo a2dissite 000-default.conf
sudo systemctl reload apache2
sudo systemctl restart apache2

deactivate