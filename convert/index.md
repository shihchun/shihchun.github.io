# 檔案格式轉換


# imagemagick

Linux imagemagick 格式 讓人

```sh
# gif 壓縮
convert raw.gif -fuzz 23.5% -layers Optimize new_image.gif

# 格式轉換
convert test.jpg test.png

# 壓縮圖片
convert a.png -quality 80 a.jpg

# 批次處理 -exec cmd {}\;

find *.png -exec convert {} -quality 80 {}.jpg \;

rename .png.jpg .jpg *.png.jpg
```
