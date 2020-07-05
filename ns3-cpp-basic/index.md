# NS3 Cpp Basic


NS3有很多文檔都是用`gnuplot`做繪圖的，這裏Run一個範例，試着在ns3製圖，動態鏈結感覺好用很多，不過暫時還是先存成`csv`再用`matplotlib`出圖

```sh
# 方便debug 略過 unuse variable 之類的問題 cc1plus: all warnings being treated as errors
移除 ns3/build/c4che/_c4che.py 裏面的所有 -Werror
```

# gnuplot

```sh
# 這個範例會產生gnuplot的script file
./waf --run examples/wireless/ofdm-validation # 畫出 yans-frame-success-rate-ofdm.plt
gnuplot yans-frame-success-rate-ofdm.plt # 產生gimp可以用的 yans-frame-success-rate-ofdm.eps
gimp yans-frame-success-rate-ofdm.eps
```

![result](/media/nist-frame-success-rate-ofdm.png)

![Deepin_plasmashell_20200616015518](/media/Peek_2020-06-21_18-09.gif)

# Matplotlib

[參考cpp ](https://openhome.cc/Gossip/CppGossip/UnFormatFileIO.html)

```cpp
/*
ios
|
--istream --|
|           ---ifstream--|
|                        |
|                        |---iostream--|
--ostream --|            |             ---fstream
            ---ofstream--|
*/
#include <iostream> 
#include <fstream> 
std::ofstream out("test.csv"); // sefl-define
out<< "snr(xlabel)" << ',' << "ps(ylabel)" << std::endl;
out<< 0 << ',' << 5.99 << std::endl;
out.close();
```

將這個加入`ofdm-validation.cc`將`yansmodel`的結果存成`test.csv`，我做的修改如下:

```cpp
#include <fstream>
#include <cmath>
#include "ns3/gnuplot.h"
#include "ns3/command-line.h"
#include "ns3/yans-error-rate-model.h"
#include "ns3/nist-error-rate-model.h"
#include "ns3/wifi-tx-vector.h"

using namespace ns3;

int main (int argc, char *argv[])
{
  uint32_t FrameSize = 1500; //bytes
  std::ofstream out("test.csv"); // sefl-define
  // out<< "snr(xlabel)" << ',' << "ps(ylabel)" << std::endl;
  // out<< 0 << ',' << 5.99 << std::endl;
  // out.close();
  std::vector <std::string> modes;

  modes.push_back ("OfdmRate6Mbps");
  modes.push_back ("OfdmRate9Mbps");
  modes.push_back ("OfdmRate12Mbps");
  modes.push_back ("OfdmRate18Mbps");
  modes.push_back ("OfdmRate24Mbps");
  modes.push_back ("OfdmRate36Mbps");
  modes.push_back ("OfdmRate48Mbps");
  modes.push_back ("OfdmRate54Mbps");

  CommandLine cmd;
  cmd.AddValue ("FrameSize", "The frame size in bytes", FrameSize);
  cmd.Parse (argc, argv);
  // introduce the yans and nist rate model // initial class with smart pointer
  Ptr <YansErrorRateModel> yans = CreateObject<YansErrorRateModel> ();
  WifiTxVector txVector; // class defined constructor
  //std::vector< int > arr; // 1d
  //std::vector<std::vector<int>> arr; // 2d
  std::vector<std::vector<double>> x;
  std::vector<std::vector<double>> y;
  // 6, 9, 12, 24, 36, 48, 54 Mbps
  for (uint32_t i = 0; i < modes.size (); i++) 
    {
      std::cout << modes[i] << ' ' << i <<std::endl;
      txVector.SetMode (modes[i]);
      //arr.push_back(std::vector<int>()); // 2d
      x.push_back(std::vector<double>());
      y.push_back(std::vector<double>());
      for (double snr = -5.0; snr <= 30.0; snr += 0.1) // snr -5db ~ 30db
        {
          double ps = yans->GetChunkSuccessRate (WifiMode (modes[i]), txVector, std::pow (10.0,snr / 10.0), FrameSize * 8);
          if (ps < 0.0 || ps > 1.0)
            {
              //error
              exit (1);
            }
          //arr.push_back(snr); // 1d
          //arr[i].push_back(snr); // 2d
          x[i].push_back(snr);
          y[i].push_back(ps); 
          //out<< snr << ',' << ps << std::endl;
        }
    }
  out<< "snr(xlabel)"<<',';
  for (uint32_t i = 0; i < modes.size (); i++) {
    out<< modes[i]<<',';
  } out<< std::endl;
  for (int i = 0; i < (int) x[1].size() ;i++){
    out<< x[1][i]<< ',';
    for (uint32_t j = 0; j < modes.size (); j++) {
      out<< y[j][i]<<',';
    }
    out<< std::endl;
  }
  out.close();
}
```

其中這裏有用到智慧指標（smart pointer）去初始化物件，`Ptr`是ns3 自定義的一個指標，智慧指標的優點是可以自行清理記憶體之類的，不用手動`delete`，當然還有很多設計上的問題，不瞭解就不說了。

```cpp
Ptr <YansErrorRateModel> yans = CreateObject<YansErrorRateModel> ();
```

再來就是`vector`的用法，我是參考[這裏](https://mropengate.blogspot.com/2015/07/cc-vector-stl.html)的，只能說`vector`真的是好用很多，不過對它的瞭解還不是很深就是了，還是會跳warning，debug設定沒設定的話ns3還是會直接不執行。

> 移除 ns3/build/c4che/_c4che.py 裏面的所有 -Werror

再來這裏是用一個物件指標訪問物件成員，下面成員要填什麼這個問題還要思考一下，ns3的文檔還看不是很懂。

```sh
double ns3::YansErrorRateModel::GetChunkSuccessRate	(	WifiMode 	mode,
                                                    WifiTxVector 	txVector,
                                                    double 	snr,
                                                    uint64_t 	nbits 
                                                    )		const
```

- `WifiMode`是我們設定的`modes` vector，裏面存的是字串，這個字串可以指定什麼還要看一下`yansmodel`，看到是這樣的格式`OfdmRate6Mbps`。

- `txVector`是輸入一個Class defined constructor產生的輸入格式之後進行填值後給`yansmodel`。

- $SNR=10^{snr/10}$

- FrameSize就是bits的數量

```cpp
double ps = yans->GetChunkSuccessRate (WifiMode (modes[i]), txVector, std::pow (10.0,snr / 10.0), FrameSize * 8);
```



最後用`pandas`讀取處理並出圖

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./test.csv')
df.plot(x=df.columns[0], y=df.columns[1:])
plt.show()
```

![testplot](/svg/test_ns3plot.svg)

## Enable Boost

boost.python可以讓cpp跟python程式之間可以變量互通，ns3裏面可以使用它，目前還不會用先記錄

> [Boost pyconfig.h](https://stackoverflow.com/questions/19810940/ubuntu-linking-boost-python-fatal-error-pyconfig-cannot-be-found) : 這個檔案的位置在python2裏面，加入`CPLUS_INCLUDE_PATH`，可以解決
>
> [boost.python 用法](https://note.qidong.name/2018/01/hello-boost-python/) 提到`boost.python`用法的複雜程度
>
> [ctypes 動態鏈結方法](https://reptate.readthedocs.io/developers/python_c_interface.html): ctypes 跟 boost都是使用dll的方法去做語言之間的通訊傳值，ns3 compile的部分似乎沒這麼好處理
>
> ```sh
> export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python2.7/" # by find the path
> ```

```sh
find /usr/include -name pyconfig.h
/usr/include/python3.8/pyconfig.h
/usr/include/python2.7/pyconfig.h
/usr/include/python3.7m/pyconfig.h
python --version # anaconda 的
Python 3.7.6
export CPLUS_INCLUDE_PATH="$CPLUS_INCLUDE_PATH:/usr/include/python3.7m/" # 讓boost可以運作
...
# 操作起來挺複雜的略過
# Compile the C file using either，動態鏈結 dll好像都是類似的辦法做的，下面是ctypes的例子
$ gcc -o basic_function_win32.so -shared -fPIC -O2 basic_function.c # Windows
$ gcc -o basic_function_darwin.so -shared -fPIC -O2 basic_function.c # Mac
$ gcc -o basic_function_linux.so -shared -fPIC -O2 basic_function.c # Linux
```

### waf加入boost

```sh
--boost-include=/usr/include/boost/ --boost-libs=/usr/lib/

--with-brite='/run/media/geek/2TB/Documents/PYTHON/NS-3/aquasim-ng_manjaro/bake/source/BRITE/'
# openflow vswitch 要先有boost，其中boost::signals要重新porting成boost::signals2，有點複雜略過
--with-openflow='/run/media/geek/2TB/Documents/PYTHON/NS-3/aquasim-ng_manjaro/openflow/'
```

```sh
./waf configure --with-python=python2 --enable-tests --enable-examples --enable-mpi --enable-des --boost-include=/usr/include/boost/ --boost-libs=/usr/lib/
./waf # build
Checking boost includes                                            : 1_72 
Checking boost libs                                                : lib signals not found in /usr/lib
# boost::signals2 porting有點複雜略過
```


