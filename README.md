# python repeated timer

![repeated timer logo](https://user-images.githubusercontent.com/41291493/122342770-f1d50d80-cf7f-11eb-87ec-844bcc1343d5.png)

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)

this repository is still under construction.

## Features:
* Thread Timer를 기반으로 주기적으로 반복되는 이벤트를 실행하는 비 차단 방식으로 구현

![reactor pattern](https://user-images.githubusercontent.com/41291493/122345732-24343a00-cf83-11eb-9941-242c4a28404d.png)

* 표준 라이브러리만 사용하여 외부 종속성 없음
* 타이머의 start(), stop()이 자유로우며, 다중 호출에도 안전함
* timer 이벤트에 인수를 원하는대로 자유롭게 지정하여 사용할 수 있음
* interval, duration을 원하는대로 쉽게 수정할 수 있음
* tkinter 등 GUI 프로그래밍에서 GUI Freezing 문제가 발생하지 않음

## Usage:

```shell
$ python
```

``` python
>>> from repeated_timer import Repeated_Timer
>>> repeated_timer = Repeated_Timer(interval=1, duration=30, args1='args1', args2='args2')
>>> repeated_timer.start()
>>> # repeated_timer.stop()
```

## Usage for GUI(TKinter)

If you want to use repeated timer with tkinter, see this [tutorials](https://github.com/takhyun12/python-repeated-timer/blob/main/usage.py)

## TODO / Known Issues:
* this repository is still under construction.
