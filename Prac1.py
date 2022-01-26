def dictPrac():
  dict={1:2}
  initialkey=1
  MaxVal=100
#   for i in range(1, 101):
  for i in dict:
    # print("the key name is" + i + "and its value is" + dict[i])
    # print(i)
    for i in range(1,101):
     if i <= MaxVal:
    #   key=i+1
    #   print(key)
      dict[i]=i*i
  
  print(dict) 

    # if i[initialkey] in dict:
    #     dict[key]=dict[key]+1
    #     print(dict[initialkey])
    # else:
    #     dict[key]=initialkey +1 
    #     print(dict[key])
    #   if i
    
    #   if dict[key] in key:
    #     dict[key]=dict[key] +1
    #   else:
    #     dict[key]=1
#   print(dict[key])
dictPrac()