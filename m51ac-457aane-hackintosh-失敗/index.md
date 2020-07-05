# M51AC-457AANE Hackintosh


- 核心：Intel Haswell Core i5-4570(3.2 GHz,turbo 3.6GHz)
- 板子：H87M-PRO
- 記憶體：8GB DDR3
- 顯示介面：NVIDIA GeForce GT630 2GB GDDR3獨顯
- 音效：ALC 892

<!-- more -->

$$
        安裝 
        \begin{cases}
        EFI \ 分割  & \text{Clover Bootloader 開機選單} \\\\
        DSDT \ Free（NO \ DSDT)  & \text{Haswell 以後 CPU 不需要} \\\\
        Bootloader \ Arguments   & \text{dart＝0 disable Bios Vtd} \\\\
        有可能要的 & \text{darkwake=0、npci=0x2000、nv_disable=1 with first boot}
        \end{cases}
$$


# Unibeast USB Installer

- Mac OS X EI Capitan
- UEFI Boot
- ***Inject Nvidia***


> For desktop systems with older NVIDIA graphics cards as GeForce 8xxxx, 9xxxx, 2xx, 4xx, 610, and 630. Equivalent to Chimera/Chameleon GraphicsEnabler=Yes
 
不知道是什麼原因，使用Unibeast安裝並不能使用，進入直接黑屏，連選單都沒有，所以我把USB格式化成Fat32，並用下面指令將安裝檔案複製到隨身碟裡面之後使用clover EFI bootloader安裝Bootloader，但是開機後還是不能進入安裝畫面，雖然比之前Unibeast格式化成Mac OS Extended （Journaled）好一些，還讀的到Bootloader，但是還是給我一個scan entries的訊息，根本進不去，`HFSPlus.efi`，我確實有放進去，但是還是沒有順利進入選單。

```bash
sudo /Applications/Install\ OS\ X\ El\ Capitan.app/Contents/Resources/createinstallmedia --volume /Volumes/UNTITLED --applicationpath /Applications/Install\ OS\ X\ El\ Capitan.app --nointeraction
```

![boot_scaning](/media/boot_scaning.jpg)


# MultiBeast 驅動安裝：

- ALC 892 (for Audio)
- FakeSMC Tool (for Power moniter)

額外安裝下載的 RealtekRTL8111.kext 網卡用 Kext Utility 驗證權限，放到 `/System/Library/Extensions`，若是權限問題再以下面指令安裝：

```bash
sudo chown -R root:wheel /System/Library/Extensions/RealtekRTL8111.kext
```

```bash
sudo chmod -R 755 /System/Library/Extensions/RealtekRTL8111.kext
```
清除 Kext 快取

```bash
rm /System/Library/Extensions.kextcache

rm /System/Library/Extensions.mkext

kextcache -k /System/Library/Extensions
```
# 參考：

[UniBeast: Install macOS Sierra on Any Supported Intel-based PC](https://www.tonymacx86.com/threads/unibeast-install-macos-sierra-on-any-supported-intel-based-pc.200564/)

[How To Install OS X Yosemite Using Clover](https://www.tonymacx86.com/threads/how-to-install-os-x-yosemite-using-clover.144426/)

[Asus H87m pro bios Ami tonymacx86](https://www.tonymacx86.com/threads/asus-h87m-pro-bios-ami.152170/)

[Mac 硬體驅動(.kext)安裝方法](http://bbs.feng.com/read-htm-tid-1449.html)

[Clover安装黑苹果之Config.plist必看](http://www.ithtw.com/8335.html)

[不敢独享，转发解决 黑苹果花屏问题方法！！（部分类型）](http://benyouhui.it168.com/thread-2261865-1-1.html)

[Hackintosh Boot Flags](http://www.fitzweekly.com/2016/04/hackintosh-boot-flags.html?m=1)

[黑苹果引导工具 Clover 配置详解](http://www.jianshu.com/p/b156b0177a24)

[Skylake Skylake Intel HD Graphics Family, Processors and new Macs & Hackintosh](https://www.firewolf.science/2015/08/skylake-intel-hd-graphics-family-processors-new-macs-hackintosh/)

[[GUIDE] Intel HD Graphics 5500 on OS X Yosemite 10.10.3](https://www.firewolf.science/?s=HD+4600)



