#!/usr/bin/python3

import sys, traceback


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("Exception: {}".format(traceback.format_exc()
                                     .strip().splitlines()[-1][12:]))
        return False
