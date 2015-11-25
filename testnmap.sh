#!/bin/bash
ip=`ifconfig wlo1 | awk '/inet / {print $2}'`
mask=`ifconfig wlo1 | awk '/mask / {print $4}'`
cidr=`ipcalc $ip $mask | awk '/Netmask: / {print $4}'`

nmap -sn $ip/$cidr -oX ./testfiles/test.xml

