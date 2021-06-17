from repeated_timer import Repeated_Timer

if __name__ == '__main__':
    repeated_timer = Repeated_Timer(interval=1, duration=30, args1='args1', args2='args2')
    repeated_timer.start()
    # repeated_timer.stop()