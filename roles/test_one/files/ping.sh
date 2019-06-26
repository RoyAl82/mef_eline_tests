#!/bin/bash

echo "Ping created VLANs in Hosts..."

int=`hostnamectl | grep "Static hostname:" |  cut -d: -f2`

declare -i INDEX=20 END=40

touch ping_results.txt

echo "*******Ping created VLANs in Hosts...*******" >> ping_results.txt

while [[ $INDEX -le $END ]]
do
    if [[ "$int" = " int02" ]] ; then
        echo "- Ping 4 times to VLAN 10.0.$INDEX.3: -" >> ping_results.txt
        ping 10.0.$INDEX.3 -c 4 | grep "received" >> ping_results.txt #FROM INT 02 TO INT 03
    else
        echo "- Ping 4 times to VLAN 10.0.$INDEX.2: -" >> ping_results.txt
        ping 10.0.$INDEX.2 -c 4 | grep "received" >> ping_results.txt #FROM INT 03 TO INT 02
    fi
    INDEX=$(($INDEX+1))
done

echo "*******Finished ping test on Hosts...*******" >> ping_results.txt
echo "Finished ping test on Hosts..."