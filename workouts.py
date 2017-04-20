import logging
import multiprocessing
import psutil
import os
import time


class Workout(multiprocessing.Process):

    sample_period = 5000

    def __init__(self, name=None, affinity=None, cpu_target=None):
        self.log = logging.getLogger("Worker [%s]" % name)
        self.affinity = affinity
        self.do_workout = True
        self.cpu_target = cpu_target
        self.check_cpu_load = True if cpu_target else False
        self.sleep_time = 0
        if affinity:
            self.set_affinity()

        # Make inital cpu_percetn_check to throwaway fake values
        self.get_cpu_percentage()

        # Call Super
        super().__init__()

    def get_cpu_percentage(self):
        return psutil.cpu_percent(percpu=True)[self.affinity]

    def set_affinity(self):
        p = psutil.Process(os.getppid())
        #p.cpu_affinity(self.affinity)

    def run(self):
        self.log.info("Starting Workout")

        a, b = 1, 1
        while self.do_workout:
            # do some work!
            for i in range(0, self.sample_period):
                a, b = b, a + b

            if self.check_cpu_load:
                percentage = self.get_cpu_percentage()
                if percentage > self.cpu_target:
                    self.sleep_time += 0.0005
                else:
                    self.log.info("TOO LAZY!!! WORK HARDER [CPU %s, sleep: %s]" % (percentage, self.sleep_time))
                    if self.sleep_time > 0.0005:
                        self.sleep_time -= 0.0005



            time.sleep(self.sleep_time)