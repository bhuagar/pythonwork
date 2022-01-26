def lisPrac():
    list=['bhu','aga','zzz','nam','hello','busy']
    list2=['new','old']
    list.extend(list2)

    listVal=sorted(list)
    listVal.insert(0,'Apple')
    listVal.reverse()
    listVal.pop()
    listVal.remove('aga')
    print(listVal)

    # list.sort(reverse=True)
    # print(listsortVal)
    # for val in listVal :
    #     finalList=list.extend(list2) 
    #     print(finalList) 
    # indexval=list.index('bhu')
    # print(indexval)
lisPrac()
