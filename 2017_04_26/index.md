# Linux關機命令

## shutdown

shutdown [option] [time]

option:

- `-c` 取消關機命令
- `-h` 關機
- `-r` 重新開機

```bash
$ shutdown now
$ shutdown -r now
```

<!---more--->

```bash
[cyberjun@localhost ~]$ shutdown -r 05:30
Must be root.
[cyberjun@localhost ~]$ su
密碼：
[root@localhost cyberjun]# shutdown -r 05:30
Shutdown scheduled for 五 2017-04-28 05:30:00 CST, use 'shutdown -c' to cancel.
[root@localhost cyberjun]# shutdown -c

Broadcast message from root@localhost.localdomain (Thu 2017-04-27 17:21:20 CST):

The system shutdown has been cancelled at Thu 2017-04-27 17:22:20 CST!
```

shutdown的關機比較安全，如果可以的話還是使用shutdown來關機，如果有打開一些伺服器、網路接口之類的就必須先關掉在關機會比較安全。

## half、poweroff、init 0 

```bash
# halt
# poweroff
# init 0
```

直接關機，這三個指令和shutdown比起來爛了不少，如果可以用shutdown就用shutdown，上面三個指令執行會有一些資料沒有貯存。

## 其他重啟命令

```bash
# reboot
# init 6
```

## init 運行級別

```bash
$ man init
```

其中內容

```bash 
SIGHUP
           Reloads the complete daemon configuration. This is mostly
           equivalent to systemctl daemon-reload.

       SIGRTMIN+0
           Enters default mode, starts the default.target unit. This is mostly
           equivalent to systemctl start default.target.

       SIGRTMIN+1
           Enters rescue mode, starts the rescue.target unit. This is mostly
           equivalent to systemctl isolate rescue.target.

       SIGRTMIN+2
           Enters emergency mode, starts the emergency.service unit. This is
           mostly equivalent to systemctl isolate emergency.service.

       SIGRTMIN+3
           Halts the machine, starts the halt.target unit. This is mostly
           equivalent to systemctl start halt.target.
SIGRTMIN+4
           Powers off the machine, starts the poweroff.target unit. This is
           mostly equivalent to systemctl start poweroff.target.

       SIGRTMIN+5
           Reboots the machine, starts the reboot.target unit. This is mostly
           equivalent to systemctl start reboot.target.

       SIGRTMIN+6
           Reboots the machine via kexec, starts the kexec.target unit. This
           is mostly equivalent to systemctl start kexec.target.
.
.
.
```

級別|動作
---|---
0|關機
1|救援模式
3|進入文字界面
5|進入GUI模式
6|重新開機

如果要查詢現在界面所在的級別可以執行`runlevel`；注意！我是使用CentOS來舉例，如果是Debian的系統就不一樣了，要自己去用`man`查詢。

```bash
$ runlevel
N 3 ##在文字界面
```

如果要設定開機之後進入的級別可以找`/etc/inittab`文件看一下，其中級別0和級別6，是不能設定在裡面的，如果設定了，初學者大概只有重新安裝這個辦法了。

```bash
$ cat /etc/inittab
# inittab is no longer used when using systemd.
#
# ADDING CONFIGURATION HERE WILL HAVE NO EFFECT ON YOUR SYSTEM.
#
# Ctrl-Alt-Delete is handled by /usr/lib/systemd/system/ctrl-alt-del.target
#
# systemd uses 'targets' instead of runlevels. By default, there are two main targets:
#
# multi-user.target: analogous to runlevel 3
# graphical.target: analogous to runlevel 5
#
# To view current default target, run:
# systemctl get-default
#
# To set a default target, run:
# systemctl set-default TARGET.target
#
id:3:initdefault:
```

## 退出登錄

>Linux支援256個遠端登錄，Windows XP 1個、Windows Sever 2003 2個、Windows Sever 2008 4~8個

如果我們遠端登入沒有登出的話會造成下一次可能登入不了的問題，舉一個例子，如果我用Windows XP遠端登入，然後我們直接關掉，沒有登出，直接關掉終端機，在下一次登入的時候，有可能會登不進去，因為Windows XP只能一個遠端登入，所以登出是很重要的習慣。

```bash
# logout
```
