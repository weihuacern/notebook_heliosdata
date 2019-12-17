#! /bin/bash
printf "TS\t\tCPU\t\tMemory\t\tDisk\n"
end=$((SECONDS+3600))
while [ $SECONDS -lt $end ]; do
  TS=$(date -u | awk '{printf "%s/%s/%s %s\t\t", $6, $2, $3, $4}')
  CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%\t\t\n", $(NF-2)}')
  MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%\t\t", $3*100/$2}')
  DISK=$(df -h | awk '$NF=="/"{printf "%s\t\t", $5}')
  echo "$TS$CPU$MEMORY$DISK"
  sleep 30
done
