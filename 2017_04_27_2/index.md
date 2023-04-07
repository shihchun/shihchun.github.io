# Linux 壓縮與解壓縮


檔案壓縮有很多種方式，所以也有很多的壓縮格式，各種壓縮方式也有它的優缺點，當然這不是這篇的重點，這篇主要是要說在Linux上面壓縮與解壓縮的方式。

在Linux上面其中壓縮格式比較常見的有`.zip`、`.gz`、`.bz2`、`.tar.gz`、`.tar.bz2`

在壓縮的過程中，其實可以不用把副檔名寫上去，因為Linux是不會認這個東西的，但是為了方便辨認大部分操作上，還是要寫上去才可以。

<!---more--->
 
## zip 壓縮

*.zip

zip [option] [filename] [source file]

zip -r [filename]  [source file]

```bash
$ touch myfile
$ zip myfile.zip myfile
adding: myfile (stored 0%) ## 因為myfile是空文件所以為0%
$ mkdir myfiles
$ mv myfile myfiles
$ zip myfile.zip myfile/ ## 只有壓縮目錄，解壓縮為空目錄
  adding: myfile/ (stored 0%)
$ zip -r  myfile.zip myfile/ ## 只有壓縮目錄及目錄下的檔案
updating: myfile/ (stored 0%)
  adding: myfile/asdf (stored 0%）
```

## unzip 解壓縮

```bash
$ unzip myfile.zip
Archive:  myfile.zip
   creating: myfile/
 extracting: myfile/myfile
```


## gzip 壓縮

*.gz

gzip [source file]

```bash
$ touch myfile
$ gzip myfile
$ ll
總計 8
drwxr-xr-x. 15 root     root     4096  4月  4 19:56 DIR-850L_A1
-rw-rw-r--.  1 cyberjun cyberjun   27  4月 26 19:29 myfile.gz
```

gzip -c [source file] > [filename]

```bash
$ touch myfile
$ gzip -c myfile > myfile.gz
$ ll
總計 8
drwxr-xr-x. 15 root     root     4096  4月  4 19:56 DIR-850L_A1
-rw-rw-r--.  1 cyberjun cyberjun    0  4月 26 19:32 myfile
-rw-rw-r--.  1 cyberjun cyberjun   27  4月 26 19:32 myfile.gz
```

gzip在壓縮之後原本的文件會消失，所以我們要把命令的結果寫到新的文件儲存，也就是使用`>`把結果給[filename]。



gzip -r [directory]

```bash
$ mkdir myfiles
$ cd myfiles
$ touch myfile1
$ touch myfile2
$ touch myfile3
$ cd ..
$ gzip -r  myfiles
$ ll
總計 4
drwxr-xr-x. 15 root     root     4096  4月  4 19:56 DIR-850L_A1
drwxrwxr-x.  2 cyberjun cyberjun   60  4月 26 19:35 myfiles
$ cd myfiles
$ ll
總計 12
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile1.gz
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile2.gz
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile3.gz
```

執行完這個指令之後他會把目錄下面的所有文件一個一個壓縮，但是不會把目錄給壓縮。

## gzip -d或gunzip解壓縮

*.gz

```bash
$ gzip -d myfile.gz
$ gunzip myfile.gz
$ gunzip myfiles.gz
$ cd myfiles
$ ll
總計 12
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile1.gz
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile2.gz
-rw-rw-r--. 1 cyberjun cyberjun 28  4月 26 19:34 myfile3.gz
$ cd ..
$ gunzip -r myfiles
gzip: myfiles is a directory -- ignored ## 目錄要 -r
$ gunzip -r  myfiles
$ ll
總計 4
drwxr-xr-x. 15 root     root     4096  4月  4 19:56 DIR-850L_A1
drwxrwxr-x.  2 cyberjun cyberjun   51  4月 26 19:42 myfiles
$ cd myfiles/
$ ll
總計 0
-rw-rw-r--. 1 cyberjun cyberjun 0  4月 26 19:34 myfile1
-rw-rw-r--. 1 cyberjun cyberjun 0  4月 26 19:34 myfile2
-rw-rw-r--. 1 cyberjun cyberjun 0  4月 26 19:34 myfile3
```

## bzip2 壓縮

*.bz2
bzip2 [sourcefile]

```bash
$ touch abc
$ bzip2 abc
$ ll
總計 4
-rw-rw-r--.  1 cyberjun cyberjun   14  4月 26 19:49 abc.bz2
```

這個樣子原本的文件會和`gzip`一樣消失，如果要保留原本的文件要使用`-k`。

bzip2 -k [sourcefile]

```bash
$ touch -k abc
$ bzip2 abc
$ ll
總計 8
-rw-rw-r--.  1 cyberjun cyberjun    0  4月 26 19:52 abc
-rw-rw-r--.  1 cyberjun cyberjun   14  4月 26 19:52 abc.bz2
```

使用`-k`這個樣子原本的文件保留下來了。

bzip2不能壓縮目錄

```bash 
$ mkdir abc
$ bzip2 abc
bzip2: Input file abc is a directory.
```

`bzip2`並沒有支援目錄壓縮

## bzip2 -d或bunzip2解壓縮

*.bz2

```bash
$ touch abc
$ bzip2 abc
$ bzip2 -d abc.bz2
$ ll
abc.bz2
$ rm -rf ab*
$ touch abc
$ bzip2 abc
$ bunzip2 abc.bz2
$ ls
abc.bz2
```

解壓縮執行之後原本的檔案會消失，所以如果要保留原本的檔案要使用`-k`

