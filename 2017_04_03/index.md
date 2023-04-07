# Linux 文件搜索指令


不像是Windows之類的GUI畫面都有搜索的功能，Linux的搜索命令非常的強大，這些搜索命令也比較多，至少功能比Windows強大了不知道多少。

# locate 文件搜索

locate和find搜索的最大差別就是，它的搜索速度比find快了很多，find會把範圍之內的所有文件都搜索一次，如果find搜索的範圍設定的很大的話，這會是一個非常耗費資源的命令。

```bash
[root@localhost ~]# locate install.log
/root/install.log
/root/install.log.syslog
[root@localhost ~]# touch G-3Gumdam.plist
[root@localhost ~]# locate G-3Gumdam.plist
## 搜不到任何檔案
[root@localhost ~]# updatedb ## 強制更新locate的資料庫
[root@localhost ~]# locate G-3Gundam.plist
/Users/Gumdam/G-3Gumdam.plist
```

`locate`速度比較快，因為它只有搜尋后台數據庫的文件，後台數據庫又叫内容管理系统Content Manage System（简称CMS），這個數據庫一般會一天更新一次，在Linux裡面它的數據庫文件就在`/var/lib/mlocate`裡面（Linux的版本不一樣，數據庫的名字也可能會不同），若要強制更新只要運行`updatedb`即可。

`locate`的功能比較差，只能使用文件名搜索，相對於`find`的功能就好了很多可以用大小、名字、使用者去做搜索。

有時候`locate`還是查不到檔案的話有可能是locate的搜尋設定的問題，在Linux裡面設定的檔案都放在`/etc`目錄下面，而`locate`的設定檔就在`/etc/updatedb.conf`，而MacOS在`/etc/locate.rc`如下：

```bash
[root@localhost ~]# vi /etc/locate.rc  
# /etc/locate.rc -  command script for updatedb(8)
#
# $FreeBSD: src/usr.bin/locate/locate/locate.rc,v 1.9 2005/08/22 08:22:48 cperc$

#
# All commented values are the defaults
#
# temp directory
#TMPDIR="/tmp"

# the actual database
#FCODES="/var/db/locate.database"

# directories to be put in the database
#SEARCHPATHS="/"

# directories unwanted in output
#PRUNEPATHS="/tmp /var/tmp"

# the actual database
#FCODES="/var/db/locate.database"

# directories to be put in the database
#SEARCHPATHS="/"

# directories unwanted in output
#PRUNEPATHS="/tmp /var/tmp"

# filesystems allowed. Beware: a non-listed filesystem will be pruned
# and if the SEARCHPATHS starts in such a filesystem locate will build
# an empty database.
#
# be careful if you add 'nfs'
#FILESYSTEMS="hfs ufs"
```

```bash
[root@localhost ~]# locate swtag.log ## 搜索/tmp下的檔案
##搜尋不到任何文件
```

如果按照上面的規則來看我的`/tmp`目錄下的檔案是不會被搜索的如果我隨便搜索一個`/tmp`是不會被查詢的，如果我要搜索`/tmp`下面的檔案，我就必須修改設定檔



# whereis、which 搜索系統命令介紹

whereis和which這兩個命令只能尋找系統命令的資訊，並不能尋找其他的外裝命令，比如我搜索`pandoc`、`npm`、`git`、`pip3`、`brew`、`macport`就不行使用，有些Linux查不到shell內建的指令例如：cd、bg、echo。

```bash
[root@localhost ~]# which npm #搜索一個外裝指令
# 搜不到任何東西
```


##  whereis 搜索命令所在位置以及幫助文檔

whereis [command name]

選項：

- `-b` 只查找命令位置
- `-m` 只查找man的幫助文檔位置


```bash
whereis  ls
ls: /bin/ls /usr/share/man/manl/ls.l.gz /usr/share/man/manlp/ls.lp.gz
```

## which 搜索命令（有別名會顯示）

[root@localhost ~]# which [command name]

```bash
[root@localhost ~]# which ls
alias ls='ls --color=auto'
        /bin/ls
[root@localhost ~]# which pwd
/bin/pwd ##不是所有命令都有別名
```

