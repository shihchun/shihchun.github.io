# Plotly csv 讀取



## 加入自定義 ShortCodes

[Hugo的文檔](https://gohugo.io/templates/shortcode-templates/)有提到我們可以自己製作`shortcodes`，這篇文章紀錄我把`char.js`放到我自己hugo的過程。


1. `/layouts/shortcodes/<SHORTCODE>.html`
2. `/themes/<THEME>/layouts/shortcodes/<SHORTCODE>.html`

hugo中加入一個檔案`layouts/shortcodes/rawhtml.html`

```html
<!-- raw html -->
{{.Inner}}
```

## 用法

最後只要在文章中加入，其實就是加入html的程式碼而已，之後可以再修改。

```md
{< rawhtml >}
html code， 由於{{ }}， 會錯誤，所以只用一個{}表示
{< /rawhtml >}
```

## python產生plotly的html

python安裝要用到的庫

```console
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
{{.Inner}}    
</div>
```

加入shortcode，hugo中加入一個檔案，檔案放在`layouts/shortcodes/plotly.html`

```html
<!-- plotly html -->
<style>.embed-container { position: relative; padding-bottom: 56.25%;      
    height: 100%; overflow: hidden; max-width: 100%; } .embed-container iframe, 
    .embed-container object, .embed-container embed { position: absolute;   
    top: 0; left: 0; width: 100%; height: 100%; }</style>
    <div class='embed-container'>
        <iframe frameborder='0' scrolling='no' src="{{ .Site.BaseURL }}{{ .Page.RelPermalink }}{{ .Get 0 }}.html"></iframe>
    </div>
    
```

以後直接使用，一樣怕`{{ }}`被識別，紀錄就少寫一個`{}`，檔案放在`static/plotly/`

```md
{< plotly ns3_ofdm_yans_wifi_model>}
```

`{{ .Site.BaseURL }}{{ .Page.RelPermalink }}`爲網址內容，`{{ .Get 0 }}`爲`ns3_ofdm_yans_wifi_model`


## 多個trace用pandas更快

這個辦法很快，但是如果要plot子圖的話就還是要用上面的。

{{< plotly ns3_ofdm_yans_wifi_model >}}

```py
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

用matplotlib的不用設定backend，當然除了plotly這個backend，pandas還支援其他的backend。


## multiple plot facet_col

{{< plotly ns3_ofdm_yans_wifi_model_col_trace >}}

```py
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

```py
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


## Matplotlib with plotly display

{{< plotly matplotlib_pandas_subplot >}}

```py
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
from plotly.tools import mpl_to_plotly
plotly_fig = mpl_to_plotly(fig)
plotly_fig.update_layout(template="none")
plotly_fig.write_html("temp-plot.html")
```

### Matplotlib pandas subplot

用pandas的時候，要返回`plt.figure()`的物件的方法是用`df.get_figure()`，返回之後就可以plot了。

用`plt_mpl`做的html相對於plotly直接做的有點缺點，大小控制的沒這麼好，我都刪除一個div了還是有一點大小問題。

{{< plotly matplotlib_pandasns3_ofdm_yans_wifi_model >}}

```py
# with matplotlib + pandas
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0], y=df.columns[1:])
#plt.show()
from plotly.offline.offline import plot_mpl
plot_mpl(fig.get_figure(), filename='temp-plot.html', auto_open=False)
# more setting with plotly
fig = fig.get_figure()
from plotly.tools import mpl_to_plotly
plotly_fig = mpl_to_plotly(fig)
plotly_fig.update_layout(template="none",showlegend=True,annotations=[dict(visible=False)])
plotly_fig.write_html("temp-plot.html")
```

不過也有例外，比如下面這樣寫，df.get_figure()我就沒找到，因該是`subplot=True`，加上的關係。

```py
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

## Plotly.js

直接寫的話比較不好寫，需要的cdn

```html
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
```





