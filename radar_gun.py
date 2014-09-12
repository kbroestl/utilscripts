#! /usr/bin/env python

""" Simple utility,
    given a known distance (96ft as default, override)
    provided at time, passed in as parameter
    Caluculate miles per hour
"""

import argparse

def calculate_mph(d,t):
    fps = calculate_fps(d,t)

    print (fps * 3600)/5280

def calculate_fps(d,t):
    return float(d)/float(t)

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", "--distance", help="Distance: in feet. Defaults to 96")
    parser.add_argument("-t", "--time", help="Time: in Seconds.")

    args = parser.parse_args()

    if args.distance:
        d = args.distance
    else:
        d = 96.0

    if args.time:
        t = args.time
    else:
        t = 0.0

    calculate_mph(d,t)
