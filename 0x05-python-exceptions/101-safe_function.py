#!/usr/bin/python3

def safe_function(fct, *args):
    try:
        fct(args)
    except:
        pass
