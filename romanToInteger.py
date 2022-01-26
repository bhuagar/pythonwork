def romanToInt(s):
  Map = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  # s = list(s)
  # print(len(s)-1)
  number = 0
  digit = 0
  for i in range(len(s)-1,-1,-1):
  # for i in len(s)-1:
    print(i)
    if int(Map[s[i]]) >= int(digit):
      number += int(Map[s[i]])
      print(number)
    else:
        number -= int(Map[s[i]])
        print(number)
    digit = int(Map[s[i]])
    print(digit)
  return number
  
romanToInt(s="IV")
# def romanToInt():
#   dic = {"I":1, "V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
#         dic2= {"IV":-2, "IX":-2, "XL":-20, "XC":-20, "CD":-200, "CM":-200}
#         ans = 0 
#         for i in range(len(s)):
# 	        ans += dic[s[i]]
#         for i in range(len(s)-1):
# 	        temp = s[i:i+2]
# 	        if temp in dic2:
# 		        ans += dic2[temp]
#         return (ans)
# romanToInt()
#   # val=input("Please Eneter Roman Number::" )
#   # if val=="I":
#   #   print(1)
#   # elif val=="v":
#   #   print(5)
#   # elif val=="X":
#   #   print(10)
#   # elif val=="L":
#   #   print(50)
#   # elif val=="C":
#   #   print(100)
#   # elif val=="D":
#   #   print(500)
#   # elif val=="M":
#   #   print(1000)
#   # else:
#   #   print("All good")
# romanToInt()
