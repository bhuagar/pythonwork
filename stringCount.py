def stringcount():
    strval="AAAAAAABBBBBBBBCCCCCCCCDDDDDDDDDEEEEEEE"
    dict={}
    count=1
    for inval in strval:
         if inval not in dict:
             dict[inval]=count
         else:
          dict[inval]=dict[inval]+1
    maxval=max(dict.values())
    print(maxval)
    # sortvalue=sorted(dict.items())
    # print(sortvalue)
    # print(sortvalue[-2])
stringcount()
