def matchrule():
    inp=[["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","glb"]]
    ruleKey = "type"
    ruleValue = "phone"
    dict={}
    count=0
    for i in inp:
        for va in i:
            if va=='phone':

                # dict=dict+1
            # if ruleValue in va:
                count+=1
                dict[ruleKey] = count

    print(count)
    print(dict)
matchrule()