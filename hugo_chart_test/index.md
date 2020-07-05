# Plotly csv 讀取


# 加入自定義 ShortCodes

[Hugo 的文檔](https://gohugo.io/templates/shortcode-templates/)有提到我們可以自己製作`shortcodes`，這篇文章紀錄我把`char.js`放到我自己hugo的過程。



1. `/layouts/shortcodes/<SHORTCODE>.html`
2. `/themes/<THEME>/layouts/shortcodes/<SHORTCODE>.html`


hugo中加入一個檔案`layouts/shortcodes/rawhtml.html`

```html
<!-- raw html -->
{{.Inner}}
```

# 用法

最後只要在文章中加入，其實就是加入html的程式碼而已，之後可以再修改。

```text
{< rawhtml >}
html code， 由於{{ }}， 會錯誤，所以只用一個{}表示
{< /rawhtml >}
```

# python產生plotly的html

python安裝要用到的庫

```sh
conda install pandas
conda install -c plotly plotly
conda install -c conda-forge cufflinks-py 
```

加入iframe之後會跑掉格式，找到一個比較可以的例子：

```html
<!-- plotly html -->
<style>.embed-container { position: relative; padding-bottom: 56.25%;      
    height: 100%; overflow: hidden; max-width: 100%; } .embed-container iframe, 
    .embed-container object, .embed-container embed { position: absolute;   
    top: 0; left: 0; width: 100%; height: 100%; }</style>
    <div class='embed-container'>
        <iframe frameborder='0' scrolling='no' src='/plotly/{ index .Params 0 }.html'></iframe>
    </div>
    
```

加入shortcode，hugo中加入一個檔案`layouts/shortcodes/plotly.html`，檔案放在

```html
<!-- plotly html -->
<style>.embed-container { position: relative; padding-bottom: 56.25%;      
height: 100%; overflow: hidden; max-width: 100%; } .embed-container iframe, 
.embed-container object, .embed-container embed { position: absolute;   
top: 0; left: 0; width: 100%; height: 100%; }</style>
<div class='embed-container'>
{{.Inner}}    
</div>
```

以後直接使用，一樣怕`{{}}`被識別，紀錄就少寫一個，檔案放在`static/plotly/`

```
{< plotly ns3_ofdm_yans_wifi_model>}
```

# 多個trace用pandas更快

這個辦法很快，但是如果要plot子圖的話就還是要用上面的。

{{< plotly  ns3_ofdm_yans_wifi_model>}}


```python
# with plotly + pandas
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0],y=df.columns[1:], title="ns3 ofdm yans wifi model",
template="none", labels=dict( index="", value="success", variable=""),log_x=False, log_y=False, kind='line'
)
fig.update_layout(xaxis_title='SNR(dB)',yaxis_title='Frame Success')
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB")
fig.add_annotation(x=1.1, y=1, text="success transmit") # add note
fig.show()
# fig.write_html("file.html")
```

用matplotlib的不用設定backend，當然除了plotly這個`backend`，pandas還支援其他的backend。


## multiple plot facet_col


{{< plotly ns3_ofdm_yans_wifi_model_col_trace>}}


```python
# with plotly + pandas + subplot col trace
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0],y=df.columns[1:], title="ns3 ofdm yans wifi model col trace",
template="none", labels=dict( index="", value="success", variable=""),log_x=False, log_y=False, kind='line',
facet_col="variable",facet_col_wrap=2 # express way facet_raw="variable", wrap col only
)
fig.update_layout(xaxis_title='SNR(dB)', yaxis_title='Frame Success' ) # showlegend=True
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB")
fig.show()
# fig.write_html("file.html")
```

這個方法雖然很快，不過很多設定還是要用plotly本身的工具:


```python
# with plotly + pandas + make_subplots
from plotly.subplots import make_subplots
import plotly.graph_objects as go
fig = make_subplots(rows=1, cols=2)

for i in range(1, 5):
    fig.add_trace(
        go.Scatter(x=df[df.columns[0]], y=df[df.columns[i]]),
        row=1, col=1
    )
    pass

for i in range(1, 5):
    fig.add_trace(
        go.Scatter(x=df[df.columns[0]], y=df[df.columns[i]]),
        row=1, col=2
    )
    pass

fig.update_layout(title="ns3 ofdm yans wifi model subplot", xaxis_title='SNR(dB)', yaxis_title='Frame Success', template="none")
fig.update_yaxes(exponentformat="power", rangemode="tozero")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB", range=[-3, 10])
fig.show()
# fig.write_html("file.html")
# mode [maker | lines ]
# theme template: ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
# exponentformat "none" | "e" | "E" | "power" | "SI" | "B"
```


# Matplotlib with plotly display

另外Matplotlib也可以用來產生plotly的圖表。

{{< plotly matplotlib_pandas_subplot>}}



```python
# with matplot + plotly.offline
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from plotly.offline import iplot_mpl, init_notebook_mode, enable_mpl_offline
from plotly.offline.offline import plot_mpl

# init_notebook_mode()
# plotly.offline.init_notebook_mode(connected=True)
enable_mpl_offline()

mean = [10,12,16,22,25]
variance = [3,6,8,10,12]
x = np.linspace(0,40,1000)

fig = plt.figure()
for i in range(4):
    sigma = np.sqrt(variance[i])
    y = norm.pdf(x,mean[i],sigma)
    plt.plot(x,y, label=r'$v_{}$'.format(i+1))
    pass

plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Standard Deviation")
plot_mpl(fig, filename='temp-plot.html', auto_open=False)
# plt.show()
```


## Matplotlib pandas subplot




用pandas的時候，要返回`plt.figure()`的物件的方法是用`df.get_figure()`，返回之後就可以plot了。

用`plt_mpl`做的html相對於plotly直接做的有點缺點，大小控制的沒這麼好，我都刪除一個div了還是有一點大小問題。


{{< plotly matplotlib_pandasns3_ofdm_yans_wifi_model>}}



```python
# with matplotlib + pandas
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig =df.plot(x=df.columns[0], y=df.columns[1:])
# plt.show()
plot_mpl(fig.get_figure(), filename='temp-plot.html', auto_open=False)
```

不過也有例外，比如下面這樣寫，`df.get_figure()`我就沒找到，因該是`subplot=True`，加上的關係。

```python

# with matplotlib + pandas
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
# Plotting
fig = df.plot(kind='line', subplots=True, grid=True, title="Sample Data (Unit)",
    layout=(4, 3), sharex=True, sharey=False, legend=False,    
    style=['r', 'r', 'r', 'g', 'g', 'g', 'b', 'b', 'b', 'r', 'r', 'r'],
    xticks=np.arange(0, len(df), 16))

[ax.legend(loc=1) for ax in plt.gcf().axes]
  df.plot(x=df.columns[0], y=df.columns[1:5])

plt.show()
```



# Plotly.js

直接寫的話比較不好寫，需要的cdn

```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```

{{< rawhtml >}}
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<!-- <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.1.0/papaparse.min.js"></script> -->
<div id="myDiv" ></div>

<script>
csv_url = document.location.origin+ '/csv/test.csv';
url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv";
function makeplot() {
  Plotly.d3.csv(url, function(data){ processData(data) } );
};
function processData(allRows) {
  // console.log(allRows);
  var x = [], y = [];
  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['AAPL_x'] );
    y.push( row['AAPL_y'] );
    // x.push( row['t'] );
    // y.push( row['v'] );
  }
  // console.log( 'X',x, 'Y',y);
  makePlotly( x, y);
}

