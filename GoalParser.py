# def Parser():
#     str="G()(al)"
#     ls=[]
#     # str2="al"
#     # stringval=str2.isalpha()
#     # print(stringval)
#     stack=''
#     for st in range(0, len(str)):
#         print(st)
#         if str[st] == '(' and str[st+1] == ')':
#             strfinalval='o'
#             ls.append(strfinalval)
#             st=st+1
#         elif str[st].isalpha():
#             ls.append(str[st])
#     print(''.join(ls))
#             # #     if st =="(" or st==")":
#     # #         st="o"
#     # #     li.append(st)
#     # print(li)
# Parser()

def parse():
    stval="b()hu(shan)()()"
    list=[]
    finalStr=''
    for i in range(0 , len(stval)):
        # print(i)
        if stval[i] =='(' and stval[i+1] ==')':
            strrepval='o'
            finalStr+=strrepval
            # list.append(strrepval)
            i=i+1
        elif stval[i].isalpha():
            finalStr+=stval[i]
            # list.append(stval[i])
    # print(''.join(list))
    print(finalStr)
parse()

