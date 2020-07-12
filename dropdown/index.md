# Dropdown Terminal


Resently I　use the Manjaro KDE, and I very love the functionilary of the dropdown terminal.

Today I wanna install it on my own PC and MacOS.

# On Windows

```sh
choco install cmder
```



![](/media/Snipaste_2020-07-12_12-05-03.png)

the *.reg file for enable the shortcut, save it and double click

```s
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\Background\shell\Cmder]
@="Open Cmder Here"
"Icon"="C:\\tools\\cmder\\Cmder.exe,0"

[HKEY_CLASSES_ROOT\Directory\Background\shell\Cmder\command]
@="\"C:\\tools\\cmder\\Cmder.exe\" \"%V\""

[HKEY_CLASSES_ROOT\Directory\shell\Cmder]
@="Open Cmder Here"
"Icon"="C:\\tools\\cmder\\Cmder.exe,0"

[HKEY_CLASSES_ROOT\Directory\shell\Cmder\command]
@="\"C:\\tools\\cmder\\Cmder.exe\" \"%1\""
```

![](/media/Snipaste_2020-07-12_12-08-39.png)

Then you can use the `Ctrl`+ `~` to open the drop down terminal.

## wsl install to other disk

```sh
choco install lxrunoffline
icacls D:\virtual_machine\wsl /grant "chenw:(OI)(CI)(F)" # give permision to open
lxrunoffline list
Ubuntu-18.04
lxrunoffline move -n Ubuntu-18.04 -d D:\wsl\virtual_machine\installed\Ubuntu-18.04 # wait for it
lxrunoffline get-dir -n Ubuntu-18.04
D:\virtual_machine\wsl\installed\Ubuntu-18.04
```

## ssh in wsl

You need to add more permision setting on `~/.ssh/config` file

```sh
git config --global user.name "git_username"
git config --global user.email "git_email"
mkdir ~/.ssh
touch ~/.ssh/config
nano ~/.ssh/config
```

Add to `~/.ssh/config`
```sh
# Github
Host github.com
    HostName github.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_rsa
# Gitlab
Host gitlab.com
    HostName gitlab.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/id_ed25519
```

Add the permision

```sh
chmod 600 ~/.ssh/config
```

# On MacOS

```sh
brew cask instal iterm2
```

![](https://www.sharmaprakash.com.np/assets/images/posts/guake-like-terminal-mac/hotkey-window.png)

![](https://i.stack.imgur.com/QXDRd.png)
