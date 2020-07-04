# 用Javascript將圖片轉換成Base64


# 使用FileReader

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <!-- Word.value=&#39;&#39; -->
    <input id="upload_file" type="file">
    <input value="顯示Base64成圖片：" type="button" onclick="prev();">
    <div class="strong red" id="img_size"></div>
    <textarea id="base64_output"></textarea>
	<img id="img_prev" src="" >
	<script>
		document.getElementById("upload_file").onchange = function(){
			var file = document.getElementById("upload_file").files[0];
			console.log(file);
			var reader = new FileReader();
			reader.readAsDataURL(file); // get Base64
			reader.onload = function(){ // get generate value
				console.log(reader.result);
				var result = reader.result;
				document.getElementById("base64_output").value = result;
			}
		}
		function prev() {
			document.getElementById("img_prev").src = document.getElementById("base64_output").value;
        }
	</script>
</body>
</html>
```

![](/media/Snipaste_2019-03-28_20-44-33.png)


```html
<input id="upload_file" type="file" multiple>
<input value="顯示Base64成圖片：" type="button" onclick="prev();">
<div class="strong red" id="img_size"></div>
<textarea id="base64_0"></textarea>
<img id="img_prev_0" src="">
<textarea id="base64_1"></textarea>
<img id="img_prev_1" src="">
<textarea id="base64_2"></textarea>
<img id="img_prev_2" src="">
<textarea id="base64_3"></textarea>
<img id="img_prev_3" src="">
<script><!-- 這個不行用 -->
	document.getElementById("upload_file").onchange = function () {
		var files = document.getElementById("upload_file").files;
		console.log("count："+files.length);
			k=0
			for(i=0;i<=files.length;i++)
			var f = document.getElementById("upload_file").files[i];
			console.log(i);
			var reader = new FileReader();
			reader.readAsDataURL(f); // get Base64
			reader.onload = function () { // get generate value
				var result = reader.result;
				console.log(result);
				document.getElementById("base64_"+k).value = result;
			}
	}
	function prev() {
		document.getElementById("img_prev").src = document.getElementById("base64_output").value;
		// document.getElementById("img_prev_"+i).src = document.getElementById("base64_"+i).value;
	}
</script>
<script><!-- 這個才可以用 -->
	function seebefore(a){
		console.log('show '+a)
		var f = document.getElementById('files').files[a];
		var freader = new FileReader();
		freader.onload = function(e){
			console.log('set img'+a);
			//$('#imgUL').append($('<li></li>').append($('<img />').attr('src', this.result)));
			$('#img'+a).attr('src', this.result);
			document.getElementById("base64_"+a).value = freader.result;
		}
		freader.readAsDataURL(f);
	}
	$(function(){
		$('#files').change(function(){
			console.log('change start');
			//$('#imgUL li').remove();
			$.each(this.files, function(a,b){
				seebefore(a);
			})
		});
	});
</script>
```


[參考](https://blog.csdn.net/renzhenhuai/article/details/16891507 )

```html 
<div id="d1"></div>
<script>
//HTML
function a(){
document.getElementById("d1").innerHTML="<img src='http://baike.baidu.com/cms/rc/240x112dierzhou.jpg'>";
}
a();
//方法
function b(){
var d1=document.getElementById("d1");
var img=document.createElement("img");
img.src="http://baike.baidu.com/cms/rc/240x112dierzhou.jpg";
d1.appendChild(img);
}
b();
//对象
function c(){
var cc=new Image();
cc.src="http://baike.baidu.com/cms/rc/240x112dierzhou.jpg";
document.getElementById("d1").appendChild(cc);
}
c();
</script>
```

