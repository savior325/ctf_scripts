#include "md5.h"
#include <errno.h>
#include <poll.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/inotify.h>
#include <unistd.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <sys/stat.h> 
#include <utime.h> 

#define READ_DATA_SIZE	1024
#define MD5_SIZE		16
#define MD5_STR_LEN		(MD5_SIZE * 2)


int Compute_file_md5(const char *file_path, char *md5_str)
{
	int i;
	int fd;
	int ret;
	unsigned char data[READ_DATA_SIZE];
	unsigned char md5_value[MD5_SIZE];
	MD5_CTX md5;

	fd = open(file_path, O_RDONLY);
	if (-1 == fd)
	{
		return -1;
	}

	// init md5
	MD5Init(&md5);

	while (1)
	{
		ret = read(fd, data, READ_DATA_SIZE);
		if (-1 == ret)
		{
			strcpy(md5_str,"directory");
			return -1;
		}

		MD5Update(&md5, data, ret);

		if (0 == ret || ret < READ_DATA_SIZE)
		{
			break;
		}
	}

	close(fd);

	MD5Final(&md5, md5_value);

	for(i = 0; i < MD5_SIZE; i++)
	{
		snprintf(md5_str + i*2, 2+1, "%02x", md5_value[i]);
	}
	md5_str[MD5_STR_LEN] = '\0'; // add end

	return 0;
}


int copyfilemodifytime(char *path,char *path2)  
{   
    struct stat       statbuf;  
    struct utimbuf   timebuf;  
  
    if (stat(path, &statbuf) == -1) {  
        printf("stat error for %s\n", path);  
    } else {  
        timebuf.modtime = statbuf.st_mtime;
        timebuf.actime = statbuf.st_atime;
        if (utime(path2, &timebuf) == -1)  
        printf("utime error for %s\n", path);  
    }     
  
    return 0;  
  
}  


int copyfile(char *path,char *path2){
    char buffer[1024];//设置缓冲区大小
    FILE *in,*out;//定义两个文件流，分别用于文件的读取和写入int len;
    if((in=fopen(path,"r"))==NULL){//打开源文件的文件流
        printf("源文件不存在，请检查路径输入是否存在！\n");
        return 1;
    }
    if((out=fopen(path2,"w"))==NULL){//打开目标文件的文件流
        printf("创建目标文件流失败！\n");
        return 1;
    }
    int len;//len为fread读到的字节长
    while((len=fread(buffer,1,1024,in))>0){//从源文件中读取数据并放到缓冲区中，第二个参数1也可以写成sizeof(char)
        fwrite(buffer,1,len,out);//将缓冲区的数据写到目标文件中memset(buffer，0，1024);
    }
    fclose(out);
    fclose(in);
    return 0;
}

unsigned long get_file_size(const char *path)  
{  
    unsigned long filesize = -1;      
    struct stat statbuff;  
    if(stat(path, &statbuff) < 0){  
        return filesize;  
    }else{  
        filesize = statbuff.st_size;  
    }  
    return filesize;  
}  

unsigned long get_file_modifytime(const char *path)  
{  
    unsigned long modifytime = -1;      
    struct stat statbuff;  
    if(stat(path, &statbuff) < 0){  
        return modifytime;  
    }else{  
        modifytime = statbuff.st_mtime;  
    }  
    return modifytime;  
}  


/* Read all available inotify events from the file descriptor 'fd'.
   wd is the table of watch descriptors for the directories in argv.
   argc is the length of wd and argv.
   argv is the list of watched directories.
   Entry 0 of wd and argv is unused. */

