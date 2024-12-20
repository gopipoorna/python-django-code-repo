#!/usr/bin/env bash

#installing cloudwatch agent to monitor the website logs and infrastructure

sudo wget https://amazoncloudwatch-agent-us-east-1.s3.us-east-1.amazonaws.com/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i -E amazon-cloudwatch-agent.deb
sudo mv /home/ubuntu/configuration/config.json /opt/aws/amazon-cloudwatch-agent/bin/
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json

# Setting up monitors to monitor instance usage of CPU, Memory and Disk

# Grab an IMDSv2 token
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`

instance_id=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)

aws cloudwatch put-metric-alarm --alarm-name $instance_id"_Blog_Server_HighCPUUtilization" --comparison-operator "GreaterThanThreshold" --namespace "AWS/EC2" --metric-name "CPUUtilization" --dimensions Name="InstanceId",Value="$instance_id" --threshold 80 --period 60 --evaluation-periods 2 --alarm-description $instance_id" CPU usage exceeds 80%" --alarm-actions "arn:aws:sns:us-east-1:572678256663:Blog_Prod_App_Notifications" --unit Percent --statistic Average --region us-east-1

aws cloudwatch put-metric-alarm --alarm-name $instance_id"_Blog_Server_HighDiskUtilization" --comparison-operator "GreaterThanThreshold" --namespace "CWAgent" --metric-name "disk_used_percent" --dimensions Name="InstanceId",Value="$instance_id" --threshold 90 --period 60 --evaluation-periods 2 --alarm-description $instance_id" Disk usage exceeds 90%"  --alarm-actions "arn:aws:sns:us-east-1:572678256663:Blog_Prod_App_Notifications" --unit Percent --statistic Average --region us-east-1

aws cloudwatch put-metric-alarm --alarm-name $instance_id"_Blog_Server_HighMemoryUtilization" --comparison-operator "GreaterThanThreshold" --namespace "CWAgent" --metric-name "mem_used_percent" --dimensions Name="InstanceId",Value="$instance_id"  --threshold 85 --period 60 --evaluation-periods 2 --alarm-description $instance_id" Memory usage is above 85%" --alarm-actions "arn:aws:sns:us-east-1:572678256663:Blog_Prod_App_Notifications" --unit Percent --statistic Average --region us-east-1

cd /home/ubuntu/g2020wa15340

# activate virtual environment
sudo python3 -m venv venv
source venv/bin/activate

echo "install requirements.txt"
sudo venv/bin/pip install -r /home/ubuntu/g2020wa15340/requirements.txt

sudo chmod 777 /home/ubuntu/g2020wa15340/.env

python3 /home/ubuntu/configuration/set_up_conf.py

echo "collecting all static files"
sudo venv/bin/python3 /home/ubuntu/g2020wa15340/manage.py collectstatic --noinput
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