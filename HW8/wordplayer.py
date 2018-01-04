# Copyright 2017 Shuang Zhao zs1995@bu.edu
# Copyright 2017 Xintong Hao hxtong@bu.edu
# Copyright 2017 LijunXiao ljxiao@bu.edu
import sys
wordlist = {}
list_len = 0
biglist = open(sys.argv[1]).read().split()
for line in biglist:
    line = line.strip('\n')
    l = len(line)
    di = {}
    for i in range(l):
        try:
            di[line[i]] += 1
        except KeyError:
            di[line[i]] = 1
    di['name'] = line
    try:
        wordlist[l].append(di)
    except KeyError:
        wordlist[l] = [di]
    list_len += 1
while True:
    inp = input()
    x = str.split(inp)
    c = x[0]
    len_c = len(c)
    d = int(x[1])
    if d == 0:
        break
    dic = {}
    __letter__ = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(26):
        dic[__letter__[i]] = 0
    for i in range(len_c):
        dic[c[i]] += 1
    __out__ = []
    __num__ = 0
    try:
        for i in range(len(wordlist[d])):
            flag = 0
            for key in wordlist[d][i]:
                if key == 'name':
                    continue
                else:
                    if wordlist[d][i][key] > dic[key]:
                        flag = 1
                        break
            if flag == 0:
                __out__.append(wordlist[d][i]["name"])
                __num__ += 1
        __out__.sort()
        for i in range(__num__):
            print(__out__[i])
        print('.')
    except KeyError:
        print('.')
