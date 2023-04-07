# Linux 幫助指令


Linux 查找命令的用法的時候可以使用Linux下面的幫助指令查找命令的使用方法。

<!---more--->

## man 使用

[![asciicast](https://asciinema.org/a/NdNkEIBFZfUAc5D9bFY9JiBDo.svg)](https://asciinema.org/a/NdNkEIBFZfUAc5D9bFY9JiBDo)

```bash
$ man ls
```

 文檔內容

```bash
LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List information about the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort is spec‐
       ified.

       Mandatory  arguments to long options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
              with -l, print the author of each file

       -b, --escape
              print C-style escapes for nongraphic characters

       --block-size=SIZE
              scale   sizes   by   SIZE   before   printing   them;   e.g.,
              '--block-size=M'  prints  sizes  in units of 1,048,576 bytes;
              see SIZE format below

       -B, --ignore-backups
              do not list implied entries ending with ~

       -c     with -lt: sort by, and show, ctime (time of last modification
              of  file status information); with -l: show ctime and sort by
 Manual page ls(1) line 1 (press h for help or q to quit)
 ```
 
 
輸入之後會會看到ls指令的相關用法如上，輸入之後可以開始查找文檔裡面的內容了，進入man模式之後其實它的操作跟vi的操作十分雷同。

如果要離開的話只要輸入一個`q`就可以離開了，同vi的操作如果我要查找`-d`的使用方式，我只要打入`/-d`，他就會跳到第一個出現`-d`的位置了，如果是要找前、後一個`-d`，只要輸入`n`、`shift`+`n`。


### man 文件級別

在之前輸入`man ls`的時候，有告知`LS(1)`，這個級別1代表指令的用戶級別，各個查找級別如下：


```bash
$ man man
```

用戶級別

```bash 
.
.
.
The table below shows the section numbers of the manual followed  by
       the types of pages they contain.

       1   Executable programs or shell commands
       2   System calls (functions provided by the kernel)
       3   Library calls (functions within program libraries)
       4   Special files (usually found in /dev)
       5   File formats and conventions eg /etc/passwd
       6   Games
       7   Miscellaneous  (including  macro packages and conventions), e.g.
           man(7), groff(7)
       8   System administration commands (usually only for root)
       9   Kernel routines [Non standard]
```

級別|查找內容
---|---
1|命令
2|內核調用函數
3|函數與數據庫
4|特殊文件（`/dev`下的文件）
5|配置文件（`/etc`下的文件）
6|遊戲
7|其他雜項
8|系統管理員可用命令
9|內核相關文件

### man -f or whatis

綜上所述，我們查找的`ls`是屬於命令的級別，級別為1。如果我們要查找指令的級別的話使用`-f`或是`whatis`如下：

```bash
$ man -f passwd
$ whatis passwd
```

輸出


```bash 
passwd (1)           - update user's authentication tokens
passwd (5)           - password file
sslpasswd (1ssl)     - compute password hashes
```



上面我們查找`passwd`有兩個級別（只查得到有安裝的幫助文檔），但是我們使用`man passwd`，出現的是級別1的內容，因為預設是打開等級最小的文件內容，所以如果要看級別5的內容，要輸入如下：

```bash
$ man 5 passwd
```

透過這樣的查詢，我們就可以查找到我們想要的訊息了。

之後我們發現級別5是配置文件，如果我們要找它的位置只要輸入如下：

```bash
$ whereis passwd
passwd: /usr/bin/passwd /etc/passwd /usr/share/man/man1/passwd.1.gz /usr/share/man/man5/passwd.5.gz
```

其他級別的指令


```bash 
$ whatis ifconfig
ifconfig (8)         - configure a network interface
$ whatis netstat
netstat(1)               - show network status
$ whatis null
BIO_f_null(3ssl)         - null filter
BIO_s_null(3ssl)         - null data sink
DBD::Gofer::Transport::null(3pm) - DBD::Gofer client transport for testing
DBM_Filter::null(3pm)    - filter for DBM_Filter
Net::DNS::RR::NULL(3pm)  - DNS NULL resource record
PPI::Statement::Null(3pm) - A useless null statement
null(4)                  - the null device
null(n)                  - Create and manipulate null channels
openpam_nullconv(3)      - null conversation function
slapd-null(5)            - Null backend to slapd
uuid_clear(3)            - reset value of UUID variable to the NULL value
uuid_is_null(3)          - compare the value of the UUID to the NULL value
```

### man -k or apropos

查找所有相關指令幫助

```bash
$ man -k passwd
$ apropos passwd
```

```bash
CURLOPT_KEYPASSWD(3)     - set passphrase to private key
SSL_CTX_set_default_passwd_cb(3ssl), SSL_CTX_set_default_passwd_cb_userdata(3ssl) - set passwd callback for encrypted PEM file handling
chkpasswd(8)             - verifies user password against various systems
firmwarepasswd(8)        - tool for setting and removing firmware passwords on a system
htpasswd(1)              - Manage user files for basic authentication
kpasswd(1)               - Kerberos 5 password changing program
kpasswdd(8)              - Kerberos 5 password changing server
ldappasswd(1)            - change the password of an LDAP entry
passwd(1)                - modify a user's password
passwd(1ssl)             - compute password hashes
passwd(5), master.passwd(5) - format of the password file
slapd-passwd(5)          - /etc/passwd backend to slapd
slappasswd(8)            - OpenLDAP password utility
```

如果我們是要找`htpasswd`的幫助文檔，但卻忘了指令的名稱，只記得有`passwd`這個字的時候，可以使用`man -k`或`apropos`來查找指令，這個指令會列出所有相關的文檔。

## 其他指令

查找指令的內容還可以使用`info`、`help`可以使用，而查找指令別名或位置還有`whereis`、`which`、`type -a`、`command -v`、`command -V`、`alias`可以使用

### help 和 info

`help`只能夠查詢shell自帶的命令內容

```bash
$ help cd
```

`info`的操作上比較複雜，雖然比較詳細，但是使用上比較複雜而且還有很多要記得一些用法。

- Enter 進入子頁面（在`*`的地方按）
- u 回到上一個頁面
- n 進入下一個小節
- p 進入上一個小節
- q 離開

```bash
$ info ls
```


輸出


```bash 
10.1 'ls': List directory contents
==================================

The 'ls' program lists information about files (of any type, including
............
* Menu:

* ls invocation::               List directory contents.
* dir invocation::              Briefly ls.
* vdir invocation::             Verbosely ls.
* dircolors invocation::        Color setup for ls, etc
.
.
.
```

在這裡按下`u`、`n`會進入下一個、上一個小節，如上如果按下`u`會變成10.2的章節，反之`n`則會回到10.1，離開`info`按`q`。

文檔裡面看到`*`的時候可以按下`Enter`進入別的頁面，返回則按`u`。

###  `whereis`、`which`、`type -a`、`command -v`、`command -V`

```bash
$ whereis cd ##查找位置
/usr/bin/cd
$ which cd ##查找shell自帶指令是會顯示
cd: shell built-in command
$ which ll ##查找別名指令的指令名稱
ll: aliased to ls -lh
```

使用`whereis`我們可以查找指令的位置，`which`則可以查詢別名指令的全名以及是否為shell自帶的指令

 type -a 更方便

```bash
$ type -a cd
cd is a shell builtin
cd is /usr/bin/cd
$ type -a ll
ll is an alias for ls -lh
```

`type -a`和`whereis`&`which`比較起來方便了許多，`type -a`和其他兩個指令不一樣的是，其他兩個指令是搜索`$PATH`找到的，而`type -a`是自己去執行一次的到的，就操作而言`type -a`簡單了不少，一個指令就可以查詢了。

 command -v or -V

```bash
$ command -v cd
cd
$ command -V cd
cd is a shell builtin
$ command -v ll
alias ll='ls -lh'
$ command -V ll
ll is an alias for ls -lh
```

另外還有`command -v or -V`也可以用來查詢，它一樣是搜索`$PATH`找到內容的，優點是比較好記。