# 環境變量

由於之前提到搜索系統命令的命令是依據環境變量`$PATH`中的系統命令路徑做搜索的，所以就來介紹一下環境變量吧！

環境變量這種設定在Windows上面也有，在Linux裡面如果沒有環境變量的話，那麼我使用指令的話就要使用絕對路徑才可以找到我要使用的指令，何其的麻煩，如果我要使用`ls`，那麼我要在終端機上面打上`/bin/ls`我的命令才可以執行，這是非常麻煩的，所以Linux上面如果要安裝指令在上面使用的話，就要設定環境變量，雖然Linux基本指令的環境變量在安裝時就已經設定了，但是如果我們要外裝命令的話還是要設定環境變量才行。

```bash
[root@localhost ~]# echo $PATH #查看設定的環境變量
/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin
[root@localhost ~]# whereis ls
[root@localhost ~]# /bin/ls
```

檔案執行一個命令的時候，Linux上會查看`$PATH`下面所有的路徑，以上為例，當我使用`ls`命令，的時候Linux上會查看`/usr/local/bin`再查看`/usr/local/bin`，直到查到了`/bin`找到`ls`指令之後執行。

所以綜合上面所說的，如果我有一個命令想要不用絕對路徑使用的話我就要把這個命令放在`$PATH$`下面的目錄當中。

環境變量不可以亂刪，不管是在Linux還是Windows下，如果環境變量刪除了，會有很多的指令無法使用，用Windows舉例好了，如果改錯有可能會無法打開遊戲(⊙o⊙)哦。

當我在使用一些要新增自己寫的命令或是別人寫的命令的時候，也可以建立一個各別的路徑去分類我的命令，設定方法如下：

```bash
[root@localhost ~]# export PATH=/usr/local/webserver/mysql/bin:$PATH
#新增環境變量
[root@localhost ~]# echo $PATH #查看設定的環境變量
/usr/local/webserver/mysql/bin：/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/TeX/texbin
#環境變量設定成功！
```

當然現在很多的軟體源在安裝的時候就會幫我們設定好環境變量了，可是有時候命令無法執行，還是要會除錯才行，所以我們還是得知道一下環境變量的設定方法。

# find 搜索文件命令

find命令的功能比較多、比較強大，相對的選項就會比較多，其中以下幾個是比較常用的選項。

find  [directory] [option] [conditions]

選項

- `-name`  以文件名搜索
- `-iname` 以文件名搜索，不區分大小寫
- `-user` 搜索該所有者的文件
- `-nouser` 搜索不是該所有者的文件
- `-mtime` 文件上次修改內容時間
- `-atime` 文件上次訪問時間
- `-ctime` 文件上次修改屬性時間
- `-size` 以文件大小搜索文件
- `-inum` 以inode numbr搜索文件
- `-a` AND邏輯
- `-o` OR 邏輯
- `-exec 命令 {} \;` 搜索完後再執行一個命令


## find / -name 以文件名搜索

```bash
[root@localhost ~]# find / -name install.log
/root/install.log
```

在使用find命令搜索文件的時候，應該要避免大範圍搜索，所以指定的路徑盡量要小，還有一點，如果使用這種無通配符的搜索的話，我的搜索條件就要完全相符，所以如果只是要搜索特定的文件，就要使用通配符來執行搜索（其他的指令也是如此）。

### 常用的通配符

通配符在其他的指令中也可以使用其中最長用的是`*`、`？`、`[]`。

- `*` 任意內容
- `?` 一個字符
- `[]`  任意刮號內的字符


