(TBD)

# Usage / 使い方
```
from decotimer.timer import Timer
import time

timer = Timer(user='Taichi Masuyama', description='Sample Usage')

@timer.use_timer
def usage():
    # Namable block
    with timer.block(name='sleep_2sec_1'):
        time.sleep(2)

    # Pause and resume timer
    timer.pause()
    time.sleep(2)
    timer.resume()

    print('Slept well!!!')
    time.sleep(2)

    # Stop completely
    timer.stop()
    time.sleep(2)

# It shows the results
usage()
```

# Output / 出力
```
Slept well!!!

-----------------------------------------
Result                --> 6.009851694107056 s
Whole program ran in  --> 8.01312780380249 s
Paused                --> 2.0005669593811035 s, 1times
Blocks                --> [{'name': 'sleep_2sec_1', 'line': Coming soon..., 'time': 2.0032761096954346}]
Paused + Blocked      --> 4.003843069076538 s
-----------------------------------------
```