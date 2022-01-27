#hell
#o
# def mapnumstr():
#     mapp={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
#     input="23"
#     list=[]
#     in1=input[0]
#     in2=input[1]
#     print(in1,in2)
#     # for inp in mapp:
#         # print(mapp.keys())
#     print(mapp.keys())
#     if input[0] in mapp.keys():
#             print('match found')
#     else:
#             print('No Match')
#
#
# mapnumstr()
#
# def letterCombinations():
#     # List[str]:
#     digits="234"
#     kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
#               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
#     ans = ['']
#     for d in digits:
#         print(d)
#         ans = [x + y for x in ans for y in kvmaps[d]]
#         print(ans)
#
# letterCombinations()

def letterCombinations():
    # List[str]:
    digits="234"
    kvmaps = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
              '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    ans = ['']
    for d in digits:
         ans = [x + y for x in ans for y in kvmaps[d]]
    print(ans)

letterCombinations()


def strmapping():
    mapp={'1':'abc','2':'def','3':'ghi','4':'jkl','5':'mno','6':'pqr','7':'stu','8':'vwx','9':'yz'}
    inputdigit="98"
    lis=['']
    for inp in inputdigit:
        lis=[(li+mp) for li in lis for mp in mapp[inp]]
        # for li in lis:
        #  for mp in mapp[inp]:
        #     lis.append(li+mp)

    print(lis)
strmapping()











