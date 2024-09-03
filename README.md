# ChineseMorse
```
usage: hanzimorse [-h] [-v] [-l LOADNAME] [-s standard] [-i INPUT_STRING] [-m INPUT_MORSE]

                            Hanzi <- Telegraph Code -> Morse
                            (中文)漢字 <-- 商碼 --> 電報碼

options:
  -h, --help            show this help message and exit
                        显示本指南后结束程序
  -v, --verbose         run in verbose mode
                        使用話癆模式
  -l LOADNAME, --load LOADNAME
                        load input from a file path (LOADNAME)
                        由文件路徑(LOADNAME)导入
  -s standard, --standard standard
                        specify a standard to use
                        選擇一種字型(T-繁, S-簡)
                        default: T
                        默認使用繁體字 因爲繁體字庫涵蓋範圍更廣
  -i INPUT_STRING, --input INPUT_STRING
                        manually feed a string of text (INPUT_STRING)->Morse Code
                        手動輸入字符串(INPUT_STRING)->電碼
  -m INPUT_MORSE, --morse INPUT_MORSE
                        manually feed a string of formatted morse code (INPUT_MORSE)->Text
                        手動輸入電碼字符串(INPUT_MORSE)->明文

A program by K6MLX.
由K6MLX開發製作.
```
