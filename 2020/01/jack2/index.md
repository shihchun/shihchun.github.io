# Jack2+cadence 低延遲輸出


{{< youtube -yA2ZmRfW7o >}}

# 安裝Jack2、qJackCtl、cadence

我是使用Manjaro community的版本。

然後打開qjackCtl設備調整成地延遲的DAC設備。

![](/media/Screenshot_from_2020-01-13_14-51-22.png)

再來設定cadence

![](/media/Screenshot_from_2020-01-13_14-52-10.png)

![](/media/Screenshot_from_2020-01-13_14-52-54.png)


另外如果之後重新開機之後如果cadence沒有啟動的話，可以試試看這個指令：

```sh
cadence-session-start --system-start
```

會發生這種狀況是因為`Auto-start JACK or LADISH at login`這個選項造成的，你會發現重新開機之後你的聲音驅動全部不見了，如果手動打開的話問題就不大，應該是官方想要整合其他的設定結果開啟的時候少了什麼，至於其他更多的設定也可以玩玩看，整體上使用起來還是不錯的。

# airwave 和 windws vst

首先必須先在wine的系統裡面安裝windows的vst。

```sh
wine xxx.exe
mv plugin ~/.wine/drive_c/plugins #*.dll vst file if have
```

再來就是airwave wine plugin了

![](/media/Screenshot_from_2020-01-13_15-03-00.png)

其中有兩個東西要設定，分別是`VST plugin`和`Link location`

`VST plugin`就是你VST plugin的 `*.dll`的檔案

`Link location`則是airwave要在哪裡給DAWs存取。

例如我設定在`/home/geek/.vst`，DAWs就要在這裡找plugin，下面是Tracktion 7 的例子

![](/media/Screenshot_from_2020-01-13_15-09-27.png)

