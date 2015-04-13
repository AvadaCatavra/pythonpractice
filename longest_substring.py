#!/usr/local/bin/python3

def longest_substring(mystring):
    #naive way: split into substrings

    substrings = [] 
    prev = -1
    for i in mystring:
        if i == prev:
            substrings[-1]+=i       #append it to the last substring
        else:
            substrings.append(i)              #otherwise you're at a new substring
        prev = i

    #now get longest substring
    lens = []
    for i in substrings:
        lens.append(len(i))
    print(substrings, lens)

    return substrings[max(lens)]


def __main__():
    print("Goal: find the longest string of repeated chars in a string")


    print(longest_substring("aaaaaabbccdddeefgh"))
    print(longest_substring("blahblahbbb"))

__main__()
