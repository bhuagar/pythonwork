import re
def regexp():
  list=["bhushan bhu","bhsuahn boh","python py","piy py"]
  for val in list:
    #   str=re.match("b\w+ m\w+ p\w+",val)
      str=re.match("(b\w+)\W(b\w+)",val)
      if str:
            print((str.groups()))
      else:     
          str2=re.match("(p\w+)\W(p\w+)",val)
          if str2:
                 print((str2.groups()))  
regexp()         

def search():
  list=["Hello this","Is Bhushan","Agrawal"]
  text="Is Bhushan"     
  for ser in list:
      str=re.search(ser,text)
      if str:
         print("match found")
      else:
          print("not Found")
search()      

def findval():
  email='guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com,adlasdasd,adsadsad'
  emails = re.findall(r'[\w\.]+@[\w\.]+', email)
  for val in emails:
      if val:
        print(val)
      else:
          print("no email")
findval()
  
def isPalindrome():
  x="1221"
  str=x[::-1]
  if str==x:
    print("string Palindrom")
  else:
    print("No Palindrom")
            
isPalindrome()

def romanToInt()
  in=input("Please Eneter Roman Number::" )
  if in=="I":
    print(1)
  else if:
    in=="v"
    print(5)
romanToInt()



