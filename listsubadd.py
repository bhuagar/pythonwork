def listsubadd():
    dict={"--x":-1,"x++":1,"++x":1,"--x":1}
    # finallis=[sum(li) for li in lis if li=="--x" li=-1 elif li=='x++' li=1]
    x=0
    y=0
    for di in dict:
        print (di)
        if di in dict :
         x+=dict[di]
         print(x)
        else:
            print("Noting to do")
        # elif di=="x++" or di=="++x":
        #     x+=dict[di]
        #     print(x)


    # for li in lis:
    #     if li =="--x":
    #         li=-1
    #
    #     elif li=="x++":
    #         li=1
    #     finalval=sum(li)
    #
    # print(finalval)
listsubadd()
