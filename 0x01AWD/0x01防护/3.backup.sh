#!/bin/bash
time=`/bin/date +%F-%H-%M-%S`
bak_file="/tmp/$time.tar.gz"
webdir="/opt/lampp/htdocs/"
tar zcvf $bak_file $webdir >/dev/null 2>&1 &

#在/etc/crontab添加
#crontab */5 * * * * /bin/bash /data/bak.sh
