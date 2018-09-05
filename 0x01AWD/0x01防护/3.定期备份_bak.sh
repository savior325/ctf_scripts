#!/bin/bash
time=`/bin/date +%F-%H-%M-%S`
bak_file="/data/backup/$time.tar.gz"
webdir="/data/www/"
tar zcvf $bak_file $webdir >/dev/null 2>&1 &

#在/etc/crontab添加
#crontab 30 * * * * /bin/bash /data/bak.sh
