#!/bin/bash
echo "monitor service started" >> device.log
while true; do
cat deviceip.txt |  while read output
do
    ping -c 1 "$output" > /dev/null
    if [ $? -eq 0 ]; then
    echo "node $output is up"  >> device.log
    else
    echo "node $output is down" >> device.log
    fi
    sleep 5
done
done
