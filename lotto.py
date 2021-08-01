import random 

with open("lotto.txt") as f:
    t = f.read()

#def make_whole_number():
#    for i in range(45):   

def make_1000_count():
    ret = list()
    for i in range(100000):
        ret.append(rand_lotto())
    return ret
        

def rand_lotto():
    ret = set()
    while True:
        ret.add(random.randrange(1, 46))
        if len(ret) == 6:
            break
    ret = list(ret)
    ret.sort()
    return ret


def analysis_test_0(lotto):
    t1 = lotto[0]
    t2 = lotto[1]
    t3 = lotto[2]
    t4 = lotto[3]
    t5 = lotto[4]
    t6 = lotto[5]
    l1 = {t1, t1+1, t1+2}
    l2 = {t2, t2+1, t2+2}
    l3 = {t3, t3+1, t3+2}
    l4 = {t4, t4+1, t4+2}
    l5 = {t5, t5+1, t5+2}
    l6 = {t6, t6+1, t6+2}

    '''
    l1 = {t1, t1+1}
    l2 = {t2, t2+1}
    l3 = {t3, t3+1}
    l4 = {t4, t4+1}
    l5 = {t5, t5+1}
    l6 = {t6, t6+1}
    '''
    if l1.issubset(set(lotto)) or  l2.issubset(set(lotto)) or  l3.issubset(set(lotto)) or  l4.issubset(set(lotto)) or  l5.issubset(set(lotto)) or  l6.issubset(set(lotto)):
        return False
    else:
        return True

def analysis_test_1(lotto):
    if int(lotto[0]) > 30:
        return False
    elif int(lotto[-1]) < 15:
        return False
    else:
        return True

def analysis_test_2(lotto):
    ev_c = 0
    od_c = 0
    for lo in lotto:
        if int(lo) % 2 == 0:
            ev_c += 1
        else:
            od_c += 1

    if ev_c == 6 or od_c == 6:
        return False
    else:
        return True


def analysis_test_3(lotto):
    zero = 0
    ten = 0
    twe = 0
    thr = 0
    four = 0

    for lo in lotto:
        if int(lo) / 10 == 0:  
            zero += 1
        elif int(lo) / 10 == 1:  
            ten += 1
        elif int(lo) / 10 == 2:  
            twe += 1
        elif int(lo) / 10 == 3:  
            thr += 1
        elif int(lo) / 10 == 4:  
            four += 1

    if zero == 6 or ten == 6 or twe == 6 or thr == 6 or four == 6:
        return False
    else:
        return True



if __name__ == "__main__":
 
    temp = make_1000_count()
    ret_list = list()
    for lonum in temp:
        if analysis_test_0(lonum):
            pass
        else:
            continue
        if analysis_test_1(lonum):
            pass
        else:
            continue
        if analysis_test_2(lonum):
            pass
        else:
            continue
        if analysis_test_3(lonum):
            pass
        else:
            continue

        ret_list.append(lonum)

    print len(ret_list)
    print ret_list[:10]



