# msys2 環境建立


## install

```sh
# install msys2
choco install msys2
# add to cmder
# *"C:\tools\msys64\msys2_shell.cmd" -msys2 -defterm -here -no-start 
# add to win11 open in terminal
# "C:\tools\msys64\msys2_shell.cmd" -msys2 -defterm -here -no-start 
```


```sh
pacman -Syyu
pacman -S git vim gcc mingw-w64-x86_64-toolchain
pacman -S msys2-w32api-headers msys2-w32api-runtime # windows cpp api ex: windows.h
pacman -S mingw-w64-x86_64-gsl
pacman -S mingw-w64-x86_64-gtk3
# Qt
# 32 bit
pacman -S --needed mingw-w64-i686-qt5-static mingw-w64-i686-qt-creator mingw-w64-i686-clang mingw-w64-i686-gdb mingw-w64-i686-cmake
# 64 bit
pacman -S --needed mingw-w64-x86_64-qt5-static mingw-w64-x86_64-qt-creator mingw-w64-x86_64-clang mingw-w64-x86_64-gdb mingw-w64-x86_64-cmake

```

## Others

### depoly espidf toolchain

```
wget https://dl.espressif.com/dl/xtensa-esp32-elf-win32-1.22.0-61-gab8375a-5.2.0.zip
unzip xtensa-esp32-elf-win32
export IDF_PATH="C:\xtensa-esp32-elf"
```

### Portable python

加入環境變數

```sh
echo %path% # 加入後存在..
C:\Portable Python-3.10.5 x64\App\Python
```


```sh
python -m ensurepip --upgrade
python -m pip install --upgrade pip
python -m pip install numpy scipy pandas pywin32 matplotlib plotly==4.8.2
```

### nvm

```sh
choco install nvm
nvm install 16.17.1 # or nvm install node
nvm list
nvm use 16.17.1
Now using node v16.17.1 (64-bit)
npm -v
node -v
```

## Ref

- [Qt install](https://blog.owo9.com/904/install-qt-static-with-msys2/)
- [Gtk](https://opensourcedoc.com/windows-programming/mingw-msys/)
- [ESP32 Tool Chain](https://gitdemo.readthedocs.io/en/latest/windows-setup.html)
