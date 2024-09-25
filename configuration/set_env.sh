#!/usr/bin/env bash

# Grab an IMDSv2 token
TOKEN=`curl -s -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`

export PUBLIC_IP_EC2=$(curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4)

echo "IP from export = $PUBLIC_IP_EC2"