<?php

/*
ip_waf()    设置黑白名单
            可以考虑设置静态界面
LOG_HTTP    日志开关
IP_WAF      防火墙开关

*/

$time=date('m_d_H_').(int)(date('i')/10);
$remote_ip = $_SERVER['REMOTE_ADDR'];
define('WAF_PATH','/var/www/html/my_waf/');
define('LOG_PATH','/tmp/waf/log/');
define('LOG_ALL_PATH','/tmp/waf/log_all/');
define('LOG_FILENAME',LOG_PATH."cap-".$remote_ip."-".$time.'.txt');
define('LOG_ALL_FILENAME',LOG_ALL_PATH."allcap-".$remote_ip."-".$time.'.txt');
define('LOG_HTTP',true);
define('IP_WAF',false);
define('ALL_RECORD',true);
define('DEBUG',true);

if(DEBUG){
    error_reporting(E_ERROR | E_WARNING | E_PARSE);
}

function waf()
    {
        if (!function_exists('getallheaders')) {
            function getallheaders() {
                foreach ($_SERVER as $name => $value) {
                    if (substr($name, 0, 5) == 'HTTP_')
                        $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
                }
                return $headers;
            }
        }
        $get = $_GET;
        $post = $_POST;
        $cookie = $_COOKIE;
        $header = getallheaders();
        $files = $_FILES;
        $ip = $_SERVER["REMOTE_ADDR"];
        $method = $_SERVER['REQUEST_METHOD'];
        $filepath = $_SERVER["SCRIPT_NAME"];
        //rewirte shell which uploaded by others, you can do more
        foreach ($_FILES as $key => $value) {
            $files[$key]['content'] = file_get_contents($_FILES[$key]['tmp_name']);
            file_put_contents($_FILES[$key]['tmp_name'], "virink");
        }
        unset($header['Accept']);//fix a bug
        $input = array("Get"=>$get, "Post"=>$post, "Cookie"=>$cookie, "File"=>$files, "Header"=>$header);
        //deal with
        $pattern = "select|insert|update|delete|union|into|load_file|outfile|dumpfile|sub|hex";
        $pattern .= "admin|file_put_contents|fwrite|curl|system|eval|assert";
        $pattern .="|passthru|exec|system|chroot|scandir|chgrp|chown|shell_exec|proc_open|proc_get_status|popen|ini_alter|ini_restore";
        $pattern .="|`|openlog|syslog|readlink|symlink|popepassthru|stream_socket_server|assert|pcntl_exec";
        $vpattern = explode("|",$pattern);
    //var_dump($vpattern);
	$bool = false;
	if(ALL_RECORD){
	    logging($input,LOG_ALL_FILENAME,false);
	}
        foreach ($input as $k => $v) {
            foreach($vpattern as $value){
                foreach ($v as $kk => $vv) {
                    if (preg_match( "/$value/i", $vv )){
                        $bool = true;
			if(DEBUG){
			    var_dump($value);
			    var_dump($vv);
			}
                        logging($input,LOG_FILENAME,true);
                        break;
                    }
                }
                if($bool) break;
            }
            if($bool) break;
        }
}


function logging($var,$filename,$isdie)
{
    file_put_contents($filename, "\n".date("m-d H:i:s")."  ".$_SERVER['REMOTE_ADDR']."\n".print_r($var, true), FILE_APPEND);
    $http_log = "\n".$_SERVER['REQUEST_METHOD']." ".$_SERVER['REQUEST_URI']." HTTP/1.1\n";
    foreach(getallheaders() as $key => $value){
       $http_log .=   $key.": ".$value."\n";
    }
    $is_first = true;
    $http_log .= "\n";
    foreach($_POST as $key => $value){
       if(!$is_first){ $http_log .= '&';}
       $http_log .= $key."=".$value;
       $is_first = false;
    }
    //echo $http_log;
    if(LOG_HTTP){file_put_contents($filename, $http_log,  FILE_APPEND);}
    if($isdie){
	echo 'I am waf';
        die();// die() or unset($_GET) or unset($_POST) or unset($_COOKIE);
    }
}

function ip_waf()
{
    $ip = $_SERVER['REMOTE_ADDR'];
    $white_ip_list = array('127.0.0.1');
    $black_ip_list = array('192.168.37.1');
    if(in_array($ip,$black_ip_list) || !in_array($ip,$white_ip_list))
	exit('403 forbidden');
}

waf();
if(IP_WAF){
    ip_waf();
}	
?>
