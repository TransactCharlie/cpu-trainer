# cpu-trainer
Python program that tries to set cpu core(s) to a certain percentage utilisation for load / autoscale testing

## Usage
Run the image from dockerhub. Command line switches are passed to the container.
```
docker run transactcharlie/cpu-trainer --help
```
Output:
```
> docker run transactcharlie/cpu-trainer --help                                                    ✓  2740  17:11:50
Usage: dojo.py [OPTIONS]

Options:
  --cpu_target INTEGER      CPU Percentage Target to hit
  --runtime INTEGER         Runtime in seconds to work
  --log_level [INFO|DEBUG]  Log level to use
  --help                    Show this message and exit.
```

With default parameters the cpu_target is 80% and the runtime is 60 seconds. You should see output like this:

```
> docker run transactcharlie/cpu-trainer                                                         ✓  2741  17:19:51
2017-04-21T16:21:58 INFO     Dojo       FEAR DOES NOT EXIST IN THIS DOJO!
2017-04-21T16:21:58 INFO     Dojo       Srudents today: 2 Deshi
2017-04-21T16:21:58 INFO     Dojo       Working for 60 seconds
2017-04-21T16:21:58 INFO     Dojo       HAJIME!
2017-04-21T16:21:58 INFO     Dojo       Sensei has arrived!
2017-04-21T16:21:58 INFO     Deshi 0    Ohayou Gozaimasu Sensei!
2017-04-21T16:21:58 INFO     Deshi 1    Ohayou Gozaimasu Sensei!
2017-04-21T16:21:59 INFO     SENSEI     I want 80 percent effort from EVERYONE!
2017-04-21T16:22:00 INFO     SENSEI     [3.1, 3.1]
2017-04-21T16:22:01 INFO     SENSEI     [10.1, 7.2]
2017-04-21T16:22:02 INFO     SENSEI     [15.5, 17.1]
...
...
2017-04-21T16:22:55 INFO     SENSEI     [81.6, 80.2]
2017-04-21T16:22:56 INFO     SENSEI     [80.8, 77.2]
2017-04-21T16:22:57 INFO     SENSEI     [83.8, 81.2]
2017-04-21T16:22:58 INFO     SENSEI     Thats enough for today everyone!
2017-04-21T16:22:58 INFO     Deshi 0    Sensei, doumo arigatou gozaimasu
2017-04-21T16:22:58 INFO     Deshi 1    Sensei, doumo arigatou gozaimasu
```

## Build / DockerHub Status
[![Build Status](https://travis-ci.org/TransactCharlie/cpu-trainer.svg?branch=master)](https://travis-ci.org/TransactCharlie/cpu-trainer)
[![](https://images.microbadger.com/badges/image/transactcharlie/cpu-trainer.svg)](https://microbadger.com/images/transactcharlie/cpu-trainer "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/transactcharlie/cpu-trainer.svg)](https://microbadger.com/images/transactcharlie/cpu-trainer "Get your own version badge on microbadger.com")