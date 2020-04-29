#!/bin/bash
 
downlink="https://hk.ap.speedtest.i3d.net.prod.hosts.ooklaserver.net:8080/download"
uplink="https://hk.ap.speedtest.i3d.net.prod.hosts.ooklaserver.net:8080/upload"
Process_quantity="64"

down(){
  for i in $(seq 1 $Process_quantity)
  do
    curl -o /dev/null $downlink &
  done
  curl -o /dev/null $downlink
}

up(){
    for i in $(seq 1 $Process_quantity)
    do
      curl $uplink -F "file=@/dev/zero" -X POST &
    done
    curl $uplink -F "file=@/dev/zero" -X POST
}

loopdown(){
while :;
do
    down
done
}

loopup(){
while :;
do
    up
done
}

loopdown&
loopup&
