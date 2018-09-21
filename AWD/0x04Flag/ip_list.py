ip_base_start='172.20.'
ip_base_end='.'
ip_list=[]
for i in range(101,137):
     for j in range(102,103):
        tmp_ip='http://'+ip_base_start+str(i)+ip_base_end+str(j)+',post,Elliot'
        ip_list.append(tmp_ip)
        print tmp_ip