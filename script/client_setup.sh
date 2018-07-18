#!/bin/bash

#Install python36 and related database packages
#https://janikarhunen.fi/how-to-install-python-3-6-1-on-centos-7.html
sudo yum update
sudo yum install vim
sudo yum install yum-utils
sudo yum install net-tools
sudo yum groupinstall development

sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
sudo yum install python36u

sudo yum install python36u-pip
sudo yum install python36u-devel

pip3.6 install names
sudo yum install gcc
sudo yum install freetds-devel
sudo yum install python36u-devel
pip3.6 install pymssql
pip3.6 install pymysql

#Setup network interface
while test $# -gt 0; do
    case "$1" in
        -h|--help)
            echo "options:"
            echo "-h, --help               show brief help"
            echo "-dev, --device=DEVICE    specify name of the revenue interface"
            echo "-ip, --ipaddr=IP         specify the ip for revenue interface"
            echo "-net, --netmask=NETMASK  specify the netmask for the revenue interface"
            exit 0
            ;;
        -dev)
            shift
            if test $# -gt 0; then
                export DEVICE=$1
            else
                echo "no interface name specified"
                exit 1
            fi
            shift
            ;;
        --device*)
            export DEVICE=`echo $1 | sed -e 's/^[^=]*=//g'`
            shift
            ;;
        -ip)
            shift
            if test $# -gt 0; then
                export IP=$1
            else
                echo "no ip addr specified"
                exit 1
            fi
            shift
            ;;
        --ipaddr*)
            export IP=`echo $1 | sed -e 's/^[^=]*=//g'`
            shift
            ;;
        -net)
            shift
            if test $# -gt 0; then
                export NETMASK=$1
            else
                echo "no output dir specified"
                exit 1
            fi
            shift
            ;;
        --netmask*)
            export NETMASK=`echo $1 | sed -e 's/^[^=]*=//g'`
            shift
            ;;
        *)
            break
            ;;
    esac
done

#echo $DEVICE
#echo $IP
#echo $NETMASK
#echo "${IP%.*}.0"

ifconfig $DEVICE $IP netmask $NETMASK
ifconfig $DEVICE down
ifconfig $DEVICE up
route del -net 192.168.7.0 netmask $NETMASK dev $DEVICE
route add -net "${IP%.*}.0" netmask $NETMASK dev $DEVICE
