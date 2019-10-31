import sys
import time
import datetime
import random


def pause_with_progress(t):
  for remaining in range(t, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} minutes remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(60)

def time_delay(low=3, high=7):
    sec = round(random.uniform(low,high), 3)
    sys.stdout.write("Pausing for " + str(sec) + " seconds")
    t = 0
    
    while t < sec:
      sys.stdout.write('.')
      sys.stdout.flush()
      time.sleep(sec/3)
      t = t + sec/3

    sys.stdout.write('\n')

def get_time_delta(start_time):
    time_now = datetime.datetime.now()

    t_delta = time_now - start_time
    t_delta_in_mins = round(t_delta/datetime.timedelta(minutes=1),2)
    
    return(t_delta_in_mins)

