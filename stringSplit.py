# def stringsplit():
#     inpStr="RLRRLLRLRLRRRLLL"
#     fnlSt1=''
#     fnlStr2=''
#     lis=[]
#     for st in range(0,len(inpStr)):
#         print(st)
#         if inpStr[st]=='R' and inpStr[st+1]=='L':
#             fnlSt1+=inpStr[st]
#             print(fnlSt1)
#             # lis=lis.append(inpStr[st])
#             # fnlSt1+=inpStr[st]+ inpStr[st+1]
#         # elif inpStr.isalpha():
#         #     fnlSt1+=inpStr[st]
#
#                 # lis =lis.append(inpStr[st])
#             # fnlStr2+= inpStr[st]
#     print(fnlSt1.split())
#     # print(fnlStr2)
# stringsplit()

def diffval():
    res=0
    cnt=0

    inst = "RLRRLLRLRL"
    for st in inst:
        print(st)
        if st =='R':
            res +=1
            print(res)
        else:
            res -=1

        if (res==0):
            cnt +=1
    # return res
    print(res)
    print(cnt)
diffval()


