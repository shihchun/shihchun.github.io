# Python 基本


JupyterNotebook 下載：
- [part I](bassic.ipynb)
- [part II](bassic2.ipynb)

## Jupyter notebook 轉換

去除output，其他自定參考[文檔](https://nbconvert.readthedocs.io/en/latest/config_options.html)

```py
jupyter nbconvert --to markdown bassic.ipynb --stdout --TemplateExporter.exclude_output=True > bassic.md
```

## Part I

`ctrl`+`]`：收起全部
`ctrl`+`[`：打開全部

基礎不討論算法


## Day1


```
## ## clear all variable in python
## import sys
## sys.modules[__name__].__dict__.clear()
```

### 篩選資料
- 一般想法
- filter 函數
- 列表解析式（list comprehension）似乎最快

##速度測試

當然一般在計算上的時候如果用的電腦比較好可能可以測到幾ms的計算速度，大概速度差個10倍左右。



```
## 一般想法 篩選掉負數
import timeit
!timeit?
data = [1,5,-3,-2,6,8,9]
res = []
for x in data:
  if x >= 0:
    res.append(x) ## 把x加入res這個list裏面（list append）
    pass
  pass
print(res)

## 執行時間測試
def test():
  res = []
  for x in data:
    if x >= 0:
      res.append(x) ## 把x加入res這個list裏面（list append）
      pass
    pass
  return res
  pass

t = timeit.timeit(test, number=10000)
print("執行時間：%f 秒" % t)

del t, res,x ,data, timeit, test
```


```
## filter 濾出奇數
## filter(fcn, iterable) == > filter(is_odd, data)
## 將data每個元素帶到is_odd中，留下返回的
!filter?
def is_odd(n):
  return n % 2 == 1 ## 返回 True or False

newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(newlist))

del is_odd
```


```
## 使用filter 篩選掉負數
from random import randint
import timeit
!randint?
data = [randint(-10, 10) for _ in range(10)] ## list comprehension
new = filter(lambda x: x >= 0 , data)
## 從data中的每個元素x來判斷，x>=0的資料，
## filter(fcn, iterable)，fcn是匿名函數
## 匿名函數除了Linux C以外大部分的新語言都有，已經是一個很普遍使用的方法

print(new,"\n",list(new)) ## python3不能直接print，python2可以，聽說節省了內存

## 執行時間測試
def test():
  return [randint(-10, 10) for _ in range(10)]
  pass

t = timeit.timeit(test, number=10000)
print("執行時間：%f 秒" % t)

del data, new, t, randint, timeit, test
```


```
## 列表解析（list comprehension） 篩選掉負數
from random import randint
import timeit
data = [randint(-10, 10) for _ in range(10)] ## xrange是python2用的
new = [x for x in data if x >= 0]
print(new)

## 執行時間測試
def test():
  return [x for x in data if x >= 0]
  pass

t = timeit.timeit(test, number=10000)
print("執行時間：%f 秒" % t)

del t, data, new, timeit, randint, test
```

### Python上的解析方式

- 列表解析（list comprehension） `[77,78,79]`
- 字典解析（dict comprehension） `{'我':12,'K.Gracia':100}`
- 集合解析（set comprehension） `{77,79,79}`
- 元組（tuple） `('a','b','c')`

  列表和字典解析使用的陳述句用的i、j、k之類的執行結束會自行del掉


```
## 字典解析
## 假設20人隨機產生分數60~100分
from random import randint
d = {x: randint(60, 100) for x in range(1,21)} ## range(20)的話會從零開始0~19

print('產生的字典\n',d,'\n解析結果：\n',d.items()) ## python2用d.iteritems()來解析出資料
  
## 篩選出大於90分，然後再寫成之前的字典形式（dict）
Largethan = {k: v for k, v in d.items() if v > 90} ## (k,v)就是dict_items下面的兩個元素

print('大於90分\n',Largethan)

del Largethan, d, randint
```


```
## 集合解析
from random import randint
data = [randint(-10, 10) for _ in range(10)] ## 建立列表（list）

s = set(data) ## 建立集合（set）
## 找集合裏面可以被3整除的元素
newS = {x for x in s if x%3 ==0 }
print('資料\n',data,'\n集合\n',s,'\n篩選可以被3整除的集合\n', newS)

del data, s , newS, randint
```

### 增加可讀性

- 原始
- 枚舉
- 元組 namedtuple數據結構

在C語言裏面是這個樣子解決這類問題的，Java的想法也類似：

```c
#define NAME 0
#define AGE 1

enum Student { /*枚舉*/
  NAME,
  AGE,
  SEX
}

name = Student[NAME]
```

Java 也是類似：

```java
enum Student { /*枚舉*/
  NAME,
  AGE,
  SEX
}
  
Student[] creatures = {Student.NAME, Student.AGE};
```


```
## 通常似乎很繁瑣的判斷寫法

student = ('Mike', 16, 'male', 'grama8722@mail.edu.tw')

## 找 name
print(student[0]) ## mike

## 找 age
if student[1] >= 18:
  ## some condition
  pass

## 找性別sex
if student[2] == 'male':
  ## some condition
  pass

del student
```


```
## 用枚舉的方式

## NAME = 0; AGE = 1; SEX = 2; EMAIL = 3;
NAME, AGE, SEX, EMAIL = range(4) ## 簡單寫法

student = ('Mike', 16, 'male', 'grama8722@mail.edu.tw')

## 找 name
print(student[NAME]) ## Mike

## 找 age
if student[AGE] >= 18:
  ## some condition
  pass

## 找性別sex
if student[SEX] == 'male':
  ## some condition
  pass

del student, NAME, AGE, SEX, EMAIL
## NAME, AGE, SEX, EMAIL 會在記憶體裡面
```


```
## 元組 namedtuple 數據結構
from collections import namedtuple ## import collections.namedtuple
Student = namedtuple('Student', ['name','age','sex','email'])
s = Student('Mike', 16, 'male', 'grama8722@mail.edu.tw')
print(s,'\nNAME: s.name\n', s.name,'\nAGE: s.age\n', s.age)
isinstance(s, tuple) ## s是否爲元組 ==> True 所以namedtuple返回確實是元組

del s, Student, namedtuple
```

## Day2

### 找到公共鍵（key）

公共鍵指在多個字典裏面存在相同的鍵（key）

在下面的字典中其中`me`和`K.Gracia`就是鍵（key）

```json
{'me':12,'K.Gracia':100}
```
- 一般寫loop找
- 使用集合（set）的方式
- 使用map reduce更快的找到公共鍵

集合下面可以使用

- python3 s.items、s.keys、s.values
- python2 s.viewitems、s.viewkeys、s.viewvalues

> 在Python寫loop的判斷運算元跟java、c、js不太一樣，ex: '||'要用'or'

| Operator (other languages) | Operator (Python) |
|----------------------------|-------------------|
| &&                         | and               |
| ||                         | or                |
| !                          | not               |

- [reduce](https://openhome.cc/Gossip/CodeData/PythonTutorial/FunctionalProgrammingPy3.html)
![](https://openhome.cc/Gossip/CodeData/PythonTutorial/images/FunctionalProgrammingPy3-1.gif)




```
from random import randint, sample
sample('abcdefg',3) ## 隨機在abcdefg中產生3個sample
sample('abcdefg',randint(3,6)) ## 隨機在abcdefg中產生3~6個sample

## 假設由abcdefg個球員名稱，每一輪的進球數是1~4
## { for x in sample('abcdefg',randint(3,6)) } 
## { x: randint(1,4) for x in sample('abcdefg',randint(3,6)) }

s1 = { x: randint(1,4) for x in sample('abcdefg',randint(3,6)) } #第一輪
s2 = { x: randint(1,4) for x in sample('abcdefg',randint(3,6)) } #第二輪
s3 = { x: randint(1,4) for x in sample('abcdefg',randint(3,6)) } #第三輪
print("\n",s1,"\n",s2,"\n",s3)



### 一般找公共鍵
res = [];
for k in s1:
  if k in s2 and k in s3:
    res.append(k)
    pass
  pass
print("Loop找公共鍵： ",res)
del k
### 使用集合（set）的方式找 直接用 & 或是 |
print('集合操作：\n',s1.keys(),'\n',s2.keys(),'\n',s3.keys())## python2用 s1.viewkeys()
print(s1.keys() & s2.keys() & s3.keys())

### 如果"很多集合"裏面找，可以使用map、reduce

mapp = map(dict.keys,[s1,s2,s3]) ## <map at 0x7f92df970278>
print("map得到： \n", list(mapp))

from functools import reduce ## functools.reduce
redd = reduce(lambda a, b: a & b, map(dict.keys,[s1,s2,s3]))
print("reduce得到\n", redd)
## 其中 lambda a, b: a & b ==> 前個結果a跟下個結果b交集

del redd, reduce, mapp, s1, s2, s3, res, randint, sample
```

### 字典排序

希望字典按照輸入順序排序。

使用`collection`.`OrdereDict`(python2)


```
## OrderDict特性 （python2需要）
## from collections import OrderedDict
## d = OrderedDict()
d = {}
d['Jim'] = (1, 35)
d['Leo'] = (5, 356)
d['Bob'] = (3, 37)
for k in d: 
  print(k) ## 會按照輸入順序
  pass

del d, k
```

### 製作歷史記錄（history log）

下面可以發現，如果執行次數多了速度就會變慢很多。


```
import time
from random import randint

players = list('ABCDEFGH') ## 8個player
start = time.time()

for i in range(1,8): ## 執行7次
  #input("：第%d次："% i)
  p = players.pop( randint( 0,7-i ) ) ## 從列表刪除pop(i)第i個元素，p爲取出的元素
  end = time.time()
  print(i, '刪除： ',p , '取出元素執行時間：', (end-start)*1000,"ms")
  print('列表變爲：', players)
  pass

del players, p, end, start, randint, time
```

在python 裏面有一個`collection.deque`的庫可以使用。

例如`deque([],5)`則可以記錄5個數列更改之前的五個元素。

將其實體化`d = deque([],5)`，直接使用再append數列的時候同時也對其append即可。


```
from collections import deque
d = deque([],5)
a = [1,2,3,4,5]
d.extend(a) ## append list中的所有元素時，使用extend
print(d)
d.append(9) ## 對[1,2,3,4,5]再append一個 '1'
print(d) ## 可以發現只剩下五個元素，第一個append的1不會顯示，剩下五個歷史記錄
#要使用直接使用 list(d) 可以直接使用數列
print(list(d))

del d, deque, a
```

若需要在下面加入歷史記錄的話


```
from random import randint
N = randint(0,5)
print("答案: ",N)

def guess(k):
  if k == N:
    print("猜對")
    return True
  if k < N:
    print("N比%s還要大" % k)
  else:
    print("N比%s還要小" % k)
  return False

while True:
  line = input("請輸入一個數字： ")
  if line.isdigit():
    k = int(line)
    if guess(k): ## 執行guess function，猜對跳出
      break
      pass
    pass
  pass

del k, line, N, randint, guess
```


```
## 加入deque歷史記錄

from random import randint
from collections import deque
'''
使用pikle的話可以將寫好的資料dump成檔案並儲存
要用的時候可一在別的檔案透過路徑的方式讀取。
類似寫程式的時候把資料存到txt裏面再讀取出來，不過那要writeline
一行一行寫與讀取，這個不用
'''
import pickle
## qq = pickle.load(open('history')) ## 讀取儲存結果
## qq = pickle.dump(q, open('history','w')) ## 儲存結果

N = randint(0,20)
history = deque([],5)
print("答案: ",N)

def guess(k):
  if k == N:
    print("猜對")
    return True
  if k < N:
    print("N比%s還要大" % k)
  else:
    print("N比%s還要小" % k)
  return False

while True:
  line = input("請輸入一個數字： ")
  if line.isdigit():
    k = int(line)
    history.append(k) ## 每次輸入一個數字就加入history裏面
    if guess(k): ## 執行guess function，猜對跳出
      break
  elif line == 'history' or line == 'h?':
    print( list(history) )
    pass
  pass

del history, line, k, N, pickle, deque, randint, guess
```

## Day 3



### 疊代

iter(x)可以檢查一個東西是否可疊代，iter()可以找到疊代器。




```
L = [1,2,3,4]
s = 'abcdefghijk'
print( '疊代器存在：\n L: ', iter(L),'\n s: ', iter(s) ) ## 都可以list跟char都可疊代
print( '疊代可實體化：\n L: ', L.__iter__(),'\n s: ', s.__iter__() ) 

### next()協議在python3變成__next__()
it = iter(L)
## print( it.__next__() ) ## 第0個元素
## print( it.__next__() ) ## 第1個元素
## print( it.__next__() ) ## 第2個元素
## print( it.__next__() ) ## 第3個元素
## print( it.__next__() ) ## 返回StopIteration 然後條錯誤

for _ in range(len(L)):
  print(it.__next__())
  pass

del it, L, s
```

### curl或是request接收

[apis](https://rapidapi.com/collection/top-weather-apis)

可以參考其他的api拿到對他們的網址伺服器發出get請求，可以返回資料，然後使用python將其轉換成json的格式，可以對這些資料做類似字典的操作。

這類操作常常要看文檔以及他們的一些檔案格式來做調整。

對HTML內容進行GET請求並且將資料拿下來成JSON之類的可分析格式就是爬蟲了。


```
## curl "http://wthrcdn.etouch.cn/weather_mini?city=" ### shell命令
import requests
def getWeather(city): 
  r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
  data = r.json()['data']['yesterday']
  #print("資料：",r.json())
  #print("昨天資料：",r.json()['data']['yesterday'])
  return '%s: %s, %s' % (city, data['low'], data['high'])

print(getWeather(u'北京'))
print(getWeather(u'上海'))

del requests
## function只會返回return的東西喔， 所以r、data都被清掉了
```


```
## 舉個例子，一般是用api的時候會長這樣
import requests

url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

querystring = {"lang":"en","lon":"<required>","lat":"<required>"}

headers = {
    'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    } ### 一般的api都需要有api key，通常是需要一些付費或是需要註冊帳號的
### 自己在自己的電腦寫網頁php、django、tornado、expressJS之類的編寫，也可以透過這個方法得到返回值

response = requests.request("GET", url, headers=headers, params=querystring)

print(response)

del response, headers, querystring, url, requests
```

### 封裝（使用疊代器）

可疊代->批次

首先瞭解什麼是[疊代器](https://www.kawabangga.com/posts/2772)，在Python中所有的loop疊代，例如for之類的都是透過所謂的next協議去做出來的，包括現在常常被使用的ES6 javascript也是，所以我們可以透過使用疊代器，減少記憶體的使用，因爲Python是一個執行效率不太高的語言。

[Python vs C](https://benchmarksgame-team.pages.debian.net/benchmarksgame/fastest/python3-gcc.html)，看完大概就知道使用這個的原因，而且很多框架（framework）也是直接調用next疊代協議（iterator protocol），所以瞭解一點對寫Python會有很多的幫助。


```
### 將之前使用的API做封裝成 可疊代物件
import requests
from collections import Iterable, Iterator

class WeatherIterator(Iterator): ##疊代器
  def __init__(self, cities): ### 設定index和cities
    self.cities = cities
    self.index = 0
    pass
  
  def getWeather(self, city): ### 拿資料
    r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
    data = r.json()['data']['yesterday']
    return '%s: %s, %s' % (city, data['low'], data['high'])
  
  def __next__(self): ### next()在python3變成__next__()
    if self.index == len(self.cities):
      raise StopIteration ### 錯誤處理 riase（引發）StopIteration錯誤（pyton內建）
      pass
    city = self.cities[self.index]
    self.index += 1
    return self.getWeather(city)
  
class WeatherIterable(Iterable): ### 可以疊代物件
  def __init__(self,cities):
    self.cities = cities
    pass
  
  def __iter__(self):
    return WeatherIterator(self.cities)
  
### 封裝完畢，實體化來使用，可以對它疊代、批次處理
for x in WeatherIterable([u'北京',u'上海']):
  print(x)
  pass

del x, Iterable, Iterator, requests
```

### 錯誤處理

- 基本
- 錯誤判斷處理
- 自己定義錯誤類型


```
## Ex1: 基本
try:
   raise TypeError
except TypeError:
  print('TypeError')
```


```
## Ex2: 錯誤判斷處理
def mye( level ):
  if level < 1:
    raise Traceback('Hi~Hi') 
    ## 這裏拋出 Traceback不是內建的，會顯示'is not defined'
    ## 就沒有，印出我們想要定義的錯誤類型
    
    print("這裏不執行")
    ### 下面是其中一些python有的錯誤類型，下面的程式不執行
    raise TypeError('Hi')
    raise ValueError("Hi") 
    raise NameError('Hi')
    raise ZeroDivisionError('Hi')
    pass
  
  pass

#mye(0) ## 會raise拋出錯誤，error會顯示我們定義的錯誤

try: ## 在c java是try catch、foreach多載之類，用法差不多
  mye( 0 )
except Exception as err: ## print出所有錯誤
  print("44321","Erro {}".format(err))
  pass

del mye
```


```
## Ex3： 自己定義錯誤類型
class Networkerror(RuntimeError):
  def __init__(self, arg):
    self.name = "Networkerror"
    self.args = arg
    pass
  pass
pass

        
try:
  raise Networkerror("Bad hostname")
except Networkerror as err:
  print("Err ",err.name, '\n',err. args)  ## 作用一樣 "Erro {}".format(err))
  pass

del Networkerror
```

## Day 4

### yield 產生器（Generator）來做疊代器

- yield 產生器使用方法
- yield 產生器做成可以疊代的物件


```
### 介紹 Python yield Generator 疊代方法

def f(): ## Generator Fcn 這個可以疊代
  print('執行 yield 1')
  yield 1
  print('執行 yield 2')
  yield 2
  print('執行 yield 3')
  yield 3
  pass
g = f()

## print( g.__next__() )
## print( g.__next__() )
## print( g.__next__() )
## print( g.__next__() ) ## StopIteration會錯誤，跟之前一樣可以用產生器（Generator）器去做

## ## 第一種
## for _ in range(3):
##   print( g.__next__() )
##   pass

## 可以寫成
for x in g:
  print(x)
  pass

print( g.__iter__() is g ) ## True =>由於g可以作爲g.__iter__()來調用

del x, g, f

```


```
class PrimeNumbers:
  def __init__(self, start, end): ## 建構子
    self.start = start
    self.end = end
    pass
  
  def isPrimeNum(self, k):
    for i in range(2, k):
      if k%i == 0: ## k mod i == 0
        return False
      return True
    pass
  
  def __iter__(self): ## 疊代器
    for k in range(self.start, self.end + 1):
      if self.isPrimeNum(k):
        yield k
        pass ## pass if pass可以不寫
      pass ## pass for
    pass ## pass fcn
  pass ## pass class

## 測試封裝完的class
y = []
for x in PrimeNumbers(1,100):
  y.append(x)
  pass
print(y)

del y, x, PrimeNumbers
```

### 反向疊代


```
## 反向疊代

L = [1,2,3,4,5]

print( 'L[::-1]: ', L[::-1] ) ## 會得到新列表到記憶體

## reversed() 只有多一個疊代器，不會多一個列表，較好
print( reversed(L) )
y = []
for _ in reversed(L):
  y.append(_)
  pass
print(y)

del y, _, L
```


```
### 寫成物件範例

class FloatRange:
  def __init__(self, start, end, step=0.1): ### 建構子
    self.start = start; self.end = end; self.step = step;
    pass
  
  def __iter__(self):
    t = self.start
    while t <= self.end:
      yield t
      t += self.step
      pass
    pass
  
  def __reversed__(self):
    t = self.end
    while t >= self.start:
      yield t
      t -= self.step
      pass
    pass
  pass

## 測試封裝完的class

## 正序
y = []
for x in FloatRange(1.0, 4.0, 0.5):
  y.append(x)
  pass
print(y)

## 反序
y = []
for x in reversed( FloatRange(1.0, 4.0, 0.5) ):
  y.append(x)
  pass

print(y)

del y, x, FloatRange
```

### 文件讀取

- ope().readlines() 把每個row存到列表中



```
## 產生可以讀寫的檔案
! dmesg > dmessg.log
! find / -name 'dmessg.log'
#! cat /content/dmessg.log

f = open('/content/dmessg.log')

## readline 讀取太大的文件會浪費太多記憶體
lines = f.readlines()
print('f after readlines()會被清空成 list(f)=', list(f))
print(lines[1:10]) ### 用列表的方法可以直接找第1到第10行的數據

## 在python中可以使用islice 做切片
## islice(iterable, [start], [stop]) ## 到最後一行stop寫None
from itertools import islice #itertools.islice
f = open('/content/dmessg.log') ## reandlines()完f = []
y = []
for _ in islice(f,1,10): ## 取出第一行到第十行f的1～10元素就會被拿走了
  y.append(_)
  pass
print(y)

del y, f
```

### 並行

使用一個for疊代多個iterable物件

- zip 把列表***並***起來
- itertools.chain 把列表***串***起來


```
!zip?
## zip 把列表並起來
x = zip([1,2,3,4],('a','b','c','d')) ## 合併兩個列表
y = zip([1,2,3,4],('a','b','c','d'),[7,8,9,10]) ## 合併三個列表
i = zip([1,2,3,4],('a','b','c')) ## 列表len()不一樣合併
print('按照順序抓元素合併包起來\n'
    ,'\n合併2個列表: ',list(x) ,'\n合併3個列表: ', list(y),
      '\n列表len()不一樣合併, 取最大公因數: ',list(i) )
del x, y, i
```


```
## zip 範例
from random import randint

## generating data
math = [randint(60, 100) for _ in range(40)] ## random the score
  science = [randint(60, 100) for _ in range(40)]
english = [randint(60, 100) for _ in range(40)]

## 處理加總
for i in range(len(math)):
  math[i] + science[i] + english[i]
  pass

## 使用zip處理
total=[] #加總
for i,j,k in zip(math, science, english):
  total.append(i+j+k)
  pass

del math, science, english, i, j, k
```


```
## itertools.chain 把列表串起來
from itertools import chain
!chain?
y = chain([1,2,3,4], ['a','b','c','d'])
print(list(y))

y = []
for _ in chain([1,2,3,4], ['a','b','c','d']):
  y.append(_)
  pass
print(y)

del _, y, chain
```


```
## 範例
from itertools import chain
e1 = [randint(60, 100) for _ in range(40)]
e2 = [randint(60, 100) for _ in range(40)]
e3 = [randint(60, 100) for _ in range(44)]
e4 = [randint(60, 100) for _ in range(39)]

## 找超過90分的數量
count = 0
for s in chain(e1,e2,e3,e4):
  if s > 90:
    count += 1
    pass
  pass
    print('超過90分的數量: ', count)

del count, s, e1, e2, e3, e4
```

## Day 5

### 字串拆分

- 單一字串 `split()`
- 多個字串 `re.split('正則表達式', str)`


```
## 處理單一分隔符號

## 產生可以讀寫的檔案
#! ps aux > psAux.log
#! find / -name 'psAux.log'
#! cat /content/psAux.log.log
## Linux中的CPU進程PID，系統目錄下面PROC執行中的程序會在上面
!ps aux
x = !ps aux 
s = x[-1] #取出x的最後一行

print('\n最後一行:\n', s)
print( '\n以空格方式去分隔:\n', s.split() )

del s, x
```

### map

[Python3 map() bug](https://stackoverflow.com/questions/18433488/non-lazy-evaluation-version-of-map-in-python3)

在Function 裡面
```
map(lambda x: k.extend(x.split(_)), res) 
```

要寫成

```
list( map(lambda x: k.extend(x.split(_)), res) )
```


```
## map(fcn, iterable)，用法跟filter很像
## map: convert each item of an array, 
## filter: select certain items of an array.
## filter 的fcn要返回True或是False判斷是否留下列表元素
## map 則是對列表每個元素操作，返回
!map?

## 對每個列表元素做平方
def square(x) :
  return x ** 2

k = map(square, [1,2,3,4,5])
print(list(k))

del k
```


```
a = ';/\,|abcdefghijklmnopqrstuvwxyzABCD'
print('使用亂數 a：', a)

## 產生了亂數a，使用 ;/\,| 分隔
## 直接使用split的問題
s = ';/\,|'
k = a.split(';'); 

print( "\n第一次拆完之後為二維列表無法直接再直接拆分 a.split(';'):\n", k)
## k = k.split('/'); 不能繼續用同樣方法拆

## map 再切一次 第二次拆分map完的結果list變得更難處理
k = map(lambda x: x.split('/'), k) ## k中的每個元素x拿出來回傳x.split(',')

print('\n第二次拆分map完的結果list變得更難處理\n',
      "map(lambda x: x.split('/'), k):\n",list(k))

## 第二次拆分map完的結果extend到新的list中
k = []
k = a.split(';'); 
map( lambda x: k.extend( x.split('/') ), k)

print('\n第二次拆分map完的結果extend到新的list中就解決了\n',
      "map( lambda x: k.extend( x.split('/') ), k):\n",k)
k = [x for x in k if x]
print('濾除空字串\n[x for x in k if x]\n',k)

del k, s, a
```

### split()拆分 vs re.split()正則表達式

正則表達式（regulation expression）




```
## 亂數產生器
from random import randint
def makeSalt(lens):
  strs = ';/\,|abcdefghijklmnopqrstuvwxyzABCD'
  salt = ''
  for i in range(lens):
    salt += strs[randint(0,31)]
    pass
  return salt
  pass

def mySplit(strs, salt):
  res = [strs]
  k = []
  for _ in salt:
    k = []
    ## python3 function裡面map()外要加上一個list()，不然不會動作
    list( map(lambda x: k.extend(x.split(_)), res) )
    res = k
    pass
  return [x for x in res if x] ##去除空字串

sInput = makeSalt(35)
sSalt = ';/\,|'
print( sInput,'\n', mySplit(sInput, sSalt) )

del sInput, sSalt, makeSalt
```


```
## 亂數產生器
from random import randint
def makeSalt(lens):
  strs = ';/\,|abcdefghijklmnopqrstuvwxyzABCD'
  salt = ''
  for i in range(lens):
    salt += strs[randint(0,31)]
    pass
  return salt
  pass

import re ## 正則表達式
!re.split?
sInput = makeSalt(35)
sSalt = ';/\,|'
print( sInput,"\n\n直接用 re.split(r'[;\,/|]+', sInput):\n",re.split(r'[;\,/|]+', sInput))

del sInput, sSalt, makeSalt, randint
```

### 判斷字串開頭結尾字符

bassic2.ipynb 從這裡開始繼續下個檔案會重新說過

`char.startswith()`、`char.endswith()`，只能傳入字串或是元組


```
#!ls -lh sample_data
import os
k = os.listdir('sample_data')

## char.startswith()、char.endswith()
s = 'california_housing_test.csv'

print("s =", s)
print("s.endswith('.csv') =>", s.endswith('.csv') )
print("s.endswith('.py') =>",s.endswith('.py'),'\n' )

## 所以可以寫成
s =[name for name in k if name.endswith( ('.md', '.json'))]
## 輸出name（最前面的），for name in k，if判斷k的第name個元素endswith（（'', '',''））
print('os.listdir(): \n',k)
print("濾出 *.md  *.json :\n",s)


del k, s, os
```


```
## 把 *.txt 檔案全部改成 *.m 的格式
import os
path = './'
f = os.listdir(path)
out = [x for x in f if x.endswith('.txt')]

n = 0; i = 0
for i in out:
    ## 設定舊檔名（就是路徑+檔名）
    oldname = out[n]
    k = len(out[n])-4
    ## 設定新檔名
    newname = out[n][0:k] + '.m'
    ## 用os模組中的rename方法對檔案改名
    os.rename(path+oldname, path+newname)
    print(oldname, '======>', newname)
    n += 1
    pass

```


```
#!ls -lh sample_data
import os, stat ## stat是掩碼庫
k = os.stat('sample_data/README.md')
print('資料：\n',k)
k = os.stat('sample_data/README.md').st_mode ## oct 八進制
print('掩碼：\n',k)
k = oct(k)
print('權限知道權限755: \n',k)

## 修改Linux權限
## stat.S_IXUSR 掩碼AND權限 => 權限755, 最上面的group會加上可執行權限(x,rwx)

## os.chmod('sample_data/README.md', os.stat('sample_data/README.md').st_mode | stat.S_IXUSR)

del k, os, stat
```


## Part II

## 判斷字串

可傳入元組
- str.startwith() 
- str.endwith()


```python
# generate testing dir file
!if [ -d "test" ]; then rm -rf test;  fi
! mkdir test && cd test && touch a.sh b.py c.h d.java e.py f.cpp  && ls -lh
```


```python
import os, stat
os.listdir('./test')

s = 'g.sh'
print( "s = 'g.sh', s.endswith: ",s.endswith('.sh') )

# 篩選
print("\n列表comprehension, \n [ name for name in os.listdir('./test') if name.endswith(('.sh', '.py')) ])")
[ name for name in os.listdir('./test') if name.endswith(('.sh', '.py'))]

del s, os, stat
```

## 修改權限

修改成其他權限可參考
- os.stat('filepath')
- os.stat('filepath').st_mode
- os.chmod('file', os.stat('file').st_mode | stat.S_IXUSR )

os.chmod(檔案路徑, 檔案的stat與掩碼做OR的結果)

[python stat doc](https://docs.python.org/2/library/stat.html)



```python
import os, stat
os.listdir('./test')

# 修改執行權限 755 644 使用遮罩掩碼做OR去改
os.stat('./test/e.py')
os.stat('./test/e.py').st_mode
print("\nos.stat:\n%s\nos.stat.st_mode: %s => 這個是二進制數值\n轉換成八進制oct(): %s =>看得出來是644的權限（user gourp other三位元權限u+g+o）\n" 
      % ( os.stat('./test/e.py'),os.stat('./test/e.py').st_mode , oct(os.stat('./test/e.py').st_mode)), 
      "每個用戶組分別有read-write-execute 可執行、可讀、可寫三種權限，基本Linux"
       )

!ls -lh ./test | grep "e.py"
os.chmod('./test/e.py', os.stat('./test/e.py').st_mode | stat.S_IXUSR )
!ls -lh ./test | grep "e.py"

del os, stat
```

## 替換文檔格式，格式處理

使用正則表達式，進行處理

替換

- re.sub()


```python
# !find / -name dpkg.log # /var/log/dpkg.log
# !cat /var/log/dpkg.log | less #more
print('看前十個資料，要改變日期格式')
!if [ -d "test" ]; then rm -rf test; mkdir test; fi
!cat /var/log/dpkg.log >> ./test/dpkg.log
# !head 10 ./test/dpkg.log
print('\n用python')
# log = open('/var/log/dpkg.log').read() # readall
log = open('/var/log/dpkg.log') #.readline() 執行一次迭代器+1 讀出一行
y = ''
for i in range(10):
  #x = log.readline().rstrip("\n") # print 會自動加入 \n
  x = log.readline()
  y = x + y
  pass
print(y)

import re # 正則表達式
#!re.sub?
# 描述日期格式 \d{4} \d{2} \d{2} 用()把三組圈起來
a = re.sub('(\d{4})-(\d{2})-(\d{2})', '\1' , y)
# '\1\2' 表示第一組跟第二組
b = re.sub('(\d{4})-(\d{2})-(\d{2})', '\1-\2' , y)
# r'\1\2' 原始字串
c = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\1-\2' , y)
print( "\na: \1': \n%s \nb: '\1\2': \n%s \nc: 使用原始字串的話長度不會因爲正規改變(可能會像是a、b一樣有格式問題)r'\1\2': \n%s "
 % (a,b,c)
  )
# 知道上面就可以知道 ==> r'\2 / \3 / \1' 三組之間用/隔開
d = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1' , y)
print("\nd:  r'\2/\3/\1': \n%s " % d)

# 可以對每個組定義名稱一樣的結果可以寫成下面 每個組( ?P<name>\d{} ), 然後建構就用\g<name>
e = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>' , y)
print("\nd: 每個組( ?P<name>\d{} ), 然後建構就用\g<name>: \n%s " % e)
del a,b,c,d,e,re,x,y

```

## 字串拼接

- '+'
- ‘分隔符號’.join(list) ：list可以是comprehension



```python
s1 = 'abcdefg'
s2 = '12345'
# 拼起來
print ("s = s1 + s2 '+' ： %s" %s1+s2 )
print("str.__add__(s1,s2) :%s" %str.__add__(s1,s2) )
print("s1 > s2: %s" % (s1>s2) )
print("str.__gt__(s1,s2): %s" %(str.__gt__(s1,s2)) )

pl = ["<0112>", "<32>", "<1024x768>", "<60>", "<1>", "<100.0>", "<500.0>"]
s = ''
for _ in pl: ## 列表很長會有記憶體浪費
  s+=_
  pass

''.join(pl) ## 這會比較好 (以空字串分隔)

print("''.join(pl): %s \n ';'.join(pl): %s " %(''.join(pl), ';'.join(pl)))

# 使用列表
''.join([str(x) for x in pl]) # 列表[]會創建列表到記憶體
''.join(str(x) for x in pl) # 產生器這個比較好

del s1,s2,pl     
```

## 對齊字串

- str.ljust(), str.rjust(), str.center() 左右中對齊
- format(,<>^) print 字典的時候也可以用


```python
s = 'abc'
a = s.ljust(20,'=')
b = s.rjust(20,'=')
c = s.center(20,'=')
print("\nljust(): \n%s\nrjust(): \n%s\ncenter(): \n%s" %(a,b,c))

a = format(s, '<20')
b = format(s, '>20')
c = format(s, '^20')
print("\nformat(s, '<20'): \n%s\nformat(s, '>20'): \n%s\nformat(s, '^20'): \n%s" %(a,b,c))
d = {
    "lodDict":100.0,
     "SmallCull": 0.04,
     "DistCull": 500.0,
     "trilinear": 40,
     "farclip": 477
}
d.keys()
map(len, d.keys())
max(map(len,d.keys()))
w = max(map(len,d.keys()))
print("\n對齊字典\n")
for k in d: #到冒號之前對齊，用最長的長度w去對齊
  print( k.ljust(w),':',d[k])
  pass
del a,b,c,d,w,s
```

## 字串去除
- strip()、lstrip()、rstrip()
- '+'、[:end]
- replace()
- replace()、re.sub
- translate()


```python
#  strip() lstrip() rstrip()
s = '    ======abc ++ 123   --   '
a = s.strip()
b = s.lstrip()
c = s.rstrip()
print( " s: %s" %s, "\n s.strip() 除掉兩邊空白: %s \n s.strip() 除掉左邊空白: %s \n s.strip() 除掉右邊邊空白: %s" %(a,b,c))

d = s.strip().strip('-=')
print(" s.strip().strip('-=') 去除前後空白再去處前後-=: %s" %d)

del a,b,c,d,s
```


```python
s = 'abc:123'
a = s[:3] + s[4:]
print("s: %s \n s[:3] + s[4:]: %s" %(s,a)); del s,a
```


```python
# replace() re.sub() '\' print 不太出來
s = "\tabc\t123\txyz\ropq\r"
a = s.replace('\t', '')
import re
b = re.sub('[\t\r]', '', s)
print("s: %s \n s.replace('\t', ''): %s \n re.sub('[\t\r]', '', s): %s" 
      %(s,a,b)); del s,a,b
```


```python
# str.translate() unicode.translate()
s = 'abc1230323xyz'
# 假設有一個加密是將上面abc->xyz，xyz->abc
import string
a = s.maketrans('abcxyz', 'xyzabc') # 產生mapping 映射表
b = s.translate(a)
print(' s:',s,'\n mapping:',a,'\n 轉換結果：',b)
```

