'''
docstring
'''
# Copyright 2017 ShuangZhao zs1995@bu.edu
# Copyright 2017 XintongHao hxtong@bu.edu
# Copyright 2017 LijunXiao ljxiao@bu.edu
import sys
from os import listdir
import re
import hashlib
import numpy as np
from skimage.io import imread
__dic__ = {}
__out__ = []
k = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
__pics__ = listdir()
for f in __pics__:
    if f[-4:] == '.png':
        image = 1 - imread(f, as_grey=True)
        x = np.nonzero(image)
        image = image[min(x[0]):max(x[0]) + 1, min(x[1]):max(x[1]) + 1]
        trans = []
        for i in range(4):
            trans.append(hashlib.sha256(
                bytes(image[::k[i][0], ::k[i][1]])).hexdigest())
            trans.append(hashlib.sha256(
                bytes(np.transpose(image[::k[i][0], ::k[i][1]]))).hexdigest())
        KEY = frozenset(trans)
        if KEY in __dic__:
            __dic__[KEY].append(f)
        else:
            __dic__[KEY] = [f]
for i in __dic__:
    __out__.append(__dic__[i])
for i in __out__:
    i.sort(key=lambda x: int(re.match(r'(\D+)(\d+)\.png', x).group(2)))
__out__.sort(key=lambda x: int(re.match(r'(\D+)(\d+)\.png', x[0]).group(2)))
__a__ = ''
__l__ = len(__out__)
for i in range(__l__):
    __a__ = __a__ + ' '.join(__out__[i]) + '\n'
__file__ = open(sys.argv[1], 'w')
__file__.write(__a__)
print(hashlib.sha256(bytes(__a__.encode('utf-8'))).hexdigest())
