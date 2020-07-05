# mongodb日期儲存問題


# mongodb日期儲存問題

今天在試著儲存日期到mongodb的時候，它出現一個錯誤碼，大概`console.log`，出來就長得像是下面那個樣子，意思大概是我的日期格式存不進去我的schema裡面，解決的方法很簡單。

最簡單的兩種方式：

1.  改變date type -> strings
2.  mongoose.save之前改格式

```sh
        message: 'Cast to Date failed for value "2019-22-03" at path "DOB"',
        name: 'CastError',
        stringValue: '"2019-22-03"',
        kind: 'Date',
        value: '2019-22-03',
        path: 'DOB',
        reason: [MongooseError] } },
  _message: 'user validation failed',
  name: 'ValidationError' }
>>>>>> model.save Error
```

<!---more--->

##  改變date type -> strings

```js
var userSchema = new mongoose.Schema({
    fullname: String,
    firstname: String,
    lastname: String,
    email: String,
    DOB: Date, // 改成 String
});
```

## mongoose.save之前改格式

在儲存之前加入如下程式，將日期做轉換：

```js
moment.locale('zh-TW');
// string -> moment.js ->  mongodb
// string -> ISO date 好像是美國日期 -> mongodb 
var t = "2019-05-03"; //日期 from datapicker
t = moment(t, "YYYY-MM-DD");
var b = t.toISOString(); // 把moment的日期轉成 ISO date
console.log("可以給 mongodb 的 date: " + b);

// date -> moment.js -> display
// ISO date -> display
t = moment(b, "YYYY-MM-DD"); // 處理後的日期
var a =  moment(t).format('YYYY-MM-DD'); //轉換成格式
console.log("轉換後拿來顯示用的日期: " + a);

// output
可以給 mongodb 的 ISO date: 2019-05-02T16:00:00.000Z //少一天
轉換後拿來顯示用的日期: 2019-05-02
```

