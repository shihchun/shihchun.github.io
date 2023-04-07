# Linux目錄指令


## mkdir 目錄創建

mkdir [option]  [parameter]

選項

- `-p`遞歸創建（創建`/Gumdan/...`）

```bash
[root@localhost~]#mkdir ~/Desktop/Gumdan
```

```bash
[root@localhost~]# mkdir ~/Desktop/Gumdan/season
mkdir: /Users/Gumdam/Desktop/Gumdan: No such file or directory
```

```bash
[root@localhost~]# mkdir -p ~/Desktop/Gumdan/season
```

當要創建`/Gumdan/season`的時候`/Gumdan`不存在的話要是用`-p`才可以進行創建。

## cd 切換目錄

簡化指令|功能
---|---
cd /|進入根目錄
cd ~|進入家目錄
cd|進入家目錄
cd -|進入上一次目錄（切換前）
cd ..|進入上一級目錄
cd .|進入當前目錄（沒有用）

可以利用`pwd`查看自己的目錄位置，`cd`值得一說的一點是它是shell原本內建（自帶）的命令，可以使用搜索指令查詢得知：

```bash
[root@localhost~]# which cd
cd: shell built-in command
```

除了`cd`是shell自帶命令以外，其實還有很多指令是自帶的，例如：`alias`、`bg`、`fg`、`echo`

使用`cd`指令的時候需要考慮路徑的問題，路徑分為相對路徑和絕對路徑，相對路徑是參照目前目錄位置去執行的路徑，絕對路徑是則可以因為不用參照路徑，所以可以在任何目錄中執行。

相對路徑|絕對路徑
---|---
`../usr/local/src` | `/usr/local/src`

```bash
[root@localhost~]# pwd
/root   # 參照目錄為 /root
[root@localhost~]# cd ../usr/local/src 
[root@localhost src]# pwd
/usr/local/src ## 參照目錄為 /usr/local/src
[root@localhost~]# cd ../usr/local/src 
cd: no such file or directory: ../usr/local ## 無法辨認 /usr、/local 
[root@localhost src]# cd /usr/local/src ## 絕對路徑可以在任何位置使用
```

相對路徑要注意一點，當我當前目錄位置發生變化，原本可以執行的命令，就有可能不能執行，相對的絕對路徑就不會有這個問題，所以使用網路上面複製的指令時，要特別注意路徑是否正確。

