#!/usr/bin/env python
# coding=utf8
# File: logger_base.py
"""
Logger Tools
"""

import sys
import time
import numpy

def log_format_time(localtime=None):
    if(localtime is None):
        localtime = time.localtime()
    return time.strftime("%Y%m%d-%H:%M:%S", localtime)

class Logger(object):
    def __init__(self, *args, sum_iter=-1, use_tensorboard=False, field=None):
        self.keys = []
        self.sum_iter = sum_iter
        self.acc_iter = 0
        if(use_tensorboard):
            try:
                import torch
                from torch.utils.tensorboard import SummaryWriter
            except ImportError:
                log_fatal('Must install torch.utils.tensorboard in case use_tensorboard==True')
            if(field is not None):
                self.writer = SummaryWriter(field)
            else:
                self.writer = SummaryWriter()
        else:
            self.writer = None
        for arg in args:
            self.keys.append(arg)

    def __call__(self, *args, epoch=-1, iteration=-1, prefix=None, rewrite=False):
        if(len(args) != len(self.keys)):
            raise Exception(f"Mismatch logger key (n={len(self.keys)}) and value (n={len(args)})")

        log = log_format_time()
        if(prefix is not None):
            log +=f'[{prefix}]'
        if(epoch > -1):
            log += ' ' + "Epoch:%03d"%epoch
        if(iteration > -1 and self.sum_iter > -1):
            progress = (iteration + 1) / self.sum_iter * 100
            log += ' ' + "Progress:%.3f%%"%progress

        def format_value(x):
            if(isinstance(x, float)):
                if((abs(x) < 0.10 or abs(x) > 1.0e+3)):
                    return "%.3e"%x
                else:
                    return "%.3f"%x
            elif(isinstance(x, int)):
                return "%03d"%x
            elif(isinstance(x, list) or isinstance(x, numpy.ndarray)):
                return ",".join(map(format_value, x))
            else:
                return str(x)

        for i, arg in enumerate(args):
            log += ' ' + self.keys[i] + ":" + format_value(arg)
            if(self.writer is not None and iteration > -1):
                self.acc_iter += 1
                self.writer.add_scalar(self.keys[i], float(arg), self.acc_iter)

        if(rewrite):
            log += '\r'
        else:
            log += '\n'
        sys.stdout.write(log)
        sys.stdout.flush()

def log_debug(*msgs, on=True):
    if(on):
        log = log_format_time()
        log +='[\033[32mDEBUG\033[0m]'
        for message in msgs:
            if(isinstance(message, str)):
                log += ' ' + message
            else:
                log += ' ' + str(message)
        log += '\n'
        sys.stdout.write(log)
        sys.stdout.flush()

def log_warn(*msgs, on=True):
    if(on):
        log = log_format_time()
        log +='[\033[33mWARNING\033[0m]'
        for message in msgs:
            if(isinstance(message, str)):
                log += ' ' + message
            else:
                log += ' ' + str(message)
        log += '\n'
        sys.stderr.write(log)
        sys.stderr.flush()

def log_fatal(*msgs):
    log = log_format_time()
    log +='[\033[31mFATAL\033[0m]'
    for message in msgs:
        if(isinstance(message, str)):
            log += ' ' + message
        else:
            log += ' ' + str(message)
    log += '\n'
    raise Exception(log)

# Paint a progress bar
def log_progress(fraction, l=100):
    percentage = int(l * fraction)
    empty = l - percentage
    log = "[\033[32m" + "=" * percentage + " " * empty + "\033[0m]" + " [\033[32m%.2f\033[0m%%]\r" % (percentage * 100 / l)
    if(1.0 - fraction < 1.0e-4):
        log += "\n"
    else:
        log += "\r"
    sys.stdout.write(log)
    sys.stdout.flush()
