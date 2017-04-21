import multiprocessing
import logging
from practitioners import Deshi, Sensei
import time

log_level = logging.INFO
log_format = '%(asctime)s %(levelname)-8s %(name)-10s %(message)s'
log_dateformat = '%Y-%m-%dT%H:%M:%S'
logging.basicConfig(level=log_level, format=log_format, datefmt=log_dateformat)
log = logging.getLogger("Dojo")

CORES = multiprocessing.cpu_count()


def main():
    log.info("FEAR DOES NOT EXIST IN THIS DOJO!")
    log.info("Srudents today: %s Deshi" % CORES)
    log.info("HAJIME!")

    instructions = [multiprocessing.JoinableQueue() for i in range(CORES)]
    responses = [multiprocessing.Queue() for i in range(CORES)]
    deshis = [Deshi("Deshi %s" % i, instructions[i], responses[i]) for i in range(CORES)]
    sensei = Sensei(instructions, 80)

    # Sensei Arrives and starts shouting at them...
    log.info("Sensei has arrived!")
    sensei.start()

    # Students arrive and start cleaning the dojo
    for p in deshis:
        p.start()

    time.sleep(90)
    sensei.terminate()
    for d in deshis:
        d.terminate()


if __name__ == "__main__":
    main()
