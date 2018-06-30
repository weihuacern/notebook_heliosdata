#!/bin/bash
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

yum install net-tools
ifconfig $DEVICE $IP netmask $NETMASK
ifconfig $DEVICE down
ifconfig $DEVICE up
route add -net "${IP%.*}.0" netmask $NETMASK dev $DEVICE
