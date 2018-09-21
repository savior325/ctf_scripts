[\*] Usage :  
        

```python
python PostShell_no_file.py [no_file_shell] [webshell]  
```

[\*] Explain :  
        

```
no_file_shell:  undead shell without using script tags <?..?>, which looks like php -r  
webshell:       new webshell filename, which ALREADY modified in undead.php by $file
```

  

[\*] ATTENTION :  
        ==DO modify the reverse IP and PORT!!!==   

利用已存在代码执行漏洞，在不上传文件的情况下，在服务器直接生成不死马进程，生成小马同时利用crontab反弹shell

1.修改不死马中反弹shell的ip和port  
2.将已知的可利用webshell写入webshell.txt  
3.将常规不死马的<?...?>标签去掉即可  
4.执行python .\PostShell_no_file.py .\undead_no_file.php conf.bak.php  
5.上传大马完成，收割  

p.s.如有时间，找另一个隐蔽位置上传备份MD5不死马  
