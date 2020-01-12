from timer_class import Timer

timer = Timer()
for i in range(50000000):
    j = 1+1
print(timer.get_current())
timer.pause_time()
for i in range(50000000):
    j = 1+1
print(timer.get_current())
timer.unpause()
for i in range(50000000):
    j = 1+1
print(timer.get_current())

