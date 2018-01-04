'''
Code for EC602 assignment10
'''
# Copyright 2017 ShuangZhao zs1995@bu.edu
# Copyright 2017 XintongHao hxtong@bu.edu
# Copyright 2017 LijunXiao ljxiao@bu.edu
from sys import argv


__small_list__ = open(argv[1], 'rt').read().split()
__large_list__ = open(argv[2], 'rt').read().split()


def change(matrix, positionlist):
    '''change the matrix'''
    nmatrix = dict(matrix)
    if positionlist == []:
        return nmatrix
    for pos in positionlist:
        del nmatrix[pos]
    while True:
        flag1 = True
        nmatrix_copy = dict(nmatrix)
        for pos in nmatrix:
            if pos[0] + 1 in range(__dim__) and \
               (pos[0] + 1, pos[1]) not in nmatrix.keys():
                flag1 = False
                nmatrix_copy[(pos[0] + 1, pos[1])] \
                    = nmatrix_copy[(pos)]
                del nmatrix_copy[pos]
        if flag1:
            return nmatrix_copy
        else:
            nmatrix = nmatrix_copy


def match(__m__, star):
    '''match the letters by hints'''
    if star == '*' * len(star):
        return True
    else:
        for i, char in enumerate(__m__):
            if star[i] != '*' and char != star[i]:
                return False
    return True


def trans(lis):
    '''transfer list to dictionary'''
    __md__ = {}
    for __i__, line in enumerate(lis):
        for __j__, char in enumerate(line):
            __md__[(__i__, __j__)] = char
    return __md__


class Brain:
    '''the matrix'''
    def __init__(self):
        self.matrix = trans(__clist__)
        self.wordfoundlist = []
        self.result = [("", self.matrix)]
        self.dict = {}
        self.check = {}
        self.condition = 'easy'
        self.thislength = 0

    def findaword(self, matrix, startpoint, wordpiece, wordposition):
        '''find one word'''
        xpos, ypos = startpoint
        wordpiece = wordpiece + matrix[(xpos, ypos)]
        localposlist = list(wordposition)
        localposlist.append((xpos, ypos))
        if wordpiece not in self.check[len(wordpiece)]:
            return 0
        for ipos, jpos in [(xpos - 1, ypos - 1), (xpos - 1, ypos),
                           (xpos, ypos - 1), (xpos + 1, ypos - 1),
                           (xpos - 1, ypos + 1), (xpos + 1, ypos),
                           (xpos, ypos + 1), (xpos + 1, ypos + 1)]:
            if (ipos, jpos) not in wordposition \
                    and (ipos, jpos) in matrix.keys():
                if len(wordpiece) + 1 == self.thislength:
                    newword = wordpiece + matrix[(ipos, jpos)]
                    if newword in self.dict:
                        self.wordfoundlist.append([newword] +
                                                  localposlist +
                                                  [(ipos, jpos)])
                    else:
                        pass
                else:
                    self.findaword(matrix, (ipos, jpos), wordpiece,
                                   localposlist)

    def findwords(self):
        '''find all posible solustions to the puzzle '''
        for i, length in enumerate(__llist__):
            self.thislength = length
            if self.condition == 'easy':
                __small_word__.setdefault(length, set())
                self.dict = __small_word__[length]
                self.check = __small_check__
            else:
                __large_word__.setdefault(length, set())
                self.dict = __large_word__[length]
                self.check = __large_check__
            formerresult = list(self.result)
            self.result = []
            for __ii__ in formerresult:
                formerword, newmatrix = __ii__
                self.wordfoundlist = []
                for startpoint in newmatrix:
                    self.findaword(newmatrix, startpoint, "", [])
                for __jj__ in self.wordfoundlist:
                    newword = __jj__[0]
                    newpositions = __jj__[1:]
                    if not match(newword, __plist__[i]):
                        continue
                    self.result.append((formerword + ' ' + newword,
                                        change(newmatrix, newpositions)))
            if self.result == []:
                if self.condition == 'easy':
                    self.condition = 'hard'
                    self.result = [("", self.matrix)]
                    self.findwords()
                    break
                else:
                    break

__small_word__ = {}
__large_word__ = {}
__small_check__ = {}
__large_check__ = {}
for word in __small_list__:
    __small_word__.setdefault(len(word), set())
    __small_word__[len(word)].add(word)
    for j, __ in enumerate(word):
        __small_check__.setdefault(j, set())
        __small_check__[j].add(word[:j])


for word in __large_list__:
    __large_word__.setdefault(len(word), set())
    __large_word__[len(word)].add(word)
    for k, __ in enumerate(word):
        __large_check__.setdefault(k, set())
        __large_check__[k].add(word[:k])

__clist__ = []
__llist__ = []
__inp__ = ""
while True:
    try:
        __inp__ = input()
    except EOFError:
        exit(0)
    if __inp__ == '':
        break
    if '*' in __inp__:
        __llist__ = []
        __plist__ = []
        __dim__ = len(__clist__)
        for __o__ in __inp__.split():
            __llist__.append(len(__o__))
            __plist__.append(__o__)
        __kk__ = Brain()
        __kk__.findwords()
        __out__ = sorted(set([__[0] for __ in __kk__.result]))
        for l in __out__:
            print(l)
        print('.')
        __clist__ = []
        __llist__ = []
    else:
        __clist__.append(list(__inp__))
