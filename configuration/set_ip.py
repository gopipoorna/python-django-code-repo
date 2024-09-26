#!/usr/bin/env python3

import re
import os

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

os.remove("/home/ubuntu/g2020wa15340/.env")

file3 = open("/home/ubuntu/g2020wa15340/.env", "w")
file3.write(new_val.strip())
file3.close()
