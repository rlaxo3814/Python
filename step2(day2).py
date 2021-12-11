def testFile():
    file = open('./data/Abc1115.csv','r')
    lines = file.readlines()
    file.close()

    mlist = []
    length = len(lines)
    print(length)
    # line을 리스트에 넣은 후 리스트를 출력하시오
    for line in lines:
        mlist.append(line);
        print(line)
    print(mlist)
    pass

def testSlice():
    file = open('./data/Abc1115.csv', 'r')
    lines = file.readlines()
    file.close()
    print(lines[:1])
    temp = []
    for line in lines[:5]:
        #temp.append(line[:len(line) - 1])
        temp.append(line[:-1])
        #print(len(line))
        pass
    print(temp)
    for item in temp:
        print(item)
    pass

#파일의 한줄을 ,로 분리하여 리스트로 만들고 해당 리스트를
#다시 리스트에 element로 저장하여 출력하는 코드 작성
def testSplit():
    file = open('./data/Abc1115.csv', 'r')
    lines = file.readlines()
    file.close()
    mlist = []
    for line in lines:
        temp = line[:-1].split(',')
        mlist.append(temp)
        pass

    print(mlist[:5][1])
    #1~5까지의 email을 출력하시오
    for item in mlist[:5]:
        print(item[1])
        pass

    pass

def testFor():
    numbers = '12345'
    index = 0
    for idx in range(len(numbers)):
        print(numbers[idx])
        #index = index + 1
        pass

    for idx, val in enumerate(numbers):
        print("{0} : {1}".format(idx,val))
    pass