在Linux當中有`Tab`補全的功能，建議使用`Tab`避免打字錯誤的狀況發生，在一些發行版本作業系統雖然指令使用方法雖然相同，但是可能會有一些小問題，比如我在Mac OS裡面的空格（blank space）在終端機上會顯示為`\`，所以在不使用`Tab`的狀況之下，打錯的可能性很高，使用`Tab`可以減少不必要的錯誤。

```bsah
[root@localhost ~/Desktop]# cd   ## 按下 Tab 鍵會出現下方補全
\$RECYCLE.BIN/   Project.logicx/  Tools/      icircuit/
Gumdan/          Rmd\ to\ pptx/   cpp\ text/
[root@localhost ~/Desktop]# cd Rmd\ to\ pptx/  ##按 Tab 選出要的
```

## rm 刪除文件或是目錄

rm  [option]  [file or directory]

選項：

- `r` 刪除目錄
- `f` 強制刪除

```bash
[root@localhost ~/Desktop]# mkdir abc
[root@localhost ~/Desktop]# rm abc
rm: abc: is a directory
[root@localhost ~/Desktop]# rm -r abc
rm: remove directory 'abc'? n
[root@localhost ~/Desktop]# rm -rf abc
```
在Linux上面的`rm`指令不是Windows上面的刪除，它並不會把檔案送到回收桶，你刪了他就消失了，一般在使用`rm`指令的時候都會直接使用`rm -rf`來刪除檔案，因為刪除目錄的時候要有`-r`、不加`-f`的話有會被問是否刪除，所以一般常用`rm -rf`。

```bash
[root@localhost ~/Desktop]# rm -rf /
```

`rm`有一個要小心的地方，上面的這個指令真的不要打上去，這個指令會讓系統99%的數據被刪除，但是系統並不會崩潰，如果沒有raid陣列或是其他的保護檔案的措施的話文件是無法還原的，說簡單一點數據恢復牽涉的條件非常的廣，要盡量避免這種事情發生。

這是讓Linux自殺的指令，但是Linux卻會不誤的去執行它，令人不安心的是，在輸入路徑的時候這個是很可能不小心出現的錯誤，但是這也側面說明了在Linux上面使用者擁有很高的系統權限。

```bash
[root@localhost /]# rm -rf /bin
[root@localhost /]# rm -rf /bin/*
```

使用`rm -rf`的時候還要注意一個地方不要刪錯一些系統目錄或是系統的掛載點，上面的指令中的`/bin/*`是指`/bin`目錄下面的內容，這個指令如果刪除`/bin`的話會刪除`/bin`這個系統目錄，這個是我們不希望發生的，如果刪除了像是`/proc`、`/sys`之類的掛在點可能就出大事情了。

## cp 複製指令 

cp  [option]  [source file] [target file]

選項

- `-r` 複製目錄
- `-p` 連帶文件屬性一起複製
- `-d` 如果複製的文件是鏈接文件，複製鏈接屬性
- `-a` 相當於 `-pdr` 全部，一般使用`-a`

```bash
[root@localhost~]# cp install.log /tmp # 沒寫檔案名稱會原名複製
[root@localhost~]# cp install.log /tmp/knps # 複製后為knps
[root@localhost~]# cp Gumdan ~/Desktop # 要複製目錄要使用 -r
cp: Gumdan is a directory (not copied).
[root@localhost~]# cp -r Gumdan ~/Desktop # 保險一點使用 -a
```
在使用`cp`指令的時候，如果只有給目標目錄位置，沒有給檔案名稱的話`cp`指令會原名複製。

### cp -a

```bash
[root@localhost~/Desktop]# date
2017年 3月 9日 周四 21時03分15秒 CST
[root@localhost~/Desktop]# ll a.out
-rwxr-xr-x  1 Gumdam  staff    15K  3  6 21:51 a.out
[root@localhost~/Desktop]# cp a.out ~
[root@localhost~/Desktop]# cp -a  a.out ~/b.out
[root@localhost~]# cd ~
[root@localhost~]# find *.out -exec ls -lh {} \;
-rwxr-xr-x  1 Gumdam  staff    15K  3  9 21:13 a.out
-rwxr-xr-x  1 Gumdam  staff    15K  3  6 21:51 b.out
```

如果單只是使用`cp`的話其他的屬性是不會被複製的例如日期、鏈接...，所以只要記得使用`-a`就可以了。如上面的指令有使用`-a`複製出來的文件日期是3月6日，而沒有使用的話，日期就是今天的日期。

## mv 搬移指令

mv  [file or directory] [target directory]

```bash
[root@localhost~/Desktop]# mv -r  Gumdan
mv: illegal option -- r
usage: mv [-f | -i | -n] [-v] source target
       mv [-f | -i | -n] [-v] source ... directory
[root@localhost~/Desktop]# mv Gumdam ~
```

`mv`和之前的`rm`還有`cp`不一樣，需要注意的之有它搬移目錄的時候不需要也不行使用`-r`，這個是因為Linux是分散式的開發，所以會有這種開發上面是有興趣人去開發的，所以有些指令會有這種選項不一的問題存在。

## Linux 目錄功用

```bash
[root@localhost~/Desktop]# cd /
[root@localhost~/Desktop]# ls
bin cgroup  etc lib media  mnt  opt root  
selinux  sys  usr boot  dev home  lost+found
misc  net proc  sbin  srv tmp var
[root@localhost~/Desktop]# cd /usr
[root@localhost~/Desktop]# ls
bin etc games include lib libexec local sbin
share src tmp
[root@localhost~/Desktop]#
```

根目錄和`/usr`目錄中的`/bin`目錄和`/sbin`是用來儲存系統命令用的目錄，`/boot`目錄是放開機啟動數據的，`/dev`目錄裡面放的是硬體相關的文件，這幾個文件沒事不用去動它，裡面是一般的使用者用不到的內容，其中`/bin`和`/sbin`的區別就是`/bin`儲存一般使用者的指令，是所有使用這都可以使用的指令、`/sbin`儲存超級使用者的指令。

`/etc`目錄儲存系統的一些設定檔案，是很常用到的目錄。

`/home`普通使用者的家目錄。

`/root`是最高權限使用者的家目錄。

`/lib`是Linux函數庫儲存的目錄，在Linux裡面啟動的時候所有函數都加載的話，啟動和執行的速度將會無比的緩慢，所以會把一些不常使用的函數庫放在`/lib`裡面要是用的時候再調用，不使用就算了。

`/mnt`、`/media`、`/misc`是Linux準備的三個掛載目錄，這三個目錄只要是空目錄就可以了，是留給使用者掛載設備用的，三個都可以使用，但是大部分人一般只使用`/mnt`，因為在比較早的Linux裡面只有`/mnt`這個掛載目錄。

`/sys`、`/proc`是儲存內存數據資料的，是內存記憶體的掛載點，是不能直接操作的，我們是不能在裡面寫資料的，第一，如果重新啟動會資料丟失、第二，如果丟太大的檔案記憶體又不夠，會系統崩潰。

`/var`儲存特定於此系統的可變數據，在系統啟動之間保持永久性。動態變化文件（如：資料庫、緩存目錄、日誌文件、印表機後台處理文檔和網站內容等）。

一般可以隨便放檔案的目錄只有三個`/home`、`/root`、`/tmp`，其他的目錄如果不清楚就不要去動它，還有不建議把所有的檔案儲存在根目錄`/`下面，就像是把檔案全部放在Windows的桌面一樣，在使用上根目錄是非常常訪問的目錄，為操作方便，不要把所有的檔案放在根目錄。

