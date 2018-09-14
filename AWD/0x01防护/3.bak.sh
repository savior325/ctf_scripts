#!/bin/bash
time=`/bin/date +%F_%H.%M.%S`
bak_file="/tmp/$time.tar.gz"
webdir="/opt/lampp/htdocs/"
tar zcvf $bak_file $webdir >/dev/null 2>&1 &

# chmod +x /tmp/bak.sh
# echo '*/10 * * * * /tmp/bak.sh' > /tmp/1
# crontab /tmp/1
