# Hugo 加入 chart.js、plotly.js



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

最後只要在文章中加入，其實就是加入html的程式碼而已。

```text
{< rawhtml >}
html code， 由於{{ }}， 會錯誤，所以只用一個{}表示
{< /rawhtml >}
```

{{< rawhtml >}}
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.1.0/papaparse.min.js"></script>
<div id="myDiv" ></div>

<script>
function makeplot() {
  Plotly.d3.csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv", function(data){ processData(data) } );

};

function processData(allRows) {

  console.log(allRows);
  var x = [], y = [], standard_deviation = [];

  for (var i=0; i<allRows.length; i++) {
    row = allRows[i];
    x.push( row['AAPL_x'] );
    y.push( row['AAPL_y'] );
  }
  console.log( 'X',x, 'Y',y, 'SD',standard_deviation );
  makePlotly( x, y, standard_deviation );
}

function makePlotly( x, y, standard_deviation ){
  var plotDiv = document.getElementById("plot");
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

# chart.js 用法

下面是`chart.js`範例使用的程式碼。




{{< rawhtml >}}
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-colorschemes"></script>
<canvas id="myChart" width="300" height="300" ></canvas>
<script>
function roundXX(val, precision) {
  return Math.round(Math.round(val * Math.pow(10, (precision || 0) + 1)) / 10) / Math.pow(10, (precision || 0));
}
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
// draw
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: t,
        datasets: [{
            data: x1,
            label: 'sine',
            borderColor: 'blue',
            pointStyle: 'rect',
            // backgroundColor: 'green',
            fill: false
        },
        {
            data: x2,
            label: 'cosine',
            borderColor: 'green',
            pointStyle: 'triangle',
            // backgroundColor: 'green',
            fill: false
        }
        ],
    },
    // Configuration options go here
    options: {
      title: {
          display: true,
          text: 'A sine wave test',
          fontSize: 14,
        },
      // legend: {
      //     display: true,
      //   },
      // maintainAspectRatio: true,
      scales: {
          xAxes: [{
            // beginAtZero: false,
            scaleLabel: {
              display: true,
              labelString: 'time(s)'
            },
            // gridLines: {
            //   display: true,
            // },
            ticks: {
              // max: 100,
              // min: 0,
              // beginAtZero: false,
              maxTicksLimit: 7,
              maxRotation: 0, // 資料多會自動轉向
              minRotation: 0,
              precision: 0,
              callback: function(value, index, values) {
              //    if (Math.floor(value) === value) { // 只擷取整數的部分
                     return roundXX(value,2) + ' 秒';
                //  }
              },
            }
          }],
          yAxes: [{
            // beginAtZero: false,
            scaleLabel: {
              display: true,
              labelString: 'voltage'
            },
            // gridLines: {
            //   display: true,
            // },
            ticks: {
              // max: 100,
              // min: 0,
              // precision: 0, 不用stepSize時，將yAxes取整數
              stepSize: 0.25,
              beginAtZero: false,
            }
          }]
        },
    }
});
</script>
{{< /rawhtml >}}


```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<canvas id="myChart" width="300" height="300"></canvas>
<script>
function roundXX(val, precision) {
  return Math.round(Math.round(val * Math.pow(10, (precision || 0) + 1)) / 10) / Math.pow(10, (precision || 0));
}
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
// draw
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',
    // The data for our dataset
    data: {
        labels: t,
        datasets: [{
            data: x1,
            label: 'sine',
            borderColor: 'blue',
            pointStyle: 'rect',
            // backgroundColor: 'green',
            // fill: false
        },
        {
            data: x2,
            label: 'cosine',
            borderColor: 'green',
            pointStyle: 'triangle',
            // backgroundColor: 'green',
            // fill: false
        }
        ],
    },
    // Configuration options go here
    options: options_sets
});
```

`chart.js` 設定的部分，比較麻煩，整理了一下，以後用貼的應該還是不會太久，比較需要注意的大概是ticks地方。

