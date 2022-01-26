# def commanPref():
#    array=["bhushan","agarwal","bhushan"] 
#    dict={}
#    count=0
#    for i in array:
#      key=i[0:2]
#     #  print(value)
#      if key in dict:
#          dict[key]=dict[key] +1
#      else:
#          dict[key]=1
#    maxval=0
#    maxkey=""
#    for key in dict:
#      print(key)
#      if dict[key]>maxval:
#         maxval=dict[key]
#         maxkey=key
#    print(dict[key]) 
#    print(maxkey)
         
         
#    print(dict) 
#     #  firstval=i[0]
#     #  secondval=i[1]
#     #  finalval=(firstval+secondval)
#     #  print(i[0:2])
#     #  if finalval==i[0:2] and finalval==finalval:
#     #     count+=1
#     #  else:
#     #      count=1
     
#     # #  dict[finalval]=count
#     #  dict.update({finalval:count})
#     #  if dict.values()>1:
#     #    print(dict.keys())
#     #  print(finalval)
#     #  print(dict)
    
#     #  for j in array:
#     #     if firstval==j[0]:
#     #         print("comman")
    
    
# commanPref()

# def compre():

#   comp=['bhus','agar','bhu','bhush']
#   dic={}
#   count=1
#   for cm in comp:
#     pre=cm[0:2]
    
#     if pre not in dic:
#       dic[pre]=count
#     else:
#       dic[pre]=dic[pre] +1
#   print(dic)
#   if max(dic) > 1:
#     print(max(dic), 'is command prefeix')

#   else:
#     print('no common prefex found ')
#     # print(pre)
#     # # for preval in pre:
#     # #   print(preval)
#     # if cm[0:2] == pre and count >=0:
#     #   count=count+1
#     #   print(count)
#     # # elif cm[0:2] == pre and  count >=1:
#     #   #  print('yes it is common pre')
#     # else: 
#     #   print('No it is not comm ')
  
# compre()


def listComAndGet():
  list =['hello','hell','man','mann','ag','bhu','bh2','bh8','man']
  count=1
  dict={}

  for commVal in list:
    preval=commVal[0:2]
    if preval not in dict:
      dict[preval]=count
    else:
      dict[preval]= dict[preval] +1
  print(dict)
  # my_dic={k:v for k,v in dict.items() if v>1}
  for k,v in dict.items():
    if v>1:
      print(k,":",v)
    else:
      print(k,' has not common prefix')
  # print(my_dic.values())
  # if my_dic.values() > 1:
  #   print(my_dic.keys(), 'IS Comman Prefex')
  # else:
  #   print('It is not comman')
listComAndGet()









