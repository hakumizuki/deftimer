(TBD)

# Environments
```
Python: 3.8
```

# Requirements
```
pip install pathlib
```

# Try decotimer with docker
```
$ cd <parent dir of decotimer>
$ docker build -t decotimer python -m unittest.
$ docker run --rm deco_usage
```

# decotimer
```
(TBD)

I'm always welcome for your ideas.
Thanks for visiting my repo :)

English:
It allows you to calculate run time of each functions. See USAGE.md for more information -->

timer = Timer()
@timer.use_timer
def do_something():
    ...

do_something() # this prints the results

Other functions:
You can divide process into blocks and name them.
Coming soon --> File exporting (JSON, CSV)


Japanese:
Python3の関数内の処理時間を計算します。

timer = Timer()
@timer.use_timer
def do_something():
    ...

として関数を呼ぶだけで計測できます。

他にも、、、
Blockで処理を分割したり、処理に名前をつけたりできます。
今後ファイル化(JSON、CSV)も考えています。
```

# Test decotimer
```
$ docker run --rm decotimer python -m unittest
```

# Author
* Taichi Masuyama
* montanha.masu536@gmail.com

# License
"decotimer" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License)