```bash

[root@localhost ~]# find /root -name ly*
##搜索範圍內ly開頭的文件
/root/lyre
/root/lyri
/root/lyris
[root@localhost ~]# find /root -name lyr?
##搜索範圍內ly后一個字符的文件
/root/lyri
[root@localhost ~]# find /root -name lyr[ie]
##搜索範圍內lyr后為i或為e的文件
/root/lyre
/root/lyri
[root@localhost ~]# find /root -name *[ie]
##搜範圍內索結尾為i或是為e的文件
/root/lyre
/root/lyri
[root@localhost ~]#find ~/Desktop/Tools -name "*"
##搜索範圍內所有文件
/Users/Gumdam/Desktop/Tools
/Users/Gumdam/Desktop/Tools/.DS_Store
/Users/Gumdam/Desktop/Tools/EFI Patch
/Users/Gumdam/Desktop/Tools/EFI Patch/efi64_31348.bin
/Users/Gumdam/Desktop/Tools/EFI Patch/SnowLeo.tool
/Users/Gumdam/Desktop/Tools/SwitchVersion.tool
[root@localhost ~]# find /root -name lyris*
```

在上面的命令中其中`-name "*"`的搜索中是包含隱藏文件的，例如`.DS_Store`就是隱藏文件。

## find / -iname 以文件名搜索，不區分大小寫


```bash
[root@localhost ~]# find / -name InStAlL.log
find: InStAlL.log: No such file or directory
[root@localhost ~]# find / -iname InStAlL.log
/root/install.log
```

在Linux上面是嚴格區分大小寫的，所以當我搜索文件的時候，如果搜索的關鍵字，我想要大小寫的內容都搜索的話，我就要使用`-iname`了，用這個指令搜索的內容都不會區分大小寫。

## find / -user 以文件所有者搜索

```bash
[root@localhost ~]# find /root -user root
/root
/root/.bashrc
/root/.tcshrc
/root/.bash_history
/root/.lesshst
/root/.bash_profile
/root/install.log
/root/.bash_logout
/root/install.log.syslog
/root/.cshrc
```

## find / -nouser 以文件所有者搜索不是該所有者的文件

```bash
[root@localhost ~]# find /root -nouser root
/root/Gumdam.out
[root@localhost ~]# find /root -nouser -exec rm -rf {} \;
#搜索並且刪除所有沒有所有者的文件
```

在Linux中沒有所用者的文件是垃圾文件，所以一般應該是要手動刪除的，但是有兩個狀況是例外，要特別注意。

第一個情況是Linux的內核產生的文件，內核在執行的過程中是不會經過所用者的，所以內核產生的文件是不會有所用者的，內核的運行過程中會在內存記憶體之中交互作用，所以在`/proc`和`/sys`目錄下面是會產生沒有檔案所用者的文件的。

第二個情況是在Windows上面建立的文件，在這個Windows盛行的時代，我們難免會使用到Windows上面建立的文件，在Windows建立文件的時候是會忽略檔案所用者的，所以如果你用USB隨身碟把你的文件拿到Linux上面作業，你之前在Windows上面建立的文件是沒有所用者的，所以不能刪除。

Linux上面除了以上兩種文件，大多都是可以直接手動刪除的。

## find / -mtime 搜索文件上次修改文件內容的時間

```bash
[root@localhost ~]# find /var/log -mtime +10
```

其中`10`代表天數，如果加上正負號的話，`+10`代表我要查找十天之前修改的文件、`10`代表十天當天修改的文件、`-10`代表十天內修改的文件。

