# Copyright 2017 Shuang Zhao zs1995@bu.edu
# Copyright 2017 Xintong Hao hxtong@bu.edu
# Copyright 2017 LijunXiao ljxiao@bu.edu
import sys
import itertools
wordlist = {}
dic1_all = {}
biglist = open(sys.argv[1]).read().split()
for line in biglist:
    letters = list(line)
    letters.sort()
    letterstr = str(letters)
    dic2_sub = dic1_all.setdefault(len(line), {letterstr: []})
    dic2_sub.setdefault(letterstr, []).append(line)
    l = len(line)
    di = {}
    for i in line:
        try:
            di[i] += 1
        except:
            di[i] = 1
    di['name'] = line
    try:
        wordlist[l].append(di)
    except:
        wordlist[l] = [di]
while True:
    inp = input()
    c, d = str.split(inp)
    d = int(d)
    if d == 0:
        break
    __out__ = []
    wordletters = list(c)
    wordletters.sort()
    wordletterstr = str(wordletters)
    if len(c) == d:
        __out__ = dic1_all.get(d, {}).get(wordletterstr, [])
    elif len(c) <= 10:
        worded = ''.join(wordletters)
        word = [''.join(x) for x in itertools.combinations(worded,d)]
        w = list(set(word))
        for i in w:
            ii = list(i)
            ii.sort()
            iii = str(ii)
            __out__ = dic1_all.get(d, {}).get(iii, []) + __out__           
    else:
        dic = {}
        for i in 'qwertyuiopasdfghjklzxcvbnm':
            dic[i] = 0
        for i in c:
            dic[i] += 1
        try:
            ll = len(wordlist[d])
            for i in range(ll):
                flag = 0
                for key in wordlist[d][i]:
                    if key != 'name':
                        if wordlist[d][i][key] > dic[key]:
                            flag = 1
                            break
                if flag == 0:
                    __out__.append(wordlist[d][i]["name"])
        except:
            pass
    __out__.sort()
    for i in __out__:
        print(i)
    print('.')
