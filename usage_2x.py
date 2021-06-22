'''
This Example is to demonstrate how to use timer in Python 2.x
'''

from repeated_timer_2x import Repeated_Timer_2x


def timer_tick(remaining_time, *args, **kwargs):
    # You can put your code in here
    print('timer tick!')
    print(remaining_time)


if __name__ == '__main__':
    repeated_timer = Repeated_Timer_2x(interval=1, duration=30, function=timer_tick, args1='args1', args2='args2')
    repeated_timer.start()
    # repeated_timer.stop()
