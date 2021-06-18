from repeated_timer import Repeated_Timer


def timer_tick(*args: tuple, **kwargs: dict):
    # You can put your code in here
    print('timer tick!')


if __name__ == '__main__':
    repeated_timer = Repeated_Timer(interval=1, duration=30, function=timer_tick, args1='args1', args2='args2')
    repeated_timer.start()
    # repeated_timer.stop()
