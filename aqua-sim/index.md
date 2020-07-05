# Aqua-Sim NS3.29 安裝




Aqua-sim 是一個用來模擬UWSNs網路的一個好工具，最近安裝遇到了一些問題，不過最後有裝出來。

我是使用Manjaro進行安裝的，在安裝之前必須先確認自己的電腦有沒有把需要的庫給安裝上了。

我是參考AUR上面的依賴庫一個一個裝上去的，首先先讓NS3可以compile，然後才裝Aqua-sim。

# Aqua-Sim 安裝

之前測試了很多次GitHub上面的檔案，結果最後發現作者並沒有放在Github上面，是放在他的Wiki，而且改了170多個內容（GitLens看到），在安裝之前請先去確定你的NS3可以使用。

![Deepin 截圖_select-area_20200604104358](/media/Deepin_select-area_20200604104358.png)



<!-- more -->

```sh
# 方便debug 略過 unuse variable 之類的問題 cc1plus: all warnings being treated as errors
移除 ns3/build/c4che/_c4che.py 裏面的所有 -Werror
```

```sh
curl -O http://hudson.ccny.cuny.edu/download/aquasim-ng.tgz
tar-zxvf aquasim-ng.tgz
cd aquasim-ng 
(base) ➜  aquasim-ng tree -L 1
.
├── AquaSim-NG_Installation #這裏提到要複製 onoff-application.h
├── bake
├── build.py
├── constants.py
├── netanim-3.108
├── ns-3.29
├── pybindgen-0.17.0.post58+ngcf00cc0
├── README
└── util.py
```

所以使用這個去安裝

```sh
cd aquasim-ng/ns-3.29
find ./src/applications/model/ -name 'onoff-app*'
./src/applications/model/onoff-application-random-destination.cc
./src/applications/model/onoff-application-random-destination.h
./src/applications/model/onoff-application.cc
./src/applications/model/onoff-application.h
cp ./src/applications/model/onoff-application.h ./build/ns3
vim ./src/aqua-sim-ng/model/aqua-sim-signal-cache.cc # creal-> std::real, cexp->exp

./waf clean
./waf configure --build-profile=debug --enable-examples --enable-tests
./waf # build 要有 aqua-sim-ng
Waf: Entering directory `/run/media/geek/2TB/Documents/PYTHON/NS-3/aquasim-ng_manjaro/ns-3.29/build'
wscript:166: Warning: (in /run/media/geek/2TB/Documents/PYTHON/NS-3/aquasim-ng_manjaro/ns-3.29/src/aqua-sim-ng) Requested to build modular python bindings, but apidefs dir not found => skipped the bindings.
  " just like 'make' does by default."),
Waf: Leaving directory `/run/media/geek/2TB/Documents/PYTHON/NS-3/aquasim-ng_manjaro/ns-3.29/build'
Build commands will be stored in build/compile_commands.json
'build' finished successfully (45.893s)

Modules built:
antenna                   aodv                      applications              
aqua-sim-ng               bridge                    brite (no Python)         
buildings                 config-store              core                      
csma                      csma-layout               dsdv                      
dsr                       energy                    fd-net-device             
flow-monitor              internet                  internet-apps             
lr-wpan                   lte                       mesh                      
mobility                  mpi                       netanim (no Python)       
network                   nix-vector-routing        olsr                      
point-to-point            point-to-point-layout     propagation               
sixlowpan                 spectrum                  stats                     
tap-bridge                test (no Python)          topology-read             
traffic-control           uan                       virtual-net-device        
visualizer                wave                      wifi                      
wimax                     

Modules not built (see ns-3 tutorial for explanation):
click                     openflow

./test.py # validating
623 of 627 tests passed (623 passed, 3 skipped, 1 failed, 0 crashed, 0 valgrind errors)
List of SKIPped tests:
    ns3-tcp-cwnd
    ns3-tcp-interoperability
    nsc-tcp-loss
List of FAILed tests:
    pcap-file # 因爲沒有權限使用tcpdump
    
    
$ tcpdump
tcpdump: wlp2s0: You don't have permission to capture on that device
(socket: Operation not permitted)
$ su # 用 --with-python=python2 configure好像會不能使用 --enable-sudo
./test.py # validating
```