function makePlotly( x, y){
  var traces = [{
    x: x,
    y: y
  }];

  Plotly.newPlot('myDiv', traces,
    {title: 'Plotting CSV data from AJAX call'});
};
  makeplot();
</script>
{{< /rawhtml >}}

```
AAPL_x,AAPL_y
2014-01-02,77.44539475
2014-01-03,77.04557544
2014-01-06,74.89697204
2014-01-07,75.856461
2014-01-08,75.09194679
2014-01-09,76.20263178
2014-01-10,75.2301837
2014-01-13,73.84891755
2014-01-14,75.0113527
2014-01-15,77.14481412
2014-01-16,77.33058367
2014-01-17,76.85652616
2014-01-21,75.39394758
2014-01-22,76.7763823
2014-01-23,76.64038513
2014-01-24,77.20512022
2014-01-27,76.66007339
```

# 讀檔

讀取我自己hugo的檔案：

```js
csv_url = document.location.origin+ '/csv/test.csv';
```

{{< rawhtml >}}
<div id="graph3"></div>

<script>
function linspace(startValue, stopValue, cardinality) {
    var arr = [];
    var step = (stopValue - startValue) / (cardinality - 1);
    for (var i = 0; i < cardinality; i++) {
      arr.push(startValue + (step * i));
    }
    return arr;
  }

t = linspace(1,8,100);
var x1 = new Array;
var x2 = new Array;
for (i = 1; t[i] != t.end; ++i){
    x1.push( Math.sin(t[i]) );
    x2.push(Math.cos(t[i]) );
}

url = document.location.origin+ '/csv/test.csv';
Plotly.d3.csv(url, function(data){
  var x = [], y = []
  for (var i=0; i<data.length; i++) {
    row = data[i];
    x.push( row['t'] );
    y.push( row['v'] );
  }
  // console.log(x)
  // console.log(y)
  var trace1 = {
    x: x,
    y: y,
    name: 'sine from csv data',
    type: 'scatter'
  };
  var trace2 = {
    x: t,
    y: x2,
    name: 'cosine',
    type: 'scatter'
  };
  var data = [trace1,trace2];
  layout = {
    title: 'test dataset',
  };
  Plotly.newPlot('graph3', data, layout);
  var layout = {
    title: 'semilog scale test',
    xaxis: {
      title: 'time(s)',
      type: 'linear',
      autorange: true
    },
    yaxis: {
      title: 'v(t)',
      type: 'log',
      autorange: true
    }
  };
  Plotly.newPlot('graph4', data, layout);
});
</script>
{{< /rawhtml >}}

