<?php
error_reporting(E_ALL^E_NOTICE^E_WARNING);

function StopAttack($StrFiltKey,$StrFiltValue,$ArrFiltReq){  

	if(is_array($StrFiltValue))
	{
    $StrFiltValue=implode($StrFiltValue);
	}  
	if (preg_match("/".$ArrFiltReq."/is",$StrFiltValue)==1){   
		//slog("<br><br>操作IP: ".$_SERVER["REMOTE_ADDR"]."<br>操作时间: ".strftime("%Y-%m-%d %H:%M:%S")."<br>操作页面:".$_SERVER["PHP_SELF"]."<br>提交方式: ".$_SERVER["REQUEST_METHOD"]."<br>提交参数: ".$StrFiltKey."<br>提交数据: ".$StrFiltValue);
		global $logfilename, $logstr,$data;
		file_put_contents($logfilename.".txt", "***".$logstr."\r\n", FILE_APPEND);
		file_put_contents($logfilename."-post.txt", "***".$logstr."|".$data."\r\n", FILE_APPEND);
		die("<!DOCTYPE HTML PUBLIC '-//IETF//DTD HTML 2.0//EN'><html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>");
	}
}


$logfilename='/tmp/log';
$getfilter="\=|flag|O:4:|array_map|z0|\#|\;|-|\&|\||'|\"|and|like|script|EXEC|UNION|SELECT|UPDATE|INSERT|INTO|VALUES|SELECT|DELETE|FROM|CREATE|ALTER|DROP|TRUNCATE|TABLE|DATABASE|\(|\)|php|eval|assert\?";
$postfilter="<\\?|flag|O:4:|array_map|z0|\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)|define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|fpopen|open|alert|showmodaldialog";
$cookiefilter="<\\?|O:4:|array_map|z0|\\b(and|or)\\b.{1,6}?(=|>|<|\\bin\\b|\\blike\\b)|\\/\\*.+?\\*\\/|<\\s*script\\b|\\bEXEC\\b|UNION.+?SELECT|UPDATE.+?SET|INSERT\\s+INTO.+?VALUES|(SELECT|DELETE).+?FROM|(CREATE|ALTER|DROP|TRUNCATE)\\s+(TABLE|DATABASE)";
$cookiefilter=$postfilter;
$URLFilter="\\/(attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)\\/.*ph.*";
///(attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)/(\\w+).(php|jsp)

$ip4=$_SERVER['REMOTE_ADDR'];
$pattern = '/^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)/';
preg_match($pattern, $ip4, $matches, PREG_OFFSET_CAPTURE);
$ip3=$matches[0][0];


$data = file_get_contents('php://input'); 
$logstr="";
$logstr=date('y-m-d_h:i:s',time())."|".$_SERVER['REMOTE_ADDR']."|".$_SERVER['REQUEST_METHOD']."|".'http://'.$_SERVER['HTTP_HOST'].$_SERVER['REQUEST_URI']."|".$_SERVER['HTTP_USER_AGENT'];

$_SERVER['HTTP_USER_AGENT']="";

$ipallow=array("10.10.1.47");

if(in_array($ip3,$ipallow) or in_array($ip4,$ipallow)){

}
else
{
  if (1==1){  //启动开关
  	
  	StopAttack("UrlFilter",$_SERVER['REQUEST_URI'],$URLFilter);
  	
		foreach($_GET as $key=>$value){
			if (strlen($value)>7){
				//die("<!DOCTYPE HTML PUBLIC '-//IETF//DTD HTML 2.0//EN'><html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>");
			}
			else{
			}
			StopAttack($key,$value,$getfilter);
		}

		foreach($_POST as $key=>$value){ 
			if (strlen($value)>15){
				//die("<!DOCTYPE HTML PUBLIC '-//IETF//DTD HTML 2.0//EN'><html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL was not found on this server.</p></body></html>");
			}
			else{
			}
			StopAttack($key,$value,$postfilter);
		}
		
		foreach($_COOKIE as $key=>$value){ 
	    StopAttack($key,$value,$cookiefilter);
		}
		
		if ($data<>""){
			StopAttack("PostDataFilter",$data,$postfilter);
		}
	}
}

file_put_contents($logfilename.".txt", $logstr."\r\n", FILE_APPEND);
file_put_contents($logfilename."-post.txt", $logstr."|".$data."\r\n", FILE_APPEND);

?>
