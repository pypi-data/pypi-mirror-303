""" This module provides functionality for checking the running time performance of code. """

from time import time
from typing import Callable


def compute_average_running_time(callback_func: Callable, args: tuple = (),
                                 n_repeats: int = 10) -> float:
    """ Computes the average running time of a function evaluation for given number of repeats.

    :param callback_func: the function to be evaluated
    :param args: arguments to the callback
    :param n_repeats: > 1, number of repeats of the function evaluation
    :return: average_running_time_in_seconds
    """

    t = time()

    for i in range(n_repeats):
        callback_func(*args)

    running_time_in_seconds = time() - t
    average_running_time_in_seconds = running_time_in_seconds / n_repeats
    return average_running_time_in_seconds


if __name__ == "__main__":
    import numpy as np
    n_reps = 100
    print("Average running time = {:.4f}s (repeats = {:d}).".format(
        compute_average_running_time(np.exp, (np.zeros((10 ** 7,)),), n_reps), n_reps))