```html
<div id="graph3"></div>

<script>
function linspace(startValue, stopValue, cardinality) {
    var arr = [];
    var step = (stopValue - startValue) / (cardinality - 1);
    for (var i = 0; i < cardinality; i++) {
      arr.push(startValue + (step * i));
    }
    return arr;
  }

t = linspace(1,8,100);
var x1 = new Array;
var x2 = new Array;
for (i = 1; t[i] != t.end; ++i){
    x1.push( Math.sin(t[i]) );
    x2.push(Math.cos(t[i]) );
}

url = document.location.origin+ '/csv/test.csv';
Plotly.d3.csv(url, function(data){
  var x = [], y = []
  for (var i=0; i<data.length; i++) {
    row = data[i];
    x.push( row['t'] );
    y.push( row['v'] );
  }
  console.log(x)
  console.log(y)
  var trace1 = {
    x: x,
    y: y,
    name: 'sine from csv data',
    type: 'scatter'
  };
  var trace2 = {
    x: t,
    y: x2,
    name: 'cosine',
    type: 'scatter'
  };
  var data = [trace1,trace2];
  Plotly.newPlot('graph3', data, {title: 'test dataset'} );
});
</script>
<div id="graph4"></div>
```

# layout 和 line type

再來title和axis，type的部分，也可以設定，下面是semilog的例子，填到後面layout就可以用了


{{< rawhtml >}}
<div id="graph4"></div>
{{< /rawhtml >}}

```js
var layout = {
  title: 'semilog scale test',
  xaxis: {
    title: 'time(s)',
    type: 'linear',
    autorange: true
  },
  yaxis: {
    title: 'v(t)',
    type: 'log',
    autorange: true
  }
};

Plotly.newPlot('myDiv', data, layout);
```

# suffix

再來是suffix，可以加在前面後面，`showexponent： all`看起來不用加


{{< rawhtml >}}

<div id="graph5"></div>

<script>
var trace1 = {
  x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
  y: [8, 7, 6, 5, 4, 3, 2, 1, 0],
  type: 'scatter'
};

var trace2 = {
  x: [0, 1, 2, 3, 4, 5, 6, 7, 8],
  y: [0, 1, 2, 3, 4, 5, 6, 7, 8],
  type: 'scatter'
};

var data = [trace1, trace2];

var layout = {
  title: 'semilog scale test',
  xaxis: {
    title: 'time(s)',
    type: 'linear',
    tickprefix: '-> ', 
    ticksuffix: ' s', 
    // showexponent: 'all',
    autorange: true
  },
  yaxis: {
    title: 'v(t)',
    type: 'log',
    tickprefix: '-> ', 
    ticksuffix: ' volt', 
    // showexponent: 'all',
    autorange: true
  }
};

Plotly.newPlot('graph5', data, layout);
</script>
{{< /rawhtml >}}

```js
var layout = {
  title: 'semilog scale test',
  xaxis: {
    title: 'time(s)',
    type: 'linear',
    tickprefix: '-> ', 
    ticksuffix: ' s', 
    // showexponent: 'all',
    autorange: true
  },
  yaxis: {
    title: 'v(t)',
    type: 'log',
    tickprefix: '-> ', 
    ticksuffix: ' volt', 
    // showexponent: 'all',
    autorange: true
  }
};
```

上面用的是cpp產生的sine csv。

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

template<typename T>
std::vector<double> linspace(T start_in, T end_in, int num_in)
{

  std::vector<double> linspaced;

  double start = static_cast<double>(start_in);
  double end = static_cast<double>(end_in);
  double num = static_cast<double>(num_in);

  if (num == 0) { return linspaced; }
  if (num == 1) 
    {
      linspaced.push_back(start);
      return linspaced;
    }

  double delta = (end - start) / (num - 1);

  for(int i=0; i < num-1; ++i)
    {
      linspaced.push_back(start + delta * i);
    }
  linspaced.push_back(end); // I want to ensure that start and end
                            // are exactly the same as the input
  return linspaced;
}

void print_vector(std::vector<double> vec)
{
  std::cout << "size: " << vec.size() << std::endl;
  for (double d : vec)
    std::cout << d << " ";
  std::cout << std::endl;
}

int main()
{
  std::ofstream out("test.csv"); // sefl-define
  std::vector< int > arr; // 1d
  std::vector<double>  t = linspace(1,8,100);
  std::vector<double> x;
  print_vector(t);
  out<< 't' << ',' << 'v' << std::endl;
  for (int i = 0; i <= t.size()-1; ++i){
    x.push_back( std::sin(t[i]) );
    out<< t[i] << ',' << x[i] << std::endl;
  }
  print_vector(x);
  out.close();
  return 0;
}
```