![時間設定](http://i.imgur.com/q3NdeQH.png)


## find / -atime 搜索文件上次訪問的時間

```bash
[root@localhost ~]# find /var/log -atime +10
```

## find / -ctime 搜索文件上次修改文件屬性的時間

```bash
[root@localhost ~]# find /var/log -ctime +10
```

## find /  -size 以文件大小搜索文件

```bash
[root@localhost ~]# find . -size 25k
```

和之前的天數的命令一樣，如果我輸入`25k`是搜索等於25KB的文件、輸入`-25k`是搜索小於25KB的文件、輸入`+25k`是搜索大於25KB的文件，

```bash
find ~/Desktop -size -25K
find: -size: -25K: illegal trailing character
```

其中有些要小心的地方是單位的大小寫，如果KB的K輸入成大小的話，Linux是便是不出來的，因為Linux是嚴格區分大小寫的。

大部分使用到的是KB以及MB，這兩個只要分別寫成`k`、`M`即可。

```bash
find ~/Desktop -size -25
```

如果不寫單位的預設的單位是磁碟扇區，一個扇區，扇區是一個邏輯的概念，並不是真實存在的東西，在這個指令上一個扇區有512KB的大小，所以上面指令是搜索$512KB \times25大小的文件$，這是非常不人性化的使用方式，所以一般不是用它，知道就可以了。

如下圖A為磁軌、B為幾何扇區、C為磁軌扇，相鄰磁區組合在一起，組成D叢集，磁區的排列由格式化成的檔案系統來決定，在Linux的ex4檔案系統中，會把硬碟每4KB切成一個區塊、每512KB切成一個扇區。

![磁碟扇區](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Disk-structure2.svg/290px-Disk-structure2.svg.png)


## find / -inum 以inode numbr搜索文件

```bash
[root@localhost ~]# find / -inum 262223
```

這個指令會搜索inode number為262223的文件，inode number在之前已經提過了所以不再多做解釋。

## find 下的`-a`和`-o`

```bash
[root@localhost ~]# find /etc -size +32k -a -mtime -10
## 搜索/etc 目錄下大於32KB且十天內有修改過內容的文件
[root@localhost ~]# find /etc -size +32k -o -mtime -10
## 搜索/etc 目錄下大於32KB或十天內有修改過內容的文件
```


## find 搜索後面加上 `-exec 命令 {} \;`

```bash
find  [directory]  [Option]  [condition]  -exec [command] {} \;
```

這個命令代表把find命令的搜尋結果用`-exec`後面的命令去處理，其中`-exec [command] {} \;`是通用格式，是要記起來的。

```bash
[root@localhost ~]# find /etc -size +32k -exec ls -lh {} \;
## 列出/etc目錄下面大於32KB的檔案
[root@localhost ~]# find /etc -nouser -exec rm -rf {} \;
## 搜索/etc 目錄下沒有所有者的文件，然後全部刪除
```

這個格式只可以在find命令下使用，如果在其他命令下面使用會報錯：

```bash
[root@localhost ~]# ll ~/Desktop/te.md -exec mv ~ {} \;
ls: -exec: No such file or directory
ls: mv: No such file or directory
ls: {};: No such file or directory
-rw-r--r--@ 1 Gumdam  staff    21K  3 16 19:25 /Users/Gumdam/Desktop/te.md

/Users/Gumdam:
total 1032
drwx------+ 33 Gumdam  staff   1.1K  3 17 00:22 Desktop
drwx------+ 32 Gumdam  staff   1.1K  3 15 18:46 Documents
-rw-r--r--   1 Gumdam  staff   9.6K  3  7 21:08 vimrc
```

# grep 搜索文件中字符串命令

grep [OPTIONS] PATTERN [FILE...]

選項

- `-i` 不區分大小寫查詢
- `-v` 排除指定字串


## grep / -i

```bash
[root@localhost ~]# grep "net" anaconda-ks.cfg
network  --bootproto=dhcp --device=ens33 --ipv6=auto --activate
network  --hostname=localhost.localdomain
[root@localhost ~]# grep -i "net" anaconda-ks.cfg
# Network information
network  --bootproto=dhcp --device=ens33 --ipv6=auto --activate
network  --hostname=localhost.localdomain
```

Linux是會區分大小寫的，如果想要大小寫全部搜尋就要加上`-i`。

## grep / -v

```
[root@localhost ~]# echo maplestory is great game >> info.log
[root@localhost ~]# grep -v maplestory info.log
[root@localhost ~]# echo you lose &>> info.log
[root@localhost ~]# cat info.log
maplestory is great game
you lose
[root@localhost ~]# grep -v "maplestory" info.log
you lose
```

如果我們要搜索除了含有某個字串以外的內容的話，我們可以使用`-v`，上面的例子中，我搜索沒有`maplestory`部分的內容，在第二行我的搜索沒有任何內容是因為`grep`查詢是查詢一整句話，我的內容就只有一句話，而除了這句話以外，我沒有其他的內容了，所以沒有查詢結果。

