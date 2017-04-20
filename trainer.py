import multiprocessing
import logging
from workouts import Workout
import time

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-8s %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S'
    )
log = logging.getLogger("Trainer")


CORES = multiprocessing.cpu_count()


def main():
    log.info("Starting ---------")
    log.info(" CORES: %s" % CORES)
    workers = [Workout(name=i, affinity=i, cpu_target=65) for i in range(0, CORES)]

    # start the workers
    for w in workers:
        w.start()

    # Kill the workers....
    time.sleep(60)
    for w in workers:
        log.info("STOPPPING WORKER %s" % w.name)
        w.terminate()


if __name__ == "__main__":
    main()
