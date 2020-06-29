# node.js body-parser + swig 處理HTML表單


## 安裝curl

```sh
# 打開cmd用Chocolatey（Windows下的軟體包管理器）
choco install curl # 安裝curl
```

## 用curl測試post

```js
router.get('/test', function (req, res, next) {
  // curl http://localhost:4000/test  --request GET
  user = {
    "username": "abc",
    "password": "abc"
  };
  res.json(user);
  res.end();
});

router.post('/test', function (req, res, next) {
  console.log(req.headers);
  console.log(req.body);
  res.end();
});
```

測試curl

```sh
curl http://localhost:4000/test
{"username":"abc","password":"abc"}
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"abc","password":"abc"}' \
    http://localhost:4000/test
```

Console

```sh
## after post
{ host: 'localhost:4000',
  'user-agent': 'curl/7.61.1',
  accept: '*/*',
  'content-type': 'application/json',
  'content-length': '35' }
{ username: 'abc', password: 'abc' }
```

## 建立路由測試

在做HTTP POST Method測試的時候，有curl可以做HTTP測試，或是POSTMAN之類的測試工具，可以進行POST測試。

```js
app.set('views', './views');
app.get('/', function (req, res) {
    //渲染範本引擎 ./views/index
    res.render('index',{
        user:{
            name: "abc",
            password: "abc"
        }
    });
});

app.post('/',function (req, res){
    // POST可以使用body-parser解析返回的HTML資料
    // <input name="a">3</> => req.body.a = 3
    // <input name="a[asd]">3</> => req.body.a[asd] = 3
    console.log(JSON.stringify(req.body));
    return res.render('index'); //要用return跳出
});
```

進行curl測試

```sh

curl locahost:3000
# => index.html 檔案
curl -X GET locahost:3000 # get
curl --header "Content-Type: application/json" \
    --request POST \
    --data '{"username":"abc","password":"abc"}' \
    http://localhost:3000
# => index.html 檔案
```
Server console顯示出req.body

```sh
## after post
{"username": abc, "password": abc}
```

使用express的post來拿表單資料，可以透過HTML樣板，如：ejs、swig、pug（jade因名字版權問題改名爲pug）透過標籤的方法得到值，或是使用bodypaser來解析表單內容。

HTMl的部分最重要的部分是`method="post"`的部分要寫，才能使用express的post方法。

```html3
<form method="post">
    <input type="text" name="name"/>
    <input type="text" name="age"/>
    <input type="submit"/>
</form>
```


下面範例在localhost訪問的話會直接顯示出server提供的數值不用在html下面寫document.write()，或是一些XMLHttpRequest、jquery Ajax來處理數值顯示的問題，伺服器可以直接給定數值，這是用範本引擎的優點。

```html
<!-- swig template -->
<form class="form-signin" method="post" action="/">
    {% if message != '' %}
    <div class="alert alert-danger" role="alert">{{ message }}</div>
    {% endif %}
    <label for="inputAccount">帳號</label>
    <input value = "{{ user.name }}" type="text" name="user[name]" id="inputAccount" required="">
    <label for="inputPassword">密碼</label>
    <input value = "{{ user.password }}" type="password" name="user[password]" id="inputPassword" required="">
</form>
``` 

以下是範例：

```html /views/login.html

{% extends 'layouts/sign.html' %}

{% block content %}
<form action="#" method="post">
    {% if message != '' %}
    <div class="alert alert-danger" role="alert">{{ message }}</div>
    {% endif %}
    <div class="form-label-group">
    <input type="text" name="name"/>
    <input type="text" name="age"/>
    <input type="submit"/>

<div class="form-label-group" >
<input type="text" name="user[lastname]" id="inputLastname" class="form-control" placeholder="Last name" required="" autofocus="">
<label for="inputLastname">名字</label>
</div>

<div class="form-label-group" >
<input type="password" name="user[password]" id="inputPassword" class="form-control" placeholder="Password" required="">
<label for="inputPassword">密碼</label>
</div>
<input type="submit" />
</form>
{% endblock %}
```

node.js後端的部分，主要是要把安裝再node_module下面的`body-parser` require進來。

```js /app.js
const mongoose = require('mongoose'); 
// use swig templete + expres.js router
var app = require('express')(),
  swig = require('swig'),
  people;

// This is where all the magic happens!
app.engine('html', swig.renderFile);
app.set('view engine', 'html');

// 優先級大於__dirname，有同名檔案先執行
// serve the static file
const serveStatic = require('serve-static');
app.use(serveStatic('public'));

// set views path
app.set('views', __dirname + '/views');

// get form data from HTML body (must express.post)
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended: true}));

// include other class
require('./routers')(app);

// define local listen port
const port = process.env.PORT || 5000;
app.listen(port);
console.log('Application start on port ' + port);
```

`app.get` 的部分可以使用swig跟HTML溝通，`app.post`的部分可以用`req.body`把表單轉換成json的格式。

```js ./routers/login.js
module.exports = function ( app ) {

    app.get("/login",function(req,res){
        res.render('login');
        /* template locals context */
          title: '管理員登入',
          message: '',
          cmstype: 'Admin Pannel',
          herf_regesit: '/admin/regesit'
    });

    app.post("/ll",function(req,res){
    console.log(req.body);
    console.log(req.body.user);
    console.log(req.body.user.email);
          //自定打印表单数据(參考)
      // console.log(User);
      // var User = new user({
      //     email: user.email,
      //     password: user.password
      // });
    });
}
```

![body-paser 範例](/media/body-paser_ex.png)

