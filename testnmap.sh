#!/bin/bash
ip=`ifconfig wlo1 | awk '/inet / {print $2}'`
mask=`ifconfig wlo1 | awk '/mask / {print $4}'`

#s=`ipcalc -p $ip $mask`

cidr=`ipcalc $ip $mask | awk '/Netmask: / {print $4}'`

#nmap -T4 -v -F -O -A --open $ip/$cidr -oX /home/leroidubid/Desktop/test.xml
rm /home/leroidubid/Desktop/test.xml
nmap -sn $ip/$cidr -oX /home/leroidubid/Desktop/test.xml

