def listComp():
    num= [1,2,3,5,6]
    newlist=[xi*xi for xi in num  if xi%3 == 0 ]
    # for xi in num:
    #     newlist.append(xi)
    print(newlist)
    # for xi in num:
        # print(xi) 


listComp()

def innerloop():
    newlist=[]
    str='bhushan'
    # for st in str:
    #     for ft in range(3):
    #         newlist.append((st,ft))
     

    newlist=[(st,ft) for st in str for ft in range(5)]    
    print(newlist)

innerloop()

def zipMeth():
    key=['hello','how','I','Glad']
    val=['hi','are you','am fine','That you are fine']
    dict={ky:va for ky,va in zip(key,val) if ky=='hello'}
    # for ky,va in zip (key,val):
    #     print(ky,va)
    print(dict)
    
zipMeth()



