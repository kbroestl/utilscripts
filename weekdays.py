#! /usr/bin/env python

import datetime as dt

def infdays(start=None):
  cur = start if start else dt.datetime.today()
  while True:
    cur = cur + dt.timedelta(days=1)
    yield cur

def due_date(num_days, start=None):
  due_date = None
  weekdays = (d for d in infdays(start) if d.weekday() < 5)
  for i in range(0, num_days):
    due_date = weekdays.next()
  else:
    return due_date


if __name__ == '__main__':
  print due_date(3, dt.datetime(2012,7,12)).strftime("%d/%m/%Y")
