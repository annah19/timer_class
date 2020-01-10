import time

class Timer:
    def __init__(self):
        self.start = time.time()
        self.pause = 0
        self.is_paused = False


    def set_start(self):
        self.start = time.time()

    def get_current(self):
        if self.is_paused:
            return self.pause
        else:
            return self.pause + (time.time() - self.start)


    def pause_time(self):
        self.pause = self.pause + time.time() - self.start()# self.start + self.current()
        self.is_paused = True


    def unpause(self):
        self.set_start()
        self.is_paused = False

        