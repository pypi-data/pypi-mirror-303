import time

class stopwatch:
    def __init__(self):
        self.timers = {}
    def click(self, tag):
        if tag not in list(self.timers.keys()): # click to start
            self.timers[tag] = {}
            self.timers[tag]['running'] = True
            self.timers[tag]['lap'] = time.time()
            self.timers[tag]['total'] = 0.
            return 
        if not self.timers[tag]['running']: # click to continue
            self.timers[tag]['running'] = True
            self.timers[tag]['total'] += time.time()-self.timers[tag]['lap']
            self.timers[tag]['lap'] = time.time()
        else: # click to pause
            self.timers[tag]['running'] = False
            self.timers[tag]['total'] += time.time()-self.timers[tag]['lap']
            return self.timers[tag]['total']
    def read(self, tag):
        return self.timers[tag]['total']
    def read_sum(self):
        return_sum = 0
        for key in list(self.timers.keys()):
            return_sum += self.timers[key]['total']
        return return_sum