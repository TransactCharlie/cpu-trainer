import logging
import multiprocessing


class Workout(multiprocessing.Process):

    def __init__(self, name=None, affinity=None, cpu_target=None):
        self.log = logging.getLogger("Worker [%s]" % name)
        self.affinity = affinity
        self.do_workout = True
        self.cpu_target = 100 if cpu_target is None else cpu_target

        super().__init__()

    def run(self):
        self.log.info("Starting Workout")

        a, b = 1, 1
        while self.do_workout:
            a, b = b, a + b
            # self.log.info(a)
