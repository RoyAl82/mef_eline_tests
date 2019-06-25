#! /bin/bash
echo "Start creating the VLAN."

vconfig add $1 $2 up

echo "Start VLAN Configuration."

ifconfig $1.$2 10.0.$2.$3/24 up

echo "End Script"