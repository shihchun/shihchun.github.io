# Express.js 簡單整理



# Express.js

Web應用框架（Web application framework），和一般HTTP server功能上的差別就是，他們有多用HTTP網路編程，提供了可靠度高的方案，讓開發者不用進行相對底層的編程，但卻也提供可以做網路編程的函式庫。

相對底層的編程如：共通閘道介面（CGI，Common Gateway Interface）、HTTP請求解析、URL routing路由解析。

但是如果要做另外其他Server的安全機制，如SSL，可能就要另外架設Server然後把，Express框架發佈在Server的listen port上面（如：http、https庫）。

ExpressJS基於NodeJS中開發的Web框架，主要的調用方法對應HTTP方法名字，容易理解。類似的工具如：PHP、spring boot（java開發）、tomecat（java開發）、Laravel（java開發）、Django（python開發）等等。

<!---more--->

## 基本安裝與設置

打開`cmd`，瀏覽器訪問Chocolatey（是一個Windows下的軟體包管理器），將安裝的指令執行一次。

```sh
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

這時候chocolatey的bin已經加入系統環境變數裡面，所以可以直接下指令快速安裝軟體包

```sh
choco install nvm # NodeJS版本管理器
nvm install 10.15.0 #安裝10.15.0的版本
nvm on #啟用
```

## 專案創建

創建一個資料夾建立專案或是使用express-generator，自動生成一個專案，express-generator安裝進去會自動把很多server應該架設的程式碼寫入，只要進行專案邏輯編寫即可。

express-generator 設定

```sh
# npm 是NodeJS軟體包管理系統，類似python的pip
npm install express-generator -g
# 會創建 package.json
express --view=hbs /tmp/myproj_g && cd /tmp/myproj_g
npm install # 根據package.json安裝依賴庫
```

## 手動架設server

```sh
mkdir /tmp/myproj && cd /tmp/myproj && npm init
npm install express body-parser serve-static
```

- 基本設定

```js
const express = require('express');
const serveStatic = require('serve-static');
var bodyParser = require('body-parser');
const port = process.env.PORT || 3000; 
var app = express();
app.listen(port);
app.set('view engine', 'html');
app.set('views', './views/pages');
app.use(serveStatic('public'));
app.use(bodyParser.urlencoded({extended: true}));
```

# Express基本使用方法

Express 支援下列的路由方法，這些方法對應至 HTTP 方法：get、 post、put、head、delete、options、 trace、copy、lock、mkcol、move、purge、propfind、proppatch、unlock、report、mkactivity、checkout、merge、m-search、notify、subscribe、unsubscribe、patch、search，以及 connect。

1. 基本HTTP code

參考 List of HTTP status codes

| HTTP Code |          Are          |
| --------- | :-------------------: |
| 200       |          OK           |
| 204       |      No Content       |
| 301, 302  |       Redirect        |
| 304       |     Not Modified      |
| 400       |      Bad Request      |
| 403       |       Forbidden       |
| 404       |       Not Found       |
| 500       | Internal Server Error |


2. app.get()、app.post()
`get`和`post`使用方法基本上很像第一個物件放入URL變量、第二個物件是一個函式，Exress定義的函式有兩個物件，先後是請求（req）跟響應（res），可以用不同方式命名。

官方定義的這兩個Array，經過更改，會執行相應的功能在HTTP設定的app.listen()的監聽端口上面。

```js
function UDF(x){return x+1;}
// GET method route 當有人訪問 '/'，的時候
app.get('/:id', function (req, res) {
    UDF(3); //使用自定義函式
    // 傳送 HTTP CODE
    // 等同 res.status(403).send('Forbidden')
    res.sendStatus(403);
    // HTTP請求
    console.log(JSON.stringify(req.headers));
    // GET請求時候 取得 URL/asdf 的話得到asdf
    console.log(req.params.id);
    // GET請求時候 取得 URL?xxxx中的xxxx 做搜索功能可以用
    // /search?q=graphic+NVDIA+AMD => "graphic NVDIA AMD"
    console.log(req.query.xxxxx)
    res.send('GET request to the homepage');
    // 底層是res.send, 功能一樣，改變了content-type
    res.json('GET request to the homepage');
});

// POST method route
app.post('/',function (req, res){
    // POST可以使用body-parser解析返回的HTML資料
    // <input name="a">3</> => req.body.a = 3
    // <input name="a[asd]">3</> => req.body.a[asd] = 3
    console.log(JSON.stringify(req.body));
});
```

# 範本引擎（Template Engine）

NodeJS支持的範本引擎有Pug（以前叫做jade）、ejs、swig。

- PUG
```js
// npm install jade --save 安裝之後
app.set("view engine","jade")
// npm install ejs --save
app.set("view engine","jade")
// npm install swig --save
const swig = require('swig');
app.engine('html', swig.renderFile);
app.set('view engine', 'html');
```
在Get方法的cb函數下範本引擎可以使用`res.render('file',{Object});`

```js
app.get('/',function(req, res){cb;);
app.get('/',function(req, res){
    // 在Get方法的cb函數下範本引擎可以使用
    // 渲染index .pug/.ejs/.html
    res.render('index',{Object});
    res.render('index', {
            // Object 可以為
            title: 'Application 首页',
            message: req.flash('pannel'),
            count: '', //清空
        }
    });
});
// 官方提供connect-flash中間件（middleware）
// 是一個基於cookie session的插件，設定完後可以使用
req.flash('pannel', 'error:"兩次密碼不一致"');
```

不要用範本引擎，在Get方法下面設定返回的HTML：

```js
// __dirname專案資料夾的根目錄
// path.join(__dirname, 'views') = __dirname/views/index.html
app.get('/',function(req, res){
        res.sendFile(path.join(__dirname+'/views/index.html'));
    });
});
```

