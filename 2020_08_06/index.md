# Matlab Linux 亂碼


安裝字體，可以複製Windows的字體`/windows/Windows/Fonts`，詳細方法可以參考[Arch Wiki Microsoft fonts](https://wiki.archlinux.org/index.php/Microsoft_fonts)，如果跟我一樣用雙系統的話，用Arch Wiki的方法打開Matlab之前掛載好windows分區硬碟，字體就會讀的到。

由於enca的格式轉換在我的電腦使用起來有點問題所以只有拿來確認格式

```bash
enca -L chinese ar_rate_1D.m
```

## 轉檔

確認格式之後進行轉檔：

```bash
iconv -f  BIG-5 -t  UTF-8 rate.m -o test1.m
iconv -f  UTF-8 -t  BIG-5 test1.m -o test2.m
```

腳本參考[這裏](https://www.geek-share.com/detail/2729179337.html)，不過要轉換的格式不是GB是BIG-5所以要改一下，未來如果要改可能加入enca判斷格式可能也不錯。

```bash
#!/bin/bash  
# 功能：将BIG-5文件 转换成 UTF-8【解决Windows文件复制到Linux之后乱码问题】  
#read -p "Input Path:" SPATH  
SPATH="."  
#echo $SPATH  
POSTFIX="m"  
param1="$1"  
if [ "$param1" == "win" ];then  
sys1="Linux"  
sys2="Windows"  
format1="UTF-8"  
format2="BIG-5"  
elif [ "$param1" == "linux" ];then  
sys1="Windows"  
sys2="Linux"  
format1="BIG-5"  
format2="UTF-8"  
else  
echo "************** 功能 ************"  
echo "  解决matlab脚本文件在Windows和Linux中移动时出现的乱码问题！"  
echo "  将该脚本复制到程序文件夹中，运行该脚本，它会对当前文件夹及子文件夹中的所有*.m文件进行格式转换，解决乱码问题。"  
echo "  转换到 Linux 的命令: $0 linux"  
echo "  转换到 Window的命令: $0 win"  
exit  
fi  
  
echo "********************************"  
echo "  格式转换中......"  
echo "  从"$sys1"("$format1") 转换到 "$sys2"("$format2")"  
echo "********************************"  
  
FILELIST(){  
filelist=`ls $SPATH `  
for filename in $filelist; do  
if [ -f $filename ];then  
#echo File:$filename  
#echo "${filename#*.}"  
EXTENSION="${filename#*.}"  
#echo $EXTENSION  
if [ "$EXTENSION" == "$POSTFIX" ];then  
#echo "${filename%%.*}"  
echo Processing: $filename  
#iconv  -f $format1 -t $format2 $filename -o $filename  
iconv -f BIG-5 -t UTF-8 $filename -o $filename  
fi  
  
elif [ -d $filename ];then  
cd $filename  
SPATH=`pwd`  
#echo $SPATH  
FILELIST  
cd ..  
else  
echo "$SPATH/$filename is not a common file."  
fi  
done  
}  
cd $SPATH  
FILELIST  
echo "======== Convert Done. ========"  
```

## Memory Overflow

在算一些東西deepleaning的時，matlab常常會有overflow的問題，clear all;之類的不行使用，在這裏看到一個可以用的方法。

修改tmp size

```bash
sudo mount -t tmpfs -o size=100G none /run/media/2TB/tmp
```

```objc
[DeepMIMO_dataset,params]=DeepMIMO_generator(params);
% pack;
% clear all;
% clearvars -except DeepMIMO_dataset params;
evalin('base','save(''DeepMIMO_dataset'')');
evalin('base','save(''params'')');
clearvars -global;
evalin('base','clear');
evalin('base','load(''DeepMIMO_dataset'')');
evalin('base','load(''params'')');
pack;
```

## Class Debug

assign要檢查的變量到workspace

```objc
function [r]=filename()
% do something
    
% assign to base with break points debugs
myVarList={'st', 'ed', 'Hj', 'Wj', 'covj', 'Pj', 'Wintf', 'covtp', 'Wintf', 'covtp', 'cov_intf', 'Pintf', 'rate'};

for indVar = 1:length(myVarList)
    assignin('base',myVarList{indVar},eval(myVarList{indVar}))
end
return r
end
```
