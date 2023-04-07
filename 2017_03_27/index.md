# Linux命令基本格式



```bash
[root@localhost~]#
```

其中表示意義如下表：

標記|意義
---|---
root：|當前登錄的目錄
localhost|主機名稱
~|家目錄（這個位置放當前所在目錄）
#|表示超級用戶（普通用戶為$）

### pwd

```bash
[root@localhost~]# pwd
```

`pwd`指令可以顯示當前的絕對路徑，所以如果我在`~`的目錄下面使用`pwd`的話，用該要顯示`/root/home/`這個家目錄才對。

### 命令格式

命令  [option]  [parameter]

其中選項（Option）又分為簡化選項和完整選項比如`ls`中的簡化選項`-a`的完整選項就是`--all`，簡化選項和完整選項的功能是一樣的。


```bash
ls  [Option]  [file or directory]
```

選項：

- `-a`  顯示所有文件，包括隱藏文件
- `-l`  顯示詳細訊息
- `-d`  查看目錄屬性
- `-h`  人性化的顯示文件大小（2023389->1.9M）
- `-i`  顯示inode number

### ls -a

```bash
[root@localhost~]# ls -a
      anaconda-ks.cfg     .bash_profile   .cshrc
```
Linux裡面(.)開頭的文件就是隱藏文件，這個指令下了之後會顯示所有文件，包括隱藏的文件，在上面的範例之中`.cshrc`就是隱藏文件。

### ls -l

```bash
[root@localhost~/Desktop]# ls -l
-rwxrwxrwx@ 1     root  staff    7056122  8 11  2015 the-swift.pdf
drwxr-xr-x  4     root  staff        136  3  8 20:21 Rmd to pptx
#權限 #軟連接次數  #所文件用者     ##檔案大小  ##日期    ##檔案名稱
      #引用計數           ##檔案大小不人性化
```

#### 權限

`-`rw--r--r--

在說權限之前，要先比較一下Linux和Windows之間文件類型，Linux不像是Windows有明顯區分擴展名，Linux的軟體、硬體都是以文件形式儲存的，不管是目錄、設備...都是以文件的方式儲存的，他們的差別就只有權限。

權限默認一般有十位的字，其中第一位`-`為文件類型，文件類型最常見的有三個分別是文件`-`、目錄`d`、軟連接文件`l`，後面九個數字分別代表各種用戶所持有的權限，每三位數為一組，分別為檔案擁有者、加入此群組之帳號的權限、非本人且沒有加入本群組之其他帳號的權限，簡略的說有三個組：u所屬者、g所屬組、o其他人，而顯示的字符有讀（r）、寫（w）、執行（x）三種權限。

權限說白了就是文件和用戶之間的關係，明確各個身份所持有的權限（讀、寫、執行）

其實文件類型除了這些以外還有四種文件類型塊設備文件`b`、字符設備文件`c`、套接字文件`s`、管道文件`p`，但是並不常用只要大概知道就可以了，因為這些內容不需要普通用戶做操作。

最近的Linux權限有時候在十個位數後面會有一個(`.`),例如：`-`rw--r--r--.，這個(`.`)官方並沒有明確定義，但是在使用經驗上面知道這個大概是代表（ACL權限），除此之外在Mac OS上面甚至還有`@`，例如：-rw-r--r--@，這些類型大概知道一下就可以了。

-|rw-|r--|r--
---|---|---|---
`-`、`d`、`l`|u所屬者|g所屬組|o其他人

### ls -d

```bash
[root@localhost~/Desktop]# ls -d
.
```

```bash
[root@localhost~/Desktop]# ls -ld
drwxr-xr-x+ 53 Gumdam  staff  1802  3 11 16:46 .
```

`-d`這個選項單獨使用時是沒有意義的，因為`ls -l`並沒有辦法顯示當前目錄的資料，因為我的Desktop沒有檔案，所以沒有任何的資訊，Linux當中目錄也是檔案，而這個檔案的權限我們無法得知，而這個`-d`可以讓我們可以查看目錄的屬性。


### ls -h

```bash
[root@localhost~/Desktop]# ls -h
Adlm                 Downloads            Untitled-figure
Applications         Library              Untitled.Rpres
```

```bash
[root@localhost~/Desktop]# ls -lh \dev
crw-------  1 root         wheel           13,   1  3  7 21:10 afsc_type5
crw-rw-rw-  1 root         wheel           18,   1  3  7 21:10 cu.Bluetooth-Incoming-Port
brw-r-----  1 root         operator         1,   0  3  7 21:10 disk0
brw-r-----  1 root         operator         1,   1  3  7 21:10 disk0s1
brw-r-----  1 root         operator         1,   3  3  7 21:10 disk0s2
brw-r-----  1 root         operator         1,   2  3  7 21:10 disk0s3
### ....etc
###權限                              ##檔案大小人性化
```
`-h`這個選項單獨使用時是沒有什麼意義的，因為這個選項是讓我的`ls`指令中的內容可以人性化的顯示檔案大小，但是單是在`ls -h`這個指令下面並不會有檔案大小所以使用的效果和`ls`是一樣的。

### ls -lh 等於 ll

```bash
## ls -lh 等同 ll
[root@localhost~]# ls -lh

[root@localhost~]# ll
```

這兩個指令是等同的，可以使用搜索指令去查`ll`會顯示如下：

```bash
## which 查詢命令的別名（wereis 可查詢命令、幫助文檔的位置）
[root@localhost~]# which ll

ll: aliased to ls -lh
```

除了這個樣子查詢以外，還可以使用`alias`透過指令的別名查詢指令指令的全名，比如我看到一個叫做`gstd`的指令，我不知道它是什麼指令，我就可以使用`alias`來查詢：

```bash
[root@localhost~]# alias _
_=sudo
```

### ls -i

```bash
[root@localhost~]# ls -i  ~/Desktop
3355431 $RECYCLE.BIN
 454344 -the-swift-programming-language-.pdf
4753760 Orphans no Namida.mp3
 453557 Command_line.pdf
#inode number  #filename
```

#### inode number 介紹

Unix的時候，利用inode來取資料的方式就已經有了，在Linux上面也是使用這種資料查找資料，在Linux上面每一個檔案都有一個inode number，就大家所知道的檔案儲存在硬碟的位置是不固定的，首先，假設你的硬碟被格式化成了ex4檔案系統，會建立一個inocde table查找表，你的硬碟被切成了好幾個等大小的數據塊，每一個數據塊可以儲存4KB的檔案，如果我有一個10KB的檔案儲存了進去，它並不會連續的儲存，假設它分別儲存了4KB在Proc A、4KB在Proc B、2KB在Proc C。

講到這裡有一個問題，我這個10KB的文件儲存了進去有一個區塊只有儲存2KB的資料，那麼這個區塊還可以儲存其他的資料嗎？答案是不行的，有興趣可以自己去研究，數據塊不是只能切成每4KB一個區塊，默認是4KB，但是其實是可以0KB、2KB、4KB三種的。

在查找表裡面會記錄inode number（ID號碼）、修改時間、權限以及要抓資料的區塊位置。Linux中檔案在開啟的時候就是利用這個概念去抓資料的，首先讀取到inode number，再確認權限，如果不匹配就直接拒絕，匹配的話就會把數據塊中的資料抓給使用者使用。

![圖3-1.1 Linux檔案系統抓資料示意圖](http://www.cs.ucsb.edu/~rich/class/cs170/notes/FileSystem/filetable.rich.jpg "Linux 讀取檔案過程示意圖")

