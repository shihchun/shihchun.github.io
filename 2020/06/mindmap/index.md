# ShortCode 整理



整理一下最近加入的shortcode，`{{}}`會錯誤所以都用`{}`代替，不然會變成這樣，今天換了Loveit發現主題內建了mermaid，所以就改檔案名，暫時擺著，順便加上Loveit有的shortcode，文檔有蠻多可以用的，就去不全部放了。

# Mind


- 根目录
    - 一级目录1
        - 二级目录1
        - 二级目录2
    - 一级目录2


{{< mind >}}
- 根目录
    - 一级目录1
        - 二级目录1
        - 二级目录2
    - 一级目录2
{{< /mind >}}

```
{< mind >}
- 根目录
    - 一级目录1
        - 二级目录1
        - 二级目录2
    - 一级目录2
{< /mind >}
```

[unordered-list-to-mind-map](https://github.com/HunterXuan/unordered-list-to-mind-map)放到`/static/mind/`目錄下面，然後加入`/layouts/shortcodes/mind.html`的全局shortcode，關於這個shortcode我要說一下，在我這裡`{{ .Inner }}`不行用，要用`{{ .Inner | markdownify }}`，就看一下結果就知道了。

![](/media/2020-06-29_PM_6.21.32.png)

![](/media/2020-06-29_PM_6.27.07.png)

```html
<!-- from https://github.com/HunterXuan/unordered-list-to-mind-map -->
<div id="{{ .Get 0 }}" class="mindmap mindmap-lg" style="width:100%;height:300px;border:3px #cccccc dashed;">
    {{ .Inner | markdownify }}
</div>

<script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
<script src="/mind/jquery-3.3.1.min.js"></script>
<link href="/mind/mindmap.css" rel="stylesheet">
<script src="/mind/kity.min.js"></script>
<script src="/mind/kityminder.core.min.js"></script>
<script src="/mind/mindmap.min.js"></script>
<!-- minder 重複加載會顯示我們不想要的結果選一個不加載或是直接刪除檔案 -->
<!-- <script src="/mind/mindmap.js"></script> --> 
```

再來就是`mindmap.js`重複加載的問題，這個檔案重複加載，也就是畫了兩個圖會出現問題，直接變成四個圖，所以要處理一下，出現了圖重複的狀況。

我是直接對`kityminder`、`kitty`這兩個物件名稱做判斷（在瀏覽器找到就直接用了），原因就是每次會用到它的時候大概也是用在這裡，不過似乎不行，可能跟hugo的內部執行順序有關，所以最後還是加到theme裡面，我自己是加載在`theme/layout/posts/single.html`的`</article>`上面一點的地方。

```js
<script>
if (typeof jQuery != "undefined" || typeof kityminder != "undefined") {
	// do something  不能用document.write
	var s=document.createElement('script');
	s.src='/mind/mindmap.min.js';
	document.body.appendChild(s);
}
</script>
```

{{< mind >}}
- mind圖加入
    - shortcode
        - obj: kityminder, kity, jquery 
    - theme
        - script: if(typeof(Obj)!= "undefined")
{{< /mind >}}


# Typeit

{{< typeit >}}
打字 [TypeIt](https://typeitjs.com/) 的 **打字動畫** 的 *段落*...
{{< /typeit >}}

```
{{< typeit >}}
打字 [TypeIt](https://typeitjs.com/) 的 **打字動畫** 的 *段落*...
{{< /typeit >}}

{< typeit >}
打字 [TypeIt](https://typeitjs.com/) 的 **打字動畫** 的 *段落*...
{< /typeit >}
```

{{< typeit code=java >}}
public class HelloWorld {
    public static void main(String []args) {
        System.out.println("Hello World");
    }
}
{{< /typeit >}}

```
{< typeit code=java >}
public class HelloWorld {
    public static void main(String []args) {
        System.out.println("Hello World");
    }
}
{< /typeit >}
下面用 {< typeit code=C# >}，{< typeit code=python >} 測試
```

{{< typeit code=C# >}}
private void Read_btn_Click(object sender, RoutedEventArgs e) {
RfidMeRead();
    if (rawtag == "-1" || rawtag == "A problem occured while communicating with the reader: RFIDME")
    {
        RfidMeEPC = "No tag read !";
    }
    else
    {
        RfidMeEPC = rawtag;
    }
}
{{< /typeit >}}

{{< typeit code=python >}}
class WeatherIterable(Iterable): ## 可以疊代物件
  def __init__(self,cities):
    self.cities = cities
    pass
  
  def __iter__(self):
    return WeatherIterator(self.cities)
{{< /typeit >}}


# Plotly

{{< plotly ns3_ofdm_yans_wifi_model_subplot >}}

```
{< plotly ns3_ofdm_yans_wifi_model_subplot >}
```

# rawhtml

{{< rawhtml>}}
<br><br><br><br>
<button type="button" class="btn btn-primary">Click Me!</button>
<button type="button" class="btn btn-secondary">Click Me!</button>
<button type="button" class="btn btn-success">Click Me!</button>
<button type="button" class="btn btn-danger">Click Me!</button>
<button type="button" class="btn btn-warning">Click Me!</button>
<button type="button" class="btn btn-info">Click Me!</button>
<button type="button" class="btn btn-light">Click Me!</button>
<button type="button" class="btn btn-dark">Click Me!</button>
<button type="button" class="btn btn-link">Click Me!</button>
{{< /rawhtml >}}

```
{< rawhtml>}
<button type="button">Click Me!</button>
{< /rawhtml >}
```


# Music

use Roland JV-1080 vst, kontakt somthing wrong

{{< music url="/mus/Tracktion7 Edit 1 Export 1.wav" name="Remix from Tracktion 7" artist=NaN cover="/lo_img/avator.jpg" >}}

add other kontakt with Roland JV-1080 vst

{{< music url="/mus/abelton_remix.wav" name="Remix from abelton Live" artist=NaN cover="/lo_img/avator.jpg" >}}

```
{< music url="/mus/abelton_remix.wav" name="Remix from abelton Live" artist=NaN cover="/lo_img/avator.jpg" >}
```
