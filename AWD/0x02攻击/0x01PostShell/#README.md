利用已存在的webshell（如RCE），批量上传不死马并自动访问，生成小马同时利用crontab反弹shell

1.修改不死马中反弹shell的ip和port
2.在PostShell.py中修改upload_file、服务器大马路径shellpath、生成小马路径webshell
4.将已知的可利用webshell写入webshell.txt
5.执行python PostShell.py
6.上传大马完成，收割


7.如有时间，找另一个隐蔽位置上传备份MD5不死马