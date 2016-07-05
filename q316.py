def removeDuplicateLetters(s):
    s1=set(s)
    s2=list(s1)
    s2.sort()
    s=''.join(s2)
    return s
