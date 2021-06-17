# Python Repeated Timer

![repeated timer logo](https://user-images.githubusercontent.com/41291493/122342770-f1d50d80-cf7f-11eb-87ec-844bcc1343d5.png)

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)

this repository is still under construction.

## Features:
* Python Repeated Timer is a open-source library based on Thread Timer, and this asynchronously triggers the event every N seconds.

![reactor pattern](https://user-images.githubusercontent.com/41291493/122346179-a3c20900-cf83-11eb-91a6-8eca01fa4c7d.png)

* For this only uses python standard-library, no additional library is required.
* Easy to implement by simply using functions such as start(), stop(). Also, this timer is stable on multiple calls.
* It is possible to insert the argument so you can customize the timer as you want.
* You may change the interval & duration of the timer.
* No freezing issue occurs with GUI libraries such as Tkinter.

## Usage:

If you want to use a repeated timer in a python code, see this [tutorials](https://github.com/takhyun12/python-repeated-timer/blob/main/usage.py)

```shell
$ python
```

``` python
>>> from repeated_timer import Repeated_Timer
>>> def timer_tick(*args: tuple, **kwargs: tuple):
>>>   # You can put your code in here
>>>   print('timer tick!')
>>>
>>> repeated_timer = Repeated_Timer(interval=1, duration=30, function=timer_tick, args1='args1', args2='args2')
>>> repeated_timer.start()
>>> # repeated_timer.stop()
```

## Usage for GUI(with TKinter)

If you want to use repeated timer with tkinter, see this [tutorials](https://github.com/takhyun12/python-repeated-timer/blob/main/usage.py)

## Performance metrics:

this repository is still under construction.

## TODO / Known Issues:
* this repository is still under construction.
