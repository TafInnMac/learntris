#!/usr/bin/env python
command = raw_input()

if command == 'p':
    for column in range(22):
        for row in range(10):
            print("."),
        print
