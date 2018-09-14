#!/bin/sh
tmpDir="demo.php"
while true
do
  if [ ! -d $tmpDir ]; then
    rm -f $tmpDir & mkdir $tmpDir 2>/dev/null
  fi
sleep 0.02
done
