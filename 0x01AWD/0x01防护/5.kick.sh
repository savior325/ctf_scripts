#!/bin/sh
 for i in {0..20};do
  if [ $i -ne 1 ]
   then 
    pkill -kill -t pts/$i
  fi
 done
