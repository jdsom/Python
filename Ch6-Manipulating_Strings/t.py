import sys, time
try:
    increase = 0
    increaseTrue = True
    while True:
        print(' ' * increase, end='')
        print('******')
        time.sleep(0.1)
        if increaseTrue:
            increase += 1
            if increase == 20:
                increaseTrue = False
        else:
            increase -= 1
            if increase == 0:
                increaseTrue = True
except KeyboardInterrupt:
    sys.exit()