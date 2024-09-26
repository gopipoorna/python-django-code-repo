#!/usr/bin/env bash

# # clean codedeploy-agent files for a fresh install
# sudo rm -rf /home/ubuntu/instal
# cd /home/ubuntu/
# sudo rm -rf blog-app
# sudo mkdir -p blog-app
# cd blog-app/


# # install CodeDeploy agent
# sudo apt-get -y update
# sudo apt-get -y install ruby
# sudo apt-get -y install wget
# wget https://aws-codedeploy-us-east-1.s3.amazonaws.com/latest/install
# sudo chmod +x ./install 
# sudo ./install auto

# update os & install python3, apache2 and some important libraries
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3 python3-dev python3-pip python3-venv git apache2 apache2-utils ssl-cert libapache2-mod-wsgi-py3 default-libmysqlclient-dev build-essential pkg-config
pip install --user --upgrade virtualenv

# Grab an IMDSv2 token
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`

curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4 > /tmp/public_ip.txt

sudo chmod 777 /tmp/public_ip.txt

cat /tmp/public_ip.txt

sudo chmod 777 /home/ubuntu/g2020wa15340/.env

sudo python3 /home/ubuntu/configuration/set_ip.py