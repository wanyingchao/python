data = 'JZCB061904001769,'\
'JZCB061904001192,'\
'JZCB061906001579,'\
'JZCB061906002283,'\
'JZCB061906001069,'\
'JZCB061904000647,'\
'JZCB061904000627'


n = data.split(',')
with open('E://python/pop/1246.txt', 'w') as file:
    for x in range(len(n)):
        if n[x][4] == '0':
            for i in range(1, 7):
                d = n[x] + ',' + str(i)
                file.write(d + '\n')
        else:
            for i in range(1, 13):
                d = n[x] + ',' + str(i)
                file.write(d + '\n')





