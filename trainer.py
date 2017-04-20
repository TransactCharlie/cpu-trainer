import multiprocessing
import logging
from workouts import Workout

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

    for w in workers:
        w.start()


if __name__ == "__main__":
    main()
