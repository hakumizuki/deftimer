# Alpha  
Deftimer is now alpha stage.  
Throw me issues!  

# Environments
```
Python: >=3.6, <4
```

# Requirements
```
pip install pathlib
```

# Try deftimer with docker
```
$ cd <parent dir of deftimer>
$ docker build -t deftimer .
$ docker run --rm deftimer
```

# deftimer
(TBD)  

* quick start  
It allows you to calculate run time of each functions. See USAGE.md for (more information)[https://github.com/hakumizuki/deftimer/blob/main/USAGE.md]  

```
timer = Timer()
@timer.use_timer
def do_something():
    ...

do_something() # this prints the results
```

## document
* ```Timer(user='', description='')```  
Initialize a Timer instance first.  
You will use the instance to decorate a function, use other methods.  
```
timer = Timer()

@timer.use_timer
def something():
    ...
```

* ```@timer.use_timer(detail=True)``` decorator  
```params```  
detail:  It shows full results when detail is True.  

```description```  
This decorator allows the function to be inspected by a timer instance.  

* ```timer.pause() & timer.resume()```  
You will sandwitch a process to omit the process from timer counting.  
The process time occured between pause&resume will not be counted as a result.  
```
@timer.use_timer
def something():
    timer.pause()
    time.sleep(5)
    timer.resume()
```
The result will be 0 sec.

* ```timer.block(name=None, exclude=True)``` context manager  
```params```  
name:     You can name the block. The name will show up in results.  
exclude:  You can choose whether or not you exclude the process time that took to run the block from results.  
```
@timer.use_timer
def something():
    with timer.block(name='sleep_2sec_1'):
        time.sleep(2)
```

* ```timer.stop()```  
Use this when you want to stop the timer.  
```
@timer.use_timer
def something():
    timer.stop()
    # any process after stop() will be excluded from results.
```

* Results  
(TBD)  

Below is an example of full results.  
```
-----------------------------------------
Result                --> 4.0531158447265625e-06 s
Whole program ran in  --> 4.0531158447265625e-06 s
Paused                --> 0 s, 0times
Blocks                --> 0 blocks: []
Paused + Blocked      --> 0 s
-----------------------------------------
```

* coming soon...
File exporting (JSON, CSV)  
Average calculation  


# Test deftimer
```
$ docker run --rm deftimer python -m unittest
```
Note: It might fail depending on your pc spec.  

# Author
* Taichi Masuyama
* montanha.masu536@gmail.com

I always welcome your ideas!  
Thanks for visiting my repo :)  

# License
"deftimer" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License)  

