#!/bin/python3

import argparse

from psycopg2 import connect

from modules.simple import SimpleClient
from modules.help import print_logo

parser = argparse.ArgumentParser()
parser.add_argument('--connect', type=str, required=False)
parser.add_argument('--host', type=None, required=False)

args = parser.parse_args()

print_logo()

if connect:
    SimpleClient().client_connect(args.connect)
