#!/usr/bin/env python

import random


def random_generrater():
    string = ''
    for n in range(0, 8):
        number = random.randint(0, 9)
        string += str(number)
    # string += '\n'
    return string


if __name__ == '__main__':
    for i in range(10):
        print random_generrater()