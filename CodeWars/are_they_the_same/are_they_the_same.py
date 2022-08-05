def comp(array1, array2):

    if not isinstance(array1,list):
        
        return False
    elif not isinstance(array2,list):
        
        return False
    # your code
    # array2 = list(array2)
    test_list = []
    for idx,number in enumerate(array1):
        if idx == 0:

            test_list.append((number))
        else:
            test_list.append(array1[idx-1]*array1[idx-1])
    test_list.sort()
    array2.sort()

    if test_list == array2:
        return True
    else:
        return False

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

comp(a1,a2)
    
    

