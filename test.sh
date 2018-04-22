#!/bin/bash 
# Prerequisite packages Installation
#yum clean all
#yum -y install wget openssl

# checking standalone RabbitMQ installed or not

ip() {

echo "ip of this machine is 180.179.47.227"
}

CLUSTER_SETUP() {

echo "calling function inside function"
ip 
}


CLUSTER_SETUP

