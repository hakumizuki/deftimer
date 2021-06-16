"""Test Page
I always welcome your ideas.
Thanks for visiting my repo :)

Taichi Masuyama <montanha.masu536@gmail.com>
"""

from deftimer.timer import Timer
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

usage()
