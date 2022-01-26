def shuffleString():
    dict={}
    s="abc"
    indices=[0,1,2]
    for ind in indices:
         # for si in s:
         # indsort=ind.sort()
         dict[ind]=s[ind]
    print(dict.values())
shuffleString()