# Linux 掛載命令


## mount 查看已經掛載的設備

在Linux上面要使用一些設備需要自己掛載，比如光碟機之類的，就需要使用掛載命令把它掛載到/mnt下面

<!---more--->

```bash
# mount
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,relatime,seclabel)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
devtmpfs on /dev type devtmpfs (rw,nosuid,seclabel,size=231216k,nr_inodes=57804,mode=755)
.
.
.
/dev/sda1 on /boot type xfs (rw,relatime,seclabel,attr2,inode64,noquota)
tmpfs on /run/user/1000 type tmpfs (rw,nosuid,nodev,relatime,seclabel,size=48388k,mode=700,uid=1000,gid=1000)
```

## mount -a 自動掛載

上面查詢了系統掛載的文件，其中我們要操作的一般只有sda的地方，並不會動到/proc、/sys這些內存記憶體的檔案（沒有持有者）

```bash
# mount -a
# cat /etc/fstab

#
# /etc/fstab
# Created by anaconda on Sun Mar 26 00:04:18 2017
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/cl-root     /                       xfs     defaults        0 0
UUID=1920c627-4c4a-4ce9-a089-ea5e113f1eca /boot     
UUID=daf56b8e-477c-7qj0-jikb-5e15eaca3f1e /home
              xfs     defaults        0 0
/dev/mapper/cl-swap     swap                    swap    defaults        0 0
```

自動掛載是依據/etc/fstab這個設定檔的內容進行掛載，這個設定檔案裡面的內容會在開機的時候自動掛載，如果有`/proc`、`/sys`的話最好不要動。

自動掛載不要把隨身碟和光碟機也放進去，如果開機沒有讀取到這些設備，很可能會進不去系統。


## 掛載方式

mount [-t vfstype] [-o optlist] [device name] [mount position]

option:
- -t 文件系統（ext3、ext4、iso9660…etc）

- -o 特殊選項

```bash
[root@localhost cyberjun]# ./myshell.sh
bash: ./myshell.sh: 拒絕不符權限的操作
[root@localhost cyberjun]# chmod 755 myshell.sh
[root@localhost cyberjun]# chown cyberjun:cyberjun myshell.sh
[root@localhost cyberjun]# ./myshell.sh
My shell work fine
[root@localhost cyberjun]#
```
