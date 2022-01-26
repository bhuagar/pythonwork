def findstrrepl():
    ipadd="1.2.3.4.5.6.7.8.9"
    finalstr=""
    lis=[]
    for fi in ipadd:
        if fi==".":
            fi="[.]"
        lis.append(fi)
    print(lis)
findstrrepl()

