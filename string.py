import re
# # bhushan="thisisbhushan agarwal"
# # print(bhushan[3:10:3])
# # print(bhushan[::-1])
def regularExp():
  out=""
  str="Thisis bhushan and working on regx https://"
  out=re.findall("^\w+",str)
  space=re.findall("\s",str)
  rang=re.findall("[]",str)
  print(rang)
  print(out)
  print(space)
  print("bhushan")
regularExp()
  
# import re
# def regularExp():
#   xx = "guru99,education is fun"
#   r1 = re.findall(r"^\w+",xx)
#   print(r1)
# regularExp()
