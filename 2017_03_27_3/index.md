# Linux鍵結指令



ln  [option]  [source file] [target file]

選項

 - `-s` 建立軟鏈接

鏈接指令分為硬鏈接和軟連接，沒有加上任何選項，軟鏈接要加上`-s`

## 硬鏈接

硬鏈接的特征

- 硬鏈接和原本文件有相同的inode number和儲存區塊，可以看做是同一個文件
- 可以通過inode number找尋檔案
- 不能跨分區
- 不能針對目錄使用


## 軟鏈接

軟連接特征：

- 類似Windows快捷方式
- 軟連接有自己的inode number和儲存區塊，但是自己的數據區塊裡面只有儲存原檔的inode number以及儲存區塊
- 軟鏈接的權限都為lrwxrwxrwx
- 修改任意文件，另一個文件會更動
- 原始檔刪了，軟鏈接失效


![圖3-3.1 軟、硬鏈接檔案查找方式](https://miro.medium.com/max/1200/1*1pFq8FM1s0LLd2EBzINA5w.png)

```bash
[root@localhost~/Desktop]# touch Gumdam00 # 建立一個空文件
[root@localhost~/Desktop]# ll
total 0
-rw-r--r--  1 Gumdam  staff     0B  3 11 23:07 Gumdam00
[root@localhost/]# ln /Gumdam00 /WinGumdam.hard ## 建立硬鏈接 .hard
[root@localhost/]# ll
total 0
-rw-r--r--  2 Gumdam  staff     0B  3 11 23:07 Gumdam00
-rw-r--r--  2 Gumdam  staff     0B  3 11 23:07 WinGumdam.hard
## 硬鍵接會增加引用計數
[root@localhost/]# ln -s /Gumdam00 /GumdamDeathscythe.bak ## 建立軟連接 .bak
[root@localhost/]# ll
total 16
-rw-r--r--  2 Gumdam  staff     0B  3 11 23:07 Gumdam00
lrwxr-xr-x  1 Gumdam  staff     8B  3 11 23:10 GumdamDeathscythe.bak -> Gumdam00
-rw-r--r--  2 Gumdam  staff     0B  3 11 23:07 WinGumdam.hard
## 軟鏈接不會增加引用計數
[root@localhost~/]# ln /WinGumdam.hard /GumdamHeavyarms.hard # 建立硬鏈接
[root@localhost~/]# rm /WinGumdam.hard # 刪除原始檔
[root@localhost~/]# open /GumdamHeavyarms.hard
## 硬鏈接沒有原文件還可以開
[root@localhost/]# ln -s /GumdamHeavyarms.hard /GumdamSandrock.bak # 建立軟鏈接
[root@localhost/]# rm /GumdamHeavyarms.hard
[root@localhost/]# open  /GumdamSandrock.bak 
The file /Users/Gumdam/Desktop/Gumdam/GumdamSandrock does not exist.
## 軟鏈接沒有原文件失效
```

軟鏈接有一個很重要的重點，路徑一定要**寫絕對路徑**，不然兩個檔案在不同目錄之下你的軟鏈接接是會找不到檔案的，寫絕對路徑是最好的，由於硬鏈接都有相同的inode number所以在不同目錄還是可以打開。

```bash
[root@localhost~/Desktop]# pwd
/Users/Gumdam/Desktop
[root@localhost~/Desktop]# ln -s /Users/Gumdam/Desktop/lyris lyris1
[root@localhost~/Desktop]# ln -s lyris lyris2
[root@localhost~/Desktop]# cat lyris2 #使用絕對路徑軟鏈接 同目錄打開
オルフェンズ　涙　愛は悲しみを背負い　強くなれるから
[root@localhost~/Desktop]# ln lyris lyris3
[root@localhost~/Desktop]# mv lyris* ~ #將lyris1、2、3 移動到~目錄
[root@localhost~/Desktop]# cd ~
[root@localhost~/Desktop]# cat lyris1 #使用絕對路徑軟鏈接 搬移後打開
オルフェンズ　涙　愛は悲しみを背負い　強くなれるから
[root@localhost~/Desktop]# cat lyris2 #使用相對路徑軟鏈接 搬移後打開
cat: lyris2: No such file or directory

[root@localhost~/Desktop]# cat lyris3 #使用相對路徑硬鏈接 搬移後打開
オルフェンズ　涙　愛は悲しみを背負い　強くなれるから
```

如果在練習指令的時候視窗的東西太亂，可以使用`clear`指令清空目前視窗上打過的指令，或是使用快捷鍵 <kbd>Ctrl</kbd>+<kbd>L</kbd>

如果是使用GUI界面的Linux，一般也會有很多很多圖形界面的軟體，鏈接的指令可以使用在安裝`.AppImage`文件的時候，如果要製作鍵結在桌面可以向下面安裝，`.AppImage`的檔案一般是不會有鏈接的，每次要使用都要去找檔案目錄的位置非常麻煩，。

```bash
[root@localhost~/Desktop]# cd ~/Downloads
[root@localhost~/Desktop]# chmod u+x MuseScore*.AppImage
[root@localhost~/Desktop]# ln -s MuseScore*.AppImage ~/Desktop
```

講到軟體安裝，就順便說一下debian的系統常常使用`.deb`的軟體包（Debian軟體包）的格式，細部的內容可以參考[dpkg使用筆記](http://foreachsam.github.io/book-util-dpkg/book/)：

```bash
[root@localhost~/Desktop]# dpkg -i teamviewer*.deb ##安裝軟體包
[root@localhost~/Desktop]# dpkg -r teamviewer*.deb ##移除軟體包
```

