#!/bin/bash

int=`hostnamectl | grep "Static hostname:" |  cut -d: -f2`

while true
do
if [ $x -le 40 ] && [ "$int" =  " int02" ] ; then
  ping 10.0.x.3 -c 4 | grep "received" > ping_results.txt #FROM INT 02 TO INT 03
else
  ping 10.0.$x.2 -c 4 | grep "received" > ping_results.txt #FROM INT 03 TO INT 02
fi
x=$((x+1))

if [ $x -gt 40 ] ; then
  break
fi
done