```js
options_sets= {
      title: {
          display: true,
          text: 'A sine wave test',
          fontSize: 14,
        },
      // legend: {
      //     display: true,
      //   },
      // maintainAspectRatio: true,
      scales: {
          xAxes: [{
            // beginAtZero: false,
            scaleLabel: {
              display: true,
              labelString: 'time(s)'
            },
            // gridLines: {
            //   display: true,
            // },
            ticks: {
              // max: 100,
              // min: 0,
              // beginAtZero: false,
              maxTicksLimit: 7, // stepSize 不會運作，用這個
              maxRotation: 0, // 資料多會自動轉向
              minRotation: 0,
              callback: function(value, index, values) {//透過callback fcn加入一些別的符號
              //    if (Math.floor(value) === value) { // 只擷取整數的部分
                     return roundXX(value,2)+' 秒';
                //  }
              },
            }
          }],
          yAxes: [{
            // beginAtZero: false,
            scaleLabel: {
              display: true,
              labelString: 'voltage'
            },
            // gridLines: {
            //   display: true,
            // },
            ticks: {
              // max: 100,
              // min: 0,
              stepSize: 0.25,
              beginAtZero: false,
            }
          }]
        },
    }
```

# chart.js 自動配色 colorschemes

[chartjs-plugin-colorschemes](https://nagix.github.io/chartjs-plugin-colorschemes/)自動配色，記得加上cdn:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-colorschemes"></script>
```

{{< rawhtml >}}
<canvas id="myChart2" width="300" height="300"></canvas>
<script>
t2 = linspace(1,8,100);
var x3 = new Array;
var x4 = new Array;
for (i = 1; t2[i] != t2.end; ++i){
    x3.push( Math.sin(t2[i]) );
    x4.push(Math.cos(t2[i]) );
}
var ctx = document.getElementById('myChart2').getContext('2d');
var chart = new Chart(ctx, {
  type: 'line',
  data: {
        labels: t2,
        datasets: [{
            data: x3,
            label: 'sine',
            fill: false
        },
        {
            data: x4,
            label: 'cosine',
            fill: false
        }
        ],
    },
    options: {
      scales: {
          xAxes: [{
            scaleLabel: { display: true, labelString: 'time(s)' },
            ticks: {
              maxTicksLimit: 7, maxRotation: 0, minRotation: 0, callback: function(value, index, values) {return roundXX(value,2)+' 秒';} 
              } }],
          yAxes: [{ scaleLabel: { display: true, labelString: 'voltage' } }]
              },
       plugins: {
         colorschemes: {
           scheme: 'office.Angles6'
         }
      }
  }
});
</script>
{{< /rawhtml >}}

```html
<canvas id="myChart2" width="300" height="300"></canvas>
<script>
t2 = linspace(1,8,100);
var x3 = new Array;
var x4 = new Array;
for (i = 1; t2[i] != t2.end; ++i){
    x3.push( Math.sin(t2[i]) );
    x4.push(Math.cos(t2[i]) );
}
var ctx = document.getElementById('myChart2').getContext('2d');
var chart = new Chart(ctx, {
  type: 'line',
  data: {
        labels: t2,
        datasets: [{
            data: x3,
            label: 'sine',
            fill: false
        },
        {
            data: x4,
            label: 'cosine',
            fill: false
        }
        ],
    },
    options: {
      scales: {
          xAxes: [{
            scaleLabel: { display: true, labelString: 'time(s)' },
            ticks: {
              maxTicksLimit: 7, maxRotation: 0, minRotation: 0, callback: function(value, index, values) {return roundXX(value,2)+' 秒';} 
              } }],
          yAxes: [{ scaleLabel: { display: true, labelString: 'voltage' } }]
              },
       plugins: {
         colorschemes: {
           scheme: 'office.Angles6'
         }
      }
  }
});
</script>
```


# Plotly 

除了chart.js以外還有plotly可以拿來畫圖，就用法還有使用性上的話plotly在python上面也可以使用，感覺學起來比較好，功能也很多，文檔也蠻多的。

下面是一個plotly的範例，比較嚴重的缺點就是在手機上瀏覽可能效果會很差。

{{< rawhtml >}}
 <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
 <div id="graph" ></div>
 <script>
var n = 100;
var x = [], y = [], z = [];
var dt = 0.015;
for (i = 0; i < n; i++) {
  x[i] = Math.random() * 2 - 1;
  y[i] = Math.random() * 2 - 1;
  z[i] = 30 + Math.random() * 10;
}
Plotly.plot('graph', [{
  x: x,
  y: z,
  mode: 'markers'
}], {
  xaxis: {range: [-40, 40]},
  yaxis: {range: [0, 60]}
}, {showSendToCloud:true})
function compute () {
  var s = 10, b = 8/3, r = 28;
  var dx, dy, dz;
  var xh, yh, zh;
  for (var i = 0; i < n; i++) {
    dx = s * (y[i] - x[i]);
    dy = x[i] * (r - z[i]) - y[i];
    dz = x[i] * y[i] - b * z[i];
    xh = x[i] + dx * dt * 0.5;
    yh = y[i] + dy * dt * 0.5;
    zh = z[i] + dz * dt * 0.5;
    dx = s * (yh - xh);
    dy = xh * (r - zh) - yh;
    dz = xh * yh - b * zh;
    x[i] += dx * dt;
    y[i] += dy * dt;
    z[i] += dz * dt;
  }
}
function update () {
  compute();
  
  Plotly.animate('graph', {
    data: [{x: x, y: z}]
  }, {
    transition: {
      duration: 0,
    },
    frame: {
      duration: 0,
      redraw: false,
    }
  });
  requestAnimationFrame(update);
}
requestAnimationFrame(update);
 </script>
{{< /rawhtml >}}

{{< rawhtml >}}
<div id="graph2"></div>
<script>
var trace1 = {
  x: t2,
  y: x3,
  type: 'scatter'
};
var trace2 = {
  x: t2,
  y: x4,
  type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('graph2', data);
</script>
{{< /rawhtml >}}

```js
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
<div id="graph2"></div>
<script>
var trace1 = {
  x: t2,
  y: x3,
  name: 'sine',
  type: 'scatter'
};
var trace2 = {
  x: t2,
  y: x4,
  name: 'cosine',
  type: 'scatter'
};
var data = [trace1, trace2];
Plotly.newPlot('graph2', data);
</script>
```

調整圖表，將[Layout的部分](https://plotly.com/javascript/tick-formatting/)填入，使用layout的話不只是要多寫一些code以外，框選圖表的話，tick也不會更新新的位置了，所以大概不要調整比較好吧，除了不能在手機上友好的顯示，plotly還是不錯用的。


```js
Plotly.newPlot('graph2', data, layout);
var layout = {
  xaxis: {
    tick0: 0.5,
    dtick: 0.75
  }
}
Plotly.newPlot('graph2', data, layout);
```

{{< rawhtml >}}
<div id="graph3"></div>
<script>
var trace1 = {
  x: t2,
  y: x3,
  name: 'sine',
  type: 'scatter'
};
var trace2 = {
  x: t2,
  y: x4,
  name: 'cosine',
  type: 'scatter'
};
var layout = {
  xaxis: {
    tick0: 0.01, // resolution
    dtick: 0.5 // stepSize
  }
}
var data = [trace1, trace2];
Plotly.newPlot('graph3', data, layout);
</script>
{{< /rawhtml >}}





# CSV 讀取

c++ 產生的資料：

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


在讀取之前我們先知道，hugo的static file在`hugo_directory/static/`

所以如果我把檔案放在`hugo_directory/static/csv/test.csv`，會在`http://localhost:1313/csv/test.csv`可以訪問。

透過一些方法可以的到當前的URL

```js
console.log(document.URL); // http://localhost:1313/2020/06/hugo_char/
console.log(document.location.origin); // http://localhost:1313/
csv_url = document.location.origin+ '/csv/test.csv'; //http://localhost:1313/csv/test.csv
```

`XMLHttpRequest`、`jQuery`、`jQuery.ajax()`，好像都蠻多人使用的，聽說`ajax`是在我們Gmail剛出現的時候讓很多開發人員感到驚艷，所以開始一堆在用的，`ajax`可以實現非同步`async=true`的程式執行，預設的時候你做的script內容都是用非同步的方式進行，這樣的話不會有資源加載的時候等待主要線程跑完才能執行下一步程式的問題，將簡單一點就是方便的工具。

我的hugo並沒有用到jQuery，也沒有必要每次執行圖表特別加載它，所以我就有調用到`Promise`的參考範例來加入非同步的功能，沒有在做Web就不糾結那些了，做個紀錄。

先讀取資料：

```js
//var csv is the CSV file with headers
function csvJSON(csv){
  var lines=csv.split("\n");
  var result = [];
  var headers=lines[0].split(",");
  for(var i=1;i<lines.length;i++){
	  var obj = {};
	  var currentline=lines[i].split(",");
	  for(var j=0;j<headers.length;j++){
		  obj[headers[j]] = currentline[j];
	  }
	  result.push(obj);
  }
  //return result; //JavaScript object
  return JSON.stringify(result); //JSON
}

csv_url = document.location.origin+ '/csv/'; 

function getURL(URL) {
   return new Promise(function(resolve, reject){
      var xhr = new XMLHttpRequest();
      xhr.open('get',csv_url+URL);
      xhr.send(null)
      xhr.onload = function(){
         // resolve(xhr.responseText);
         // console.log(xhr.responseText);
         resolve(JSON.parse(csvJSON(xhr.responseText)));
      }
   });
}

// init
var data = getURL('test.csv'); //xhttprequest xhr 返回一個 Promise
// Promise.resolve 判定陣列方法為 `.then(function(v){console.log(v)})`
// JS 討厭的地方就是動不動就是一堆巢狀迴圈
data.then(function(v){console.log(v[0])})
```

抓多個檔案，用`Promise.all`解決：

```js
var data = getURL('test.csv');
var data2 = getURL('test.csv');

Promise.all([data, data2]).then(function(results){
   var originData =[]; // json push 成可以 plot 的 array
   originData.push(['第一筆資料'].concat(results[0])) // 時間
   originData.push(['第二筆資料'].concat(results[1])) // 大小
   load(originData);
})
```

再來是資料格式的問題，python的話可以使用列表解析方式（list comprehension）製作一個新的List，JavaScript

![2020-06-27_AM_3.25.28](/media/2020-06-27_AM_3.25.28.png)

方法主要是[在這裡](https://segmentfault.com/q/1010000018557544)看到的，做個紀錄，由於我的讀取csv會自動轉換第一個header所以我就直接將header輸入我的csv，寫這個很浪費時間。

```js
var data = getURL('test.csv');
data.then(function(v){
  console.log(v[0]);
  console.log(v['1']);
  // 兩個結果都是
  // {1: "3", 0.841471: "0.14112"}
  //   0.841471: "0.14112"
  //   1: "3"
  // obj[key]['name']]=obj[key] 用for的方式去修改就行
  // 具體的方法是用 Object.keys(obj).forEach(key=>{if(...)}) 請參考箭頭函數
  console.log(Object.keys(v))
  // ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", …]
  console.log(v);
  })
```

我就直接在csv上面加入，Surprise！csv讀出來不行用得到了一個`undefined`的值

```js
// t,v
// 1,0.841471
data.then(function(v){ 
  console.log(typeof(v));
  console.log(v);
  // 0: {t: "1", "v ": "0.841471"}
  // 1: {t: "2", "v ": "0.909297"}
  // 2: {t: "3", "v ": "0.14112"}
  // 3: {t: "4", "v ": "-0.756802"}
  console.log(v[0]);
  // {t: "1", "v": "0.841471" } 
  console.log( v[0]['t'] );
  // "1"
  console.log( v[0]['v'] );
  // undefined
  var time = [];
  var voltage = [];
  Object.keys(v).forEach(key=>{ time.push( parseFloat(v[key]['t'])); voltage.push(parseFloat(v[key]['v'])); });
  // voltage undefined
```

## Papa.js

雖然看起來csv json轉換的function沒什麼問題不過，好像是不行用的，最後還是不鐵齒了，就用最後我用char.js上面使用的Papa.js的作法：

改寫一下

```js
function getURL(URL) {
   return new Promise(function(resolve, reject){
      var xhr = new XMLHttpRequest();
      xhr.open('get',csv_url+URL);
      xhr.send(null)
      xhr.onload = function(){
        // console.log(xhr.responseText);
        // resolve(JSON.parse(csvJSON(xhr.responseText)));
        csvff= csv({output: "csv"}).fromString(xhr.responseText).then(function(result){ return result });
        var data = Papa.parse(xhr.responseText).data;
        console.log(data);
        // 得到這個
        // 0: (2) ["t", "v"]
        // 1: (2) ["1", "0.841471"]
        // 2: (2) ["2", "0.909297"]
        // 3: (2) ["3", "0.14112"]
        // 4: (2) ["4", "-0.756802"]
        resolve( data ); // 給promise，回傳.them(fuction(v){})這個cb fcn 後用 for 處理
      }
   });
}
```

{{< rawhtml >}}
<!-- Load PapaParse to read csv files -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.1.0/papaparse.min.js"></script>

<script>
csv_url = document.location.origin+ '/csv/'; 

function getURL(URL) {
   return new Promise(function(resolve, reject){
      var xhr = new XMLHttpRequest();
      xhr.open('get',csv_url+URL);
      xhr.send(null)
      xhr.onload = function(){
        var data = Papa.parse(xhr.responseText).data;
        // console.log(data);
        // 得到這個
        // 0: (2) ["t", "v"]
        // 1: (2) ["1", "0.841471"]
        // 2: (2) ["2", "0.909297"]
        // 3: (2) ["3", "0.14112"]
        // 4: (2) ["4", "-0.756802"]
        resolve( data ); // 給promise，回傳.them(fuction(v){})這個cb fcn 後用 for 處理
      }
   });
}

var time = [];
var voltage = [];
var plot_data = [];
// init
var data = getURL('test.csv');
var plot_data = data.then(function(v){ 
  // console.log(v[0][1])
  // console.log(v.length)
  for (var i = 1; i < v.length; i++) {
    // time.puch( v[i][0] );
    time.push( v[i][0] );
    voltage.push( v[i][1] );
   }
  plot_data = {
    't': time, // plot_data.t 叫出一個Array
    'v': voltage
   };
  return plot_data
});
// console.log('plot_data');
// console.log(plot_data);
</script>
<div id="graph4"></div>
<script>
console.log('可以plot的 t2,x3');
console.log(x3)
console.log("不行plot的，plot_data['t'], plot_data['v']");
console.log(voltage)
var trace1 = {
  x: t2,
  y: x3,
  name: 'sine',
  type: 'scatter'
};
var data = [trace1];
Plotly.newPlot('graph4', data);
</script>
<canvas id="myChart3" width="300" height="300"></canvas>
<script>
var plot_data = []
for (var i = 1; i < time.length; i++) {
   plot_data.push( {
           labels: time[i],
           datasets: [{
               data: voltage[i],
               label: 'sine',
               fill: false
           }
           ],
       });
    }
var ctx = document.getElementById('myChart3').getContext('2d');
data
var chart = new Chart(ctx, {
  type: 'line',
  data: plot_data,
    options: {
      scales: {
          xAxes: [{
            scaleLabel: { display: true, labelString: 'time(s)' },
            ticks: {
              maxTicksLimit: 7, maxRotation: 0, minRotation: 0, callback: function(value, index, values) {return roundXX(value,2)+' 秒';} 
              } }],
          yAxes: [{ scaleLabel: { display: true, labelString: 'voltage' } }]
              },
       plugins: {
         colorschemes: {
           scheme: 'office.Angles6'
         }
      }
  }
});
</script>

{{< /rawhtml >}}


chart.js 官方用 jQuery，下面是範例，我的hugo沒有用到它，所以就不用jQuery跑了，這個地方資料切片的方式還蠻不錯，Papa.js也讓我可以成功使用它們了，資料格式處理果然不要自己來比較好，記錄一下。

```html
<script>
csv_url = document.location.origin+ '/csv/test.csv';

$(document).ready(function() {
  // Read data file and create a chart
  $.get(csv_url, function(csvString) {
    var data = Papa.parse(csvString).data;
    var timeLabels = data.slice(1).map(function(row) { return row[0]; });
    var datasets = [];
    for (var i = 1; i < data[0].length; i++) {
      datasets.push( // iterable chart 蠻酷的 
        {
          label: data[0][i], // column name
          data: data.slice(1).map(function(row) {return row[i]}), // data in that column
          fill: false // `true` for area charts, `false` for regular line charts
        }
      )
    }
  });
});
</script>
```

