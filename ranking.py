#!/usr/local/bin/python3

#
# Given a list of scores, return the array of ranks of each value
#   largest = 1...
#   ties all get the same rank
#

def ranks(scores):


    ranklist=[]
    ranksout=[]

    #first, dedup and sort all scores, then go through and assign ranks based on that
    #is there a way to only go through the list once?

    from collections import OrderedDict
    ranklist = list(OrderedDict.fromkeys(scores.sort(reverse=True)))

    print('deduped:', ranklist)

    for i in scores:
        ranksout = ranklist.index(i)


def __main__():
    print(ranks([9,3,6,10]))
    print(ranks([3,3,3,5,3,1]))

#Nope did it wrong, because you don't have 1,2, 3 place then, you have 1,2,6


__main__()



