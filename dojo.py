import multiprocessing
import logging
from practitioners import Deshi, Sensei
import time
import click

CORES = multiprocessing.cpu_count()
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(name)-10s %(message)s'
LOG_DATEFORMAT = '%Y-%m-%dT%H:%M:%S'

@click.command()
@click.option("--cpu_target", default=80, help="CPU Percentage Target to hit")
@click.option("--runtime", default=60, help="Runtime in seconds to work")
@click.option("--log_level", default="INFO", type=click.Choice(["INFO", "DEBUG"]), help="Log level to use")
def main(cpu_target, runtime, log_level):

    # Setup Logging
    level = logging.INFO
    if log_level == "DEBUG":
        level = logging.DEBUG
    logging.basicConfig(level=level, format=LOG_FORMAT, datefmt=LOG_DATEFORMAT)
    log = logging.getLogger("Dojo")


    log.info("FEAR DOES NOT EXIST IN THIS DOJO!")
    log.info("Srudents today: %s Deshi" % CORES)
    log.info("Working for %s seconds" % runtime)
    log.info("HAJIME!")

    instructions = [multiprocessing.JoinableQueue() for i in range(CORES)]
    responses = [multiprocessing.Queue() for i in range(CORES)]
    deshis = [Deshi("Deshi %s" % i, instructions[i], responses[i]) for i in range(CORES)]
    sensei = Sensei(instructions, cpu_target)

    # Sensei Arrives and starts shouting at them...
    log.info("Sensei has arrived!")
    sensei.start()

    # Students arrive and start cleaning the dojo
    for p in deshis:
        p.start()

    time.sleep(runtime)
    sensei.terminate()
    for d in deshis:
        d.terminate()


if __name__ == "__main__":
    main()
