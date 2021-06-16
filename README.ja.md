# deftimer
Python3の関数内の処理時間を計算します。  

```
timer = Timer()
@timer.use_timer
def do_something():
    ...
```

として関数を呼ぶだけで計測できます。  

他にも、、、  
Blockで処理を分割したり、処理に名前をつけたりできます。  
今後ファイル化(JSON、CSV)も考えています。  