```bash
$ bunzip -k abc.bz2
$ bzip -dk abc.bz2
```

# tar 打包


由於gzip和bzip2不能把目錄壓縮起來所以就有了tar了打包，如果要壓縮的話就只要把檔案先打包起來再壓縮成`.tar.gz`、`.tar.bz2`就可以了

## tar -cvf 打包

*.tar

tar -cvf [filename] [sourcefile]

- `-c`: 打包
- `-v`: 顯示打包過程
- `-f`: 指定打包後的文件名稱

```bash
$ mkdir myfiles
$ cd myfiles/
$ touch myfile1
$ touch myfile2
$ touch myfile
$ cd ..
$ tar -cvf myfiles.tar myfiles
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ ll
總計 16
drwxrwxr-x.  2 cyberjun cyberjun    50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun 10240  4月 26 20:14 myfiles.tar
```

之後如果想要在進行gzip、bzip2壓縮的話，就直接執行壓縮如下：

```bash
$ gzip -c myfiles.tar > 
$ bzip2 -k myfiles.tar
$ ll
總計 24
drwxrwxr-x.  2 cyberjun cyberjun    50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun 10240  4月 26 20:14 myfiles.tar
-rw-rw-r--.  1 cyberjun cyberjun   191  4月 26 20:14 myfiles.tar.bz2
-rw-rw-r--.  1 cyberjun cyberjun   191  4月 26 20:18 myfiles.tar.gz
```

## tar -xvf 解打包

tar -xvf [.tar file]

- `-x` 解打包

解.tar.gz

```bash 
$ gunzip -c myfiles.tar.gz > myfiles.tar
$ tar -xvf myfiles.tar
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ ll
總計 24
drwxrwxr-x.  2 cyberjun cyberjun    50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun 10240  4月 26 20:31 myfiles.tar
-rw-rw-r--.  1 cyberjun cyberjun   191  4月 26 20:27 myfiles.tar.gz
```

解.tar.bz2

```bash 
$ bunzip -k myfiles.tar.bz2
$ tar -xvf myfiles.tar
$ ll
總計 24
drwxrwxr-x.  2 cyberjun cyberjun    50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun 10240  4月 26 20:28 myfiles.tar
-rw-rw-r--.  1 cyberjun cyberjun   191  4月 26 20:14 myfiles.tar.bz2
```

# 打包.tar.gz和.tar.bz2

`tar`是支援直接打包成`.tar.gz`、`.tar.bz2`的，所以其實不需要像之前那個樣子壓縮與解壓縮這麼麻煩。

## tar -z cvf或xvf

tar -zcvf [filename.tar.gz] [sourcefile]

tar -zxvf [sourcefile.tar.gz]

如果要打包成.tar.gz的話，只要在之前的打包指令前面加上`-z`即可。

```bash
$ tar -zcvf myfiles.tar.gz myfiles/
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ rm -rf myfiles
$ tar -zxvf myfiles.tar.gz
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ ll
總計 8
drwxrwxr-x.  2 cyberjun cyberjun   50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun  179  4月 26 20:46 myfiles.tar.gz
```

## tar -j cvf 或xvf

tar -jcvf [filename.tar.bz2] [sourcefile]

tar -jxvf [sourcefile.tar.bz2]

如果要打包成.tar.bz2的話，只要在之前的打包指令前面加上`-j`即可。

```bash
$ tar -jcvf myfiles.tar.bz2 myfiles/
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ rm -rf myfiles
$ tar -jxvf myfiles.tar.bz2
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ ll
總計 8
drwxrwxr-x.  2 cyberjun cyberjun   50  4月 26 20:14 myfiles
-rw-rw-r--.  1 cyberjun cyberjun  191  4月 26 20:48 myfiles.tar.bz2
```

## tar 指定解壓縮位置

tar -xvf [sourcefile.tar] -C [directory]

```bash
$ tar -zcvf myfiles.tar.gz myfiles/
myfiles/
myfiles/myfile1
myfiles/myfile2
myfiles/myfile
$ tar -zxvf myfiles.tar.gz -C /tmp/
$ ll /tmp/
總計 8
drwxrwxr-x.  2 cyberjun cyberjun   50  4月 26 20:14 myfiles
drwx------. 3 root root 17  4月 26 14:45 systemd-private-14d94e1345584cf1b22f365c4e00445b-vmtoolsd.service-6dKW4n
```

#@ tar 壓縮多個文件

tar -cvf [filename.tar] [file1] [file2]....etc.

如果要指定壓縮位置的話，只要把[filename.tar]用絕對路徑去寫就可以了。

```bash
$ ll
總計 8
-rw-rw-r--. 1 cyberjun cyberjun   0  4月 26 20:14 myfile
-rw-rw-r--. 1 cyberjun cyberjun   0  4月 26 20:13 myfile1
-rw-rw-r--. 1 cyberjun cyberjun   0  4月 26 20:14 myfile2
-rw-rw-r--. 1 cyberjun cyberjun 142  4月 26 21:01 myfile3.tar.bz2
-rw-rw-r--. 1 cyberjun cyberjun 139  4月 26 21:01 myfile3.tar.gz
drwxrwxr-x. 2 cyberjun cyberjun   6  4月 26 20:59 myfiledir
$ tar -cvf ~/myfiles.tar myfile myfile1 myfile2 myfile3.tar.bz2  myfile3.tar.gz
myfile
myfile1
myfile2
myfile3.tar.bz2
myfile3.tar.gz
$ cd
$ ll
總計 16
-rw-rw-r--.  1 cyberjun cyberjun 10240  4月 26 21:02 myfiles.tar
```

