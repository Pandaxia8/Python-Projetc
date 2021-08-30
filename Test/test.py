def getDataMode1():
    file = open('test.txt', 'r')
    contents = file.read()
    # print((contents))
    contets_list = contents.split()
    grade1 = []
    grade2 = []
    # print(contets_list)
    for i in range(len(contets_list)):
        if i % 2 == 0:
            grade1.append(int(contets_list[i]))
        else:
            grade2.append(float(contets_list[i]))
    print('录取人数：   ', len(grade1))
    print('初试平均分： ', sum(grade1) / len(grade1))
    print('录取最低分： ', min(grade1))
    print('录取最高分： ', max(grade1))
    print('复试平均分： ', sum(grade2) / len(grade2))

def getDataMode2():
    grade1 = []
    grade2 = []
    file = open('type2.txt','r',encoding='utf-8')
    # print(file.read())
    contents = file.read()
    contets_list = contents.split('\n')
    print(contets_list)
    for i in range(3,len(contets_list),5):
        print(contets_list[i])
        grade1.append(int(contets_list[i]))

    # for i in range(len(contets_list)):
    #     print(contets_list[i].replace('\t',' ').split(' '))
    # for i in range(0,len(contets_list),1):
    #     try:
    #         grade1.append((int(contets_list[i].replace('\t',' ').split(' ')[1])))
    #         grade2.append((float(contets_list[i].replace('\t', ' ').split(' ')[2])))
    #     except:
    #         print()
        # grade1.append(int(contets_list[i].split()[7]))
        # grade2.append(float(contets_list[i].split()[8]))

    print('录取人数：   ', len(grade1))
    print('初试平均分： ', sum(grade1) / len(grade1))
    print('录取最低分： ', min(grade1))
    print('录取最高分： ', max(grade1))
# getDataMode1()
getDataMode2()
