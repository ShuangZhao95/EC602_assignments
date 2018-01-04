#!/bin/bash
g++ fourargs.cpp -o fourargs

python fourargs.py one two 3 four five six

python fourargs.py one two 3

fourargs one two 3 four five six

fourargs one two 3

# Copyright year ShuangZhao zs1995@bu.edu