# webpack 安裝


# webpack 使用

```sh
## webpack 3.x & 之前
webpack hello.js hello.bundle.js

## npx 可寫可不寫 webpack 4.x
npx webpack hello.js --output-filename hello.bundle.js --output-path  --mode development 

 main  [emitted]  main
Entrypoint main = hello.bundle.js
[./hello.js] 20 bytes {main} [built]

## bundle出來的檔案結果應該要一樣
## 裡面寫了 console.log("test");
λ node hello.js
test
λ node hello.bundle.js
test
```

<!-- more -->

# 環境設定

這裡使用chocolatey管理器安裝nvm（node.js版本管理器）

## 安裝chocolatey

打開CMD安裝[chocolatey](https://chocolatey.org/install)

```sh
@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
```

## 安裝nvm和node

```sh
choco install nvm
```

安裝[node.js](https://nodejs.org/en/) LTS版本

![](/media/Snipaste_2019-03-12_16-52-22.png)

```sh
nvm install 10.15.3
nvm on
```

## 設定npm環境變量

由於之前chocolatey安裝過nvm了，所以環境變量已經加好了，但是npm global的變數沒有加進去，右下圖可知路徑是

```sh
C:\ProgramData\nvm\v10.15.3\node_modules\npm
```

![](/media/Snipaste_2019-03-12_16-58-42.png)


然後加入環境變量即可

![](/media/Snipaste_2019-03-12_17-03-13.png)


## 備份環境變數

以防萬一記得備份環境變量哦，在Environment右鍵匯出，下次出事的時候又沒有`COMPUTER\HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002`、`WINDOWS/System32/config/Regbackup`備份的時候才不會焦頭爛額。

```sh
## 打開regedit註冊表
COMPUTER\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment
```

![](/media/Snipaste_2019-03-12_17-12-11.png)

