#!/bin/bash
PATH=/bin:/sbin:/usr/bin:/usr/sbin/:/usr/local/bin:/usr/local/sbin:~/bin
s=10
touch /tmp/abc
while [ "$s" != "0" ]
do
find /tmp/test -type f -newer abc -print0 | xargs -0 rm -rf {}
#find /tmp/test -type f -newer abc | xargs
echo "====================================" 
sleep 2
done
