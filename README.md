# Python Repeated Timer

![repeated timer logo](https://user-images.githubusercontent.com/41291493/122342770-f1d50d80-cf7f-11eb-87ec-844bcc1343d5.png)

![Python](https://img.shields.io/badge/python-2.7%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)
![PyPI](https://badge.fury.io/py/tensorflow.svg)

python-repeated-timer is a open-source and highly performing timer using only standard-libraries, and users may change the interval and duration of the event as they wish.
Without any additional thread, GUI freezing issue won't be happening. 
Also, performance of the timer won't be affected by any event. 

## Features:
* Python Repeated Timer is a open-source library based on Thread Timer, and this asynchronously triggers the event every N seconds.

![reactor pattern](https://user-images.githubusercontent.com/41291493/122346179-a3c20900-cf83-11eb-91a6-8eca01fa4c7d.png)

* For this only uses python standard-library, no additional library is required.
* Easy to implement by simply using functions such as start(), stop(). Also, this timer is stable on multiple calls.
* No matter how heavy timer_tick() is, the timer's interval & duration won't be affected.
* It is possible to insert the argument so you can customize the timer as you want.
* You may change the interval & duration of the timer.
* No freezing issue occurs with GUI libraries such as Tkinter.

## Install (~ing)
To install the current release:

```shell
$ pip install python-repeated-timer
```

## Usage:

If you want to use a repeated timer in a python code, see this [tutorials](https://github.com/takhyun12/python-repeated-timer/blob/main/usage.py)

```shell
$ python
```

``` python
>>> from repeated_timer import Repeated_Timer
>>> def timer_tick(remaining_time: int, *args: tuple, **kwargs: dict):
>>>   # You can put your code in here
>>>   print('timer tick!')
>>>   print(remaining_time)  # You can use remaining_time
>>>
>>> repeated_timer = Repeated_Timer(interval=1, duration=30, function=timer_tick, args1='args1')
>>> repeated_timer.start()
>>> # repeated_timer.stop()
```

## Usage for GUI(with TKinter)

![tkinter_tutorial](https://user-images.githubusercontent.com/41291493/122524359-01715680-d053-11eb-9292-10927552e96c.png)

If you want to use repeated timer with tkinter, see this [tutorials](https://github.com/takhyun12/python-repeated-timer/blob/main/usage_gui.py)

## Performance metrics:

this repository is still under construction.

## TODO / Known Issues:

* this repository is still under construction.
