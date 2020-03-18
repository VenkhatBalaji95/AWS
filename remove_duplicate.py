def lambda_handler(event, context):
    print ('into the function')
    lis = [['venkhat',24],['Balaji',24],['venkhat',21],['Balaji',13],['venkhat balaji',24],['venkhat balaji', 22]]
    another_lis = []
    another_lis.append(lis[0])
    for i in lis:
        j = 0
        k = 0
        while j < len(another_lis):
            if i[0] == another_lis[j][0]:
                k = 1
            j = j+1
        if k == 0:
            another_lis.append([i[0],i[1]])
    for i in another_lis:
        print (i[0],i[1])