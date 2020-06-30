###------------------------ /test.csv ------------------------###
# with matplotlib
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./test.csv')
fig = df.plot(x='t',y= 'v')
plt.show()

##--------------------------------------------------------------##

# with plotly
import pandas as pd
import plotly.graph_objects as go
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./test.csv')
# df.plot(x=df.t,y=df.v)
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['t'], y= df['v'],
                    mode='lines', name='sine'))
fig.update_layout(
    title="test Datasets", 
    template="none",
    xaxis_type="linear", 
    yaxis_type="linear"
)
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "s")
fig.show()
# mode [maker | lines ]
# theme template: ["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]
# exponentformat "none" | "e" | "E" | "power" | "SI" | "B" 

##--------------------------------------------------------------##

# with plotly + pandas
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./test.csv')
fig = df.plot(x=df['t'],y=df['v'],title="test Datasets", 
template="none",labels=dict(index="time", value="voltage"),
log_x=False, log_y=False )
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "s")
# fig.show()
fig.write_html("file.html")

###------------------------ /test.csv ------------------------###
###-------- /ns3_ofdm_yans_wifi_model.csv multiple trace --------###

# with matplotlib + pandas
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
df.plot(x=df.columns[0], y=df.columns[1:])
plt.show()

#---------------------------------------------------------------#

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
fig.add_annotation(x=1.1, y=1, text="success transmit")
fig.show()
# fig.write_html("file.html")

#---------------------------------------------------------------#

# with plotly + pandas + subplot + csv
import pandas as pd
import plotly.graph_objects as go # to ajust layout
from plotly.subplots import make_subplots
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0],y=df.columns[1:], title="ns3 ofdm yans wifi model",
template="none", labels=dict( index="", value="success", variable=""),log_x=False, log_y=False, kind='line',
)
fig.update_layout(xaxis_title='SNR(dB)', yaxis_title='Frame Success' ) # showlegend=True
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB")
fig.show()
fig.write_html("file.html")

#---------------------------------------------------------------#

# with plotly + pandas + subplot col trace
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0],y=df.columns[1:], title="ns3 ofdm yans wifi model",
template="none", labels=dict( index="", value="success", variable=""),log_x=False, log_y=False, kind='line',
facet_col="variable",facet_col_wrap=2 # express way facet_raw="variable", wrap col only
)
fig.update_layout(xaxis_title='SNR(dB)', yaxis_title='Frame Success' ) # showlegend=True
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB")
fig.show()
# fig.write_html("file.html")

#---------------------------------------------------------------#

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

fig.update_layout(xaxis_title='SNR(dB)', yaxis_title='Frame Success', template="none")
fig.update_yaxes(exponentformat="power", rangemode="tozero")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB", range=[-3, 10])
fig.show()
# fig.write_html("file.html")

#---------------------------------------------------------------#

# 土法煉鋼
# with plotly
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate6Mbps'],
                    mode='lines'), name='OfdmRate6Mbps')
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate9Mbps'],
                    mode='lines', name='OfdmRate12Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate12Mbps'],
                    mode='lines', name='OfdmRate18Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate18Mbps'],
                    mode='lines', name='OfdmRate18Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate24Mbps'],
                    mode='lines', name='OfdmRate24Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate36Mbps'],
                    mode='lines', name='OfdmRate36Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate48Mbps'],
                    mode='lines', name='OfdmRate48Mbps'))
fig.add_trace(go.Scatter(x=df['snr(xlabel)'], y= df['OfdmRate54Mbps'],
                    mode='lines', name='OfdmRate54Mbps'))
fig.update_layout(
    title="ns3 ofdm yans wifi model", 
    template="none",
    xaxis_type="linear", 
    yaxis_type="linear"
)
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "s")
# fig.show()
fig.write_html("file.html")

###-------- /ns3_ofdm_yans_wifi_model.csv multiple trace --------###
###------------------------ plotly.offline -----------------------###

# with matplot + plotly.offline
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from plotly.offline import plot_mpl, init_notebook_mode, enable_mpl_offline
import plotly.offline

from plotly.offline.offline import plot_mpl

# init_notebook_mode()
enable_mpl_offline()
plotly.offline.init_notebook_mode(connected=True)
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
plot_mpl(fig, filename='temp-plot.html')
# plt.show()

###--------------------- plotly.offline ---------------------###

# with plotly + pandas + subplot express
# 可以分類 Plot
import pandas as pd
import plotly.express as px
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = px.scatter(df, x=df.columns[0], y=df.columns[1], facet_col="species")
fig.update_xaxes(ticks="inside")
fig.update_yaxes(ticks="inside", col=1)
fig.show()
# >>> df
#      sepal_length  sepal_width  ...    species  species_id
# 3             4.6          3.1  ...     setosa           1
# ..            ...          ...  ...        ...         ...
# 145           6.7          3.0  ...  virginica           3
# >>> df.groupby('species').size()
# species
# setosa        50
# versicolor    50
# virginica     50
# dtype: int64


import matplotlib.pyplot as plt
import plotly.offline

fig, ax = plt.subplots()

ax.plot([0, 1, 2], [0, 1, 2], 'o-', label='a')
ax.plot([0, 1, 2], [0.5, 1.5, 2.5], 'o-', label='b')

ax.legend()

plotly.offline.plot_mpl(fig, filename='temp-plot.html')

# with plotly + pandas + subplot + csv
import pandas as pd
import plotly.graph_objects as go # to ajust layout
from plotly.subplots import make_subplots
pd.options.plotting.backend = "plotly"
df = pd.read_csv('./ns3_ofdm_yans_wifi_model.csv')
fig = df.plot(x=df.columns[0],y=df.columns[1:], title="ns3 ofdm yans wifi model",
template="none", labels=dict( index="", value="success", variable=""),log_x=False, log_y=False, kind='line',
)
fig.update_layout(xaxis_title='SNR(dB)', yaxis_title='Frame Success' ) # showlegend=True
fig.update_yaxes(exponentformat="power")
fig.update_xaxes(tickprefix=">", ticksuffix = "dB")
# fig.show()
# fig.write_html("file.html")

# >>> fig.get_subplot(1,1), fig.to_dict(), 
# fig.to_ordered_dict(), fig.to_json(), fig.to_plotly_json()
# console 按tab看到這個拿來用用看
# pickle.dump; pickle.dump(obj, open("s.txt","wb"))
# f = open("s.txt","wb"); pickle.dump(dict,f); f.close()
# 'wb 'write byte format 應該沒問題
# with open("data.txt", "w") as f: # with write
#     	f.write(json.dumps(data, ensure_ascii=False))
# 看了看可能是因為是collection 產生的dict類型不一樣
# <class 'dict'>, <class 'collections.OrderedDict'>
# plotly.subplots.SubplotXY 的 source 中看到用
# collections.namedtuple


from plotly.subplots import make_subplots
fig2 = make_subplots(rows=1, cols=2)
for i in range(1, 5):
    fig2.add_trace(
        go.Scatter(x=df[df.columns[0]], y=df[df.columns[i]]),
        row=1, col=2
    )
    pass


