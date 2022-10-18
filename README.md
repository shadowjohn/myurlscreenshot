# myurlscreenshot
我的網址截圖機

Author:
  Feather Mountain (https://3wa.tw)
  
編譯方式：
  python 2.7
  
  pip install selenium 
  pip install pillow
  pip install pyinstaller
  
  build.bat 執行後產生 dist\screenshot.exe
  
使用方法：

  URL ScreenShot

  Usage:
  
    python.exe screenshot.py -h
    
  Dist:  
    screenshot.exe -u <URL> -d <Delay[ms]> -o <outputfile>

  Example:
    screenshot.exe -u "https://3wa.tw" -d 3000 -o "output_3wa.png"

