#!/usr/bin/env python3

import re
import boto3

file = open("/home/ubuntu/g2020wa15340/.env", "r+")
file2 = open("/tmp/public_ip.txt", "r+")
new_ip=file2.read()
val = file.read()
print(val)
pattern=re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
old_ip= (pattern.search(val)).group()
new_val = val.replace(old_ip, new_ip)
print(new_val)
file.close()
file2.close()


file3 = open("/home/ubuntu/g2020wa15340/.env", "w")
file3.write(new_val.strip())
file3.close()

ssm = boto3.client('ssm', region_name='us-east-1')

AccessKey = ssm.get_parameter(Name='/2020wa15340/AccessKey', WithDecryption=True)
AccessKeyId = ssm.get_parameter(Name='/2020wa15340/AccessKeyId', WithDecryption=True)
DjangoSecret = ssm.get_parameter(Name='/2020wa15340/blog_app_secret', WithDecryption=True)
DBHost = ssm.get_parameter(Name='/2020wa15340/DBHost', WithDecryption=True)
DBPass = ssm.get_parameter(Name='/2020wa15340/DBPass', WithDecryption=True)
EMAIL_USER = ssm.get_parameter(Name='/2020wa15340/EMAIL_USER', WithDecryption=True)
EMAIL_PASS = ssm.get_parameter(Name='/2020wa15340/EMAIL_PASS', WithDecryption=True)


AKV = f'AWS_ACCESS_KEY_ID={AccessKeyId["Parameter"]["Value"]}'
ASAK = f"AWS_SECRET_ACCESS_KEY={AccessKey['Parameter']['Value']}"
BS = f'SECRET={DjangoSecret["Parameter"]["Value"]}'
DH = f'DB_HOST={DBHost["Parameter"]["Value"]}'
DP = f"DB_PASS={DBPass['Parameter']['Value']}"
EU = f"EMAIL_USER={EMAIL_USER['Parameter']['Value']}"
EP = f"EMAIL_PASS={EMAIL_PASS['Parameter']['Value']}"

data = "\n"+AKV+"\n"+ASAK+"\n"+BS+"\n"+DH+"\n"+DP+"\n"+EU+"\n"+EP

file = open("/home/ubuntu/g2020wa15340/.env", "a")
file.write(data)
file.close()