- Run Example

  waf-tool python pip 封裝原則上要在`/ns3/scratch/`這個資料夾執行

```sh
cp -R src/aqua-sim-ng/examples/broadcastMAC_example.cc scratch/ 
./waf --run scratch/broadcastMAC_example # --vis
# --build-profile=debug 要configure，讓ns3.commandline可以用
./waf --run "broadcastMAC_example --simStop=1000 --nodes=5 --sinks=2" # 注意`“`符號格式問題

```

![Deepin 截圖_select-area_20200604173838](/media/Deepin_select-area_20200604173838.png)



# PyViz

另外我測試了一下pyviz在上面build

由於pyviz要用到pybindgen，這個東西是要用python2弄的

```sh
./waf configure --enable-tests --enables-examples --with-python=python2
...
# 看到Pyviz: enable 就行
./waf #build
./waf --pyrun src/flow-monitor/examples/wifi-olsr-flowmon.py --vis #Run sample
```

這個東西真的蠻酷的，有動畫的方式顯示做模擬，Node碰久一點還可以看ipaddr之類的模擬參數。

或是使用Anaconda安裝[PyViz](https://anaconda.org/pyviz/pyviz)

```sh
conda install -c pyviz pyviz
./waf configure --enable-tests --enables-examples
./waf --pyrun src/flow-monitor/examples/wifi-olsr-flowmon.py --vis #Run sample
```



![Deepin_plasmashell_20200616015518](/media/Deepin_plasmashell_20200616015518.png)

![Deepin_plasmashell_20200616015518](/media/Peek_2020-06-21_13-37.gif)



# NetAnim

另外還有一個視覺化的工具

```sh
➜  ns-3.29 ./waf --run "dumbbell-animation --nLeftLeaf=5 --nRightLeaf=5 --animFile=dumbbell.xml"
(base) ➜  aquasim-ng_manjaro tree -L 1            
.
├── AquaSim-NG_Installation
├── bake
├── build.py
├── constants.py
├── netanim-3.108
├── ns-3.29
├── pybindgen-0.17.0.post58+ngcf00cc0
├── README
└── util.py
cd netanim-3.108
make clean 
qmake NetAnim.pro
make
./NetAnim
```

![Deepin_plasmashell_20200616030357](/media/Deepin_plasmashell_20200616030357.png)

![Deepin_select-area_20200616030433.png](/media/Deepin_select-area_20200616030433.png)

![Deepin_select-area_20200616030433.png](/media/Peek_2020-06-21_13-33.gif)





# NS3 install

由於NS3需要這些庫所以可能要先安裝一下，這個套件管理這裏沒辦法構建成功，所以要一個個Google一下了。

其中python的部分，因爲我不是很肯定它NS3的3.26~3.29那邊用了python2、python3，所以我都有把pip2、pip3的庫儘量能裝的都裝進去。

```sh
pip2 install pygccxml #例如
pip3 install pygccxml
pip install pygccxml
```

![Deepin 截圖_select-area_20200604180155](/media/Deepin_select-area_20200604180155.png)

![Deepin 截圖_select-area_20200604180218](/media/Deepin_select-area_20200604180218.png)

## NS3 in WSL

在WSL上面裝基本上差不多，不過有點繁瑣，自己裝覺得裝的比Manjaro還要久，一樣是庫、pip套件裝上，configure的地方檢查完有就行build了。

[NS3 Installation](https://www.nsnam.org/wiki/Installation)

不過他要注意一個問題，要加上CXXFLAG，略過一些命名錯誤。

> [Ns-3.28-errata](https://www.nsnam.org/wiki/Ns-3.28-errata)
>
> ```sh
> CXXFLAGS="-Wall -Werror -Wno-parentheses" ./waf configure --enable-examples --enable-tests
> ```

另外要執行PyViz的話要使用下面的設定，`--with-python=python2`。

```sh
CXXFLAGS="-Wall -Werror -Wno-parentheses" ./waf configure --enable-examples --enable-tests --with-python=python2
```

- 下面是在wsl build 的過程

{{< youtube FHd4pBPzXDw >}}

## 安裝Anaconda (Python3)

ns-3.29使用python3，有些不確定哪些還是python2，pip2已經漸漸的快淘汰

```sh
curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-ppc64le.sh
sudo chmod 755 Anaconda3-2020.02-Linux-ppc64le.sh # rwx rwx rwx 給755 都給執行權限
# read write exec Linux三個user group的權限定義 root user other
./Anaconda3-2020.02-Linux-ppc64le.sh # 安裝到 /home/usename/anaconda3/bin/conda 要調用它
export PATH=$PATH:/home/geek/anaconda3/bin
type -a conda
conda is /home/geek/anaconda3/bin/conda
conda update conda
conda init bash # 或是你用zsh, cmd.exe 環境變量自動加到 *.bashrc, *.zshrc, windows path foloder
```

[我的Linux筆記，一些基本筆記](https://shihchun.github.io/categories/linux/)

## Mercurial hg clone

```sh
sudo pacman -S mercurial
hg clone http://..... # ns3 有些資料要用mercurial下載
hg clone http://code.nsnam.org/jabraham3/ns-3-win2 #example

# windows 上
# install chocolatey
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# then install the hg
choco install hg
```



## NS3 install and Build (Bassic)

Manjaro（*Arch Linux* 的Linux 發行版）上安裝3.24~3.26版本的NS-3，~~aqua-sim是使用舊版的NS3（python2去做compile），所以使用的python要加上alias讓shell知道我們是使用python2來做compile~~

> Begin by downloading ns-3 (version 3.24~3.26 have been tested with aqua-sim-ng) from
>
> [here](https://www.nsnam.org/releases/ns-3-29/) 
>
> [Github Release(https://github.com/nsnam/ns-3-dev-git/releases)

```sh
# 我直接複製下載鏈接網址
curl -O https://www.nsnam.org/release/ns-allinone-3.26.tar.bz2
wget https://github.com/nsnam/ns-3-dev-git/archive/ns-3.29.tar.gz # github
wget http://www.nsnam.org/release/ns-allinone-3.30.tar.bz2 # 官網
git clone https://github.com/nsnam/ns-3-dev-git.git # 最新
# 3.29之後用Manjaro試過的都可以compile過
###############################################################################
# tar -z 包cvf 解xvf tar.gz
# tar -j 包cvf 解xvf tar.bz2
tar -jxvf ns-allinone-3.29.tar.bz2 
cd ns-allinone-3.29/ns-3.29

ls -lh | grep "waf"
-rwxrwxrwx 1 geek geek 100K  6月  3 15:10 waf
-rwxrwxrwx 1 geek geek   28  6月  3 15:10 waf.bat	# windows 用
drwxrwxrwx 1 geek geek 4.0K  6月  3 15:10 waf-tools

./waf configure --enable-examples
./waf build # C語言編譯 ./configure, make, make install 已經包裝成./waf裏面 應該吧。。。。

[0001/2402] ...
...
...
[2400/2402] Compiling src/fd-net-device/helper/encode-decode.cc
[2401/2402] Compiling src/fd-net-device/helper/tap-device-creator.cc
[2402/2402] Linking build/src/fd-net-d
[2403/2406] Compiling src/fd-net-device/helper/creator-utils.cc
[2404/2406] Compiling src/fd-net-device/helper/encode-decode.cc
[2405/2406] Compiling src/fd-net-device/helper/raw-sock-creator.cc
[2406/2406] Linking build/src/fd-net-device/ns3-dev-raw-sock-creator-debug
[2407/2409] Compiling src/tap-bridge/model/tap-encode-decode.cc
[2408/2409] Compiling src/tap-bridge/model/tap-creator.cc
[2409/2409] Linking build/src/tap-bridge/ns3-dev-tap-creator-debug
Waf: Leaving directory `/run/media/geek/2TB/Documents/PYTHON/NS-3/ns-3-dev-git/build'
Build commands will be stored in build/compile_commands.json
'build' finished successfully (3m23.327s)

Modules built:
antenna                   aodv                      applications
bridge                    buildings                 config-store
core                      csma                      csma-layout
dsdv                      dsr                       energy
fd-net-device             flow-monitor              internet
internet-apps             lr-wpan                   lte
mesh                      mobility                  netanim
network                   nix-vector-routing        olsr
point-to-point            point-to-point-layout     propagation
sixlowpan                 spectrum                  stats
tap-bridge                test (no Python)          topology-read
traffic-control           uan                       virtual-net-device
wave                      wifi                      wimax

Modules not built (see ns-3 tutorial for explanation):
brite                     click                     mpi
openflow                  visualizer
ns3-dev-tap-bridge-debug.so
```

![Deepin 截圖_plasmashell_20200602203521](/media/Deepin_plasmashell_20200602203521.png)

```sh
./waf --run simple-global-routing
Waf: Entering directory `/run/media/geek/2TB/Documents/PYTHON/NS-3/ns-allinone-3.29/ns-3.29/build'
Waf: Leaving directory `/run/media/geek/2TB/Documents/PYTHON/NS-3/ns-allinone-3.29/ns-3.29/build'
Build commands will be stored in build/compile_commands.json
'build' finished successfully (1.882s)
```

![Deepin 截圖_select-area_20200602203815](/media/Deepin_select-area_20200602203815.png)

```sh

(base) ➜  NS-3 tree -L 1
.
├── aqua-sim-ng   # 要執行/examples/broadcastMAC_example.cc
└── ns-allinone  # ./waf在這裏 要把Models 丟到/src這裏使用

2 directories, 0 files
```



## waf Run Examples

build samples

```sh
(base) ➜  ns-allinone-3.29/ns-3.29 git:(master) # directory
cp -R examples/tutorial/first.cc scratch/ # 把example移動在ns-3-dev-git/scratch

## 這樣不行
./waf --run scratch/first.cc # get error 不能打 *.cc
program 'scratch/first.cc' not found; available programs are: ['first', 'scratch/first', 'scratch-simulator', 'scratch/scratch-simulator', 'subdir', 'scratch/subdir/subdir', 'test-runner', 'utils/test-runner', 'bench-simulator', 'utils/bench-simulator', 'bench-packets', 'utils/bench-packets', 'print-introspected-doxygen', 'utils/print-introspected-doxygen', 'tap-device-creator', 'src/fd-net-device/tap-device-creator', 'raw-sock-creator', 'src/fd-net-device/raw-sock-creator', 'tap-creator', 'src/tap-bridge/tap-creator']

## 要這樣執行
#./waf --python=/usr/bin/python2 configure #...# 或是alias python='python2'
./waf --run scratch/first # 去除副檔名 加上-v 或是--vis 看更多debug訊息
Waf: Entering directory `/home/geek/ns-allinone-3.29/ns-3.29/build'
[1861/1913] Compiling scratch/first.cc
[1863/1913] Compiling scratch/scratch-simulator.cc
[1870/1913] Compiling scratch/subdir/scratch-simulator-subdir.cc
[1872/1913] Linking build/scratch/scratch-simulator
[1873/1913] Linking build/scratch/subdir/subdir
[1874/1913] Linking build/scratch/first
Waf: Leaving directory `/home/geek/ns-allinone-3.29/ns-3.29/build'
Build commands will be stored in build/compile_commands.json
'build' finished successfully (2.395s)
At time 2s client sent 1024 bytes to 10.1.1.2 port 9
At time 2.00369s server received 1024 bytes from 10.1.1.1 port 49153
At time 2.00369s server sent 1024 bytes to 10.1.1.1 port 49153
At time 2.00737s client received 1024 bytes from 10.1.1.2 port 9
```

其中下面這部分是Example的執行結果

```sh
At time 2s client sent 1024 bytes to 10.1.1.2 port 9
At time 2.00369s server received 1024 bytes from 10.1.1.1 port 49153
At time 2.00369s server sent 1024 bytes to 10.1.1.1 port 49153
At time 2.00737s client received 1024 bytes from 10.1.1.2 port 9
```





