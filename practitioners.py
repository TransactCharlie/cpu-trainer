import logging
import multiprocessing
import time
import queue
import psutil


class Sensei(multiprocessing.Process):

    def __init__(self, students, target_cpu):
        self.log = logging.getLogger("SENSEI")
        self.students = students
        self.target_cpu = target_cpu
        self.upper_work_threshold = target_cpu + 3
        self.lower_work_threshold = target_cpu - 3

        super().__init__()

    def run(self):
        # Make an initial call ot psutil cpu_times to start the measurement
        psutil.cpu_percent(percpu=True, interval=1)

        # Monitor the practitioners and make them go slower or faster as required.
        reps = 0
        self.log.info("I want %s percent effort from EVERYONE!" % self.target_cpu)
        while True:
            work = psutil.cpu_percent(percpu=True, interval=1)
            for c in [c for c, p in enumerate(work) if p > self.upper_work_threshold]:
                self.log.debug("Deshi [%s] SLOW DOWN!" % c)
                self.students[c].put("-")
            for c in [c for c, p in enumerate(work) if p < self.lower_work_threshold]:
                self.log.debug("Deshi [%s] GO FASTER!" % c)
                self.students[c].put("+")
            reps += 1
            if reps % 100:
                self.log.info(work)

    def terminate(self):
        self.log.info("Thats enough for today everyone!")
        super().terminate()


class Deshi(multiprocessing.Process):

    sample_period = 5000
    rest_scaling = 0.003

    def __init__(self, name, instruction_queue, response_queue):
        self.log = logging.getLogger(name)
        self.sleep_time = 0.03
        self.instructions = instruction_queue
        self.responses = response_queue
        # Call Super
        super().__init__()

    def run(self):
        self.log.info("Ohayou Gozaimasu Sensei!")
        a, b = 1, 1
        while True:
            # do some work!
            for i in range(self.sample_period):
                a, b = b, a + b

            # Check to see if we need to adjust our rest time
            instruction = None
            try:
                instruction = self.instructions.get(block=False)
            except queue.Empty as e:
                pass

            if instruction == "STOP":
                self.log.info("Sensei arigatou gozaimasu! phew...")
                break

            if instruction == "+":
                if self.sleep_time >= self.rest_scaling:
                    self.sleep_time -= self.rest_scaling
                self.log.debug("Speeding up... Rest Interval %s" % self.sleep_time)

            if instruction == "-":
                self.sleep_time += self.rest_scaling
                self.log.debug("Slowing up... Rest Interval %s" % self.sleep_time)


            time.sleep(self.sleep_time)

    def terminate(self):
        self.log.info("Sensei, doumo arigatou gozaimasu")
        super().terminate()
