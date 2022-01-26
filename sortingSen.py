def sortingSen():
    inpst="is2 sentence4 This1 a3"
    s = inpst.split()
    print(s)
    res = []
    count = 1
    while len(s) > 0:
        for i in s:
            if int(i[-1]) == count:
                res.append(i[:-1])
                count += 1
                s.remove(i)

    print(" ".join(res))

sortingSen()