static void
handle_events(int fd, int *wd, int argc, char* argv[])
{
    /* Some systems cannot read integer variables if they are not
       properly aligned. On other systems, incorrect alignment may
       decrease performance. Hence, the buffer used for reading from
       the inotify file descriptor should have the same alignment as
       struct inotify_event. */

    char buf[4096]
        __attribute__ ((aligned(__alignof__(struct inotify_event))));
    const struct inotify_event *event;
    int i;
    ssize_t len;
    char *ptr;
    char filename[200];
    char lastfilename[200];
    char filetype[20];
    char tempstr[200];
    char bakfilemame[200];
    char tempstr2[200];
    time_t now;
    struct tm *tm_now;
    char    datetime[200];
    unsigned long modifytimefile;
    unsigned long modifytimebakfile;
    char md5_str1[MD5_STR_LEN + 1];
    char md5_str2[MD5_STR_LEN + 1];
    char operatemethod[100];

    time(&now);
    tm_now = localtime(&now);
    strftime(datetime, 200, "%Y-%m-%d %H:%M:%S %Z", tm_now);

    printf("======= %s ========\n", datetime);  
    //printf("================================================\n");

    /* Loop while events can be read from inotify file descriptor. */

    for (;;) {

        /* Read some events. */

        len = read(fd, buf, sizeof buf);
        if (len == -1 && errno != EAGAIN) {
            perror("read");
            exit(EXIT_FAILURE);
        }

        /* If the nonblocking read() found no events to read, then
           it returns -1 with errno set to EAGAIN. In that case,
           we exit the loop. */

        if (len <= 0)
            break;

        /* Loop over all events in the buffer */

        for (ptr = buf; ptr < buf + len;ptr += sizeof(struct inotify_event) + event->len) {
            event = (const struct inotify_event *) ptr;
            /* Print type of filesystem object */

            if (event->mask & IN_ISDIR)
                strcpy(filetype,"[directory]");
            else
                strcpy(filetype,"[file]");       

            /* Print the name of the watched directory */

			for (i = 1; i < argc; ++i) {
				if (wd[i] == event->wd) {
					/* printf("%s/", argv[i]); */
                    strcpy(filename,argv[i]);
                    strcat(filename,"/");
                    break;
                }
			}

            /* Print the name of the file */

            if (event->len){
                /* printf("%s", event->name); */
                strcat(filename,event->name);
            }

            /* Print event type */
            if (event->mask & IN_CREATE)
                strcpy(operatemethod,"CREATE");
            if (event->mask & IN_MOVED_TO)
                strcpy(operatemethod,"MOVED_IN"); 
            if (event->mask & IN_CLOSE_WRITE)
                strcpy(operatemethod,"CLOSE_WRITE"); 
            if (event->mask & IN_DELETE)
                strcpy(operatemethod,"DELETE");
			if (event->mask & IN_MOVED_FROM){
                strcpy(operatemethod,"MOVED_OUT");
				printf("MOVED_OUT %s \n",filename);
			}
            
            strcpy(bakfilemame,"./bak");
            strcat(bakfilemame,filename);
            modifytimefile=get_file_modifytime(filename);
            modifytimebakfile=get_file_modifytime(bakfilemame);
            strcpy(md5_str1,"");
            strcpy(md5_str2,"");
            Compute_file_md5(filename, md5_str1);
            Compute_file_md5(bakfilemame, md5_str2);
            //printf("filemd5 %s ,bakfilemd5 %s \n",md5_str1,md5_str2);
            //if (modifytimefile==modifytimebakfile && get_file_size(bakfilemame)==get_file_size(filename)){
            if (!strcmp(md5_str1,md5_str2)){
                    printf("%s%s %s ,与备份文件一致。\n",filetype,operatemethod,filename);
                }
            else{
                if (modifytimebakfile==-1){
                    printf("%s%s %s ,备份文件不存在，执行删除。\n",filetype,operatemethod,filename);
                    if( remove(filename) == 0 ){
                        printf("***Removed %s \n", filename);
                    }
                    else{
                        perror("remove");
						strcpy(tempstr2,"rm -rf ");
                        strcat(tempstr2,filename);
                        system(tempstr2);
                        printf("****use '%s'\n",tempstr2);
					}
                }
                else{
                    if ((event->mask & IN_CLOSE_WRITE)||(event->mask & IN_DELETE)||(event->mask & IN_MOVED_FROM)){
                        printf("%s%s %s,与备份文件不一致。执行覆盖。\n" ,filetype,operatemethod,filename);
                        if (copyfile(bakfilemame,filename)==0){
                            printf("覆盖成功,");
                            if (copyfilemodifytime(bakfilemame,filename)==0){
                                printf("复制修改时间成功\n");
                            }
                        }
                    }                        
                }
            }
            printf("--------------------------------------\n");
        }
    }
}

int
main(int argc, char* argv[])
{
    char buf;
    int fd, i, poll_num;
    int *wd;
    nfds_t nfds;
    struct pollfd fds[2];

    if (argc < 2) {
        printf("Usage: %s PATH [PATH ...]\n", argv[0]);
        exit(EXIT_FAILURE);
    }

    printf("Press ENTER key to terminate.\n");

    /* Create the file descriptor for accessing the inotify API */

    fd = inotify_init1(IN_NONBLOCK);
    if (fd == -1) {
        perror("inotify_init1");
        exit(EXIT_FAILURE);
    }

    /* Allocate memory for watch descriptors */

    wd = calloc(argc, sizeof(int));
    if (wd == NULL) {
        perror("calloc");
        exit(EXIT_FAILURE);
    }

    /* Mark directories for events
       - file was opened
       - file was closed */

    for (i = 1; i < argc; i++) {
        wd[i] = inotify_add_watch(fd, argv[i],
                                  IN_CREATE | IN_CLOSE_WRITE | IN_DELETE | IN_MOVED_TO | IN_MOVED_FROM );
        if (wd[i] == -1) {
            fprintf(stderr, "Cannot watch '%s'\n", argv[i]);
            perror("inotify_add_watch");
            exit(EXIT_FAILURE);
        }
    }

    /* Prepare for polling */

    nfds = 2;

    /* Console input */

    fds[0].fd = STDIN_FILENO;
    fds[0].events = POLLIN;

    /* Inotify input */

    fds[1].fd = fd;
    fds[1].events = POLLIN;

    /* Wait for events and/or terminal input */

    printf("Listening for events.\n");
    while (1) {
        poll_num = poll(fds, nfds, -1);
        if (poll_num == -1) {
            if (errno == EINTR)
                continue;
            perror("poll");
            exit(EXIT_FAILURE);
        }

        if (poll_num > 0) {

            if (fds[0].revents & POLLIN) {

                /* Console input is available. Empty stdin and quit */

                while (read(STDIN_FILENO, &buf, 1) > 0 && buf != '\n')
                    continue;
                break;
            }

            if (fds[1].revents & POLLIN) {

                /* Inotify events are available */

                handle_events(fd, wd, argc, argv);
            }
        }
    }

    printf("Listening for events stopped.\n");

    /* Close inotify file descriptor */

    close(fd);

    free(wd);
    exit(EXIT_SUCCESS);
}



