import multiprocessing
import logging
from practitioners import Deshi, Sensei
import click
from flask import Flask


CORES = multiprocessing.cpu_count()
LOG_FORMAT = '%(asctime)s %(levelname)-8s %(name)-10s %(message)s'
LOG_DATEFORMAT = '%Y-%m-%dT%H:%M:%S'
app = Flask(__name__)


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
    log.info("Students today: %s Deshi" % CORES)
    log.info("Working for %s seconds" % runtime)
    log.info("HAJIME!")

    student_instructions = [multiprocessing.JoinableQueue() for i in range(CORES)]
    sensei_instructions = multiprocessing.JoinableQueue()
    responses = [multiprocessing.Queue() for i in range(CORES)]
    deshis = [Deshi("Deshi %s" % i, student_instructions[i], responses[i], True) for i in range(CORES)]
    sensei = Sensei(student_instructions, cpu_target, sensei_instructions)

    # Sensei Arrives and starts shouting at them...
    log.info("Sensei has arrived!")
    sensei.start()

    # Students arrive and start cleaning the dojo
    for p in deshis:
        p.start()

    # Management Flask Object
    app = Flask(__name__)

    @app.route("/begin")
    def begin():
        log.info("Sensei: BEGIN")
        sensei_instructions.put("BEGIN")
        return "BEGINNING"

    @app.route("/rest")
    def rest():
        log.info("Sensei: REST")
        sensei_instructions.put("REST")
        return "RESTING"

    # start it
    from waitress import serve
    serve(app, host="0.0.0.0", port=8888)

if __name__ == "__main__":
    main()
