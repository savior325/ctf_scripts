gcc monitor2.c md5.c -o filemonitor
./filemonitor /var/www/html /tmp 可以跟多个目录


./filemonitor /tmp `find /var/www/html -type d -print | xargs echo` 
备份目录  当前目录下的bak  
./bak/var/www/html
./bak/tmp

---------------------------------------------------------------------------------------------------------
dir='/var/www/html'
rm -rf bak && mkdir bak && mkdir -p ./bak$dir && cp -a $dir/* ./bak$dir 
gcc monitor2.c md5.c -o filemonitor &&./filemonitor `find $dir -type d -print | xargs echo`