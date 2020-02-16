#Task 1
def task1():
    n = int(input("Insert n:\n"))
    e = n
    for i in range(1,n+1):
        for j in range(1,i+1):
            if e == 0:
                break
            e-=1
            print(i,end = " ")
#Task 2
def task2():
    s = input("Input lst:\n")
    x = int(input("Input x:\n"))
    lst = s.split(" ")
    res = []
    for i,item in enumerate(lst):
        if item == str(x):
            res.append(i)
    if len(res) == 0:
        print("Отсутствует")
    else:
        for i in res:
            print(i,end=" ")
#Task 3
def task3():
    strItem = input("Input string:\n")
    strMatrix = []
    while strItem!="end":
        strMatrix.append(strItem)
        strItem = input("Input string:\n")
    intMatrix = []
    result = []
    for i in strMatrix:
        intMatrix.append(i.split(" "))
    for i in range(len(intMatrix)):
        result.append([])
        for j in range(len(intMatrix[0])):
            a = intMatrix[i-1][j] if i != 0 else intMatrix[len(intMatrix)-1][j]
            b = intMatrix[i+1][j] if i != len(intMatrix)-1 else intMatrix[0][j]
            c = intMatrix[i][j-1] if j != 0 else intMatrix[i][len(intMatrix[0])-1]
            d = intMatrix[i][j+1] if j != len(intMatrix[0])-1 else intMatrix[i][0]
            result[i].append(int(a)+int(b)+int(c)+int(d))
    for i in result:
        for j in i:
            print(j,end=" ")
        print()
#Task 4
def task4():
    n = int(input("Input n:\n"))
    m,d = n,n
    lst = []
    for q in range(n):
        lst.append([])
        for s in range(n):
            lst[q].append(0)
    i,j,k = 0,0,0
    incJ = True
    incI = True
    startI,startJ = -1,-1
    while k <d**2:
        while j < m and j > startJ:
            lst[i][j] = k+1
            k+=1
            if incJ:
                j+=1
            else:
                j-=1
        else:
            if incJ:
                startI+=1
                j-=1
            else:
                startJ+=1
                j+=1
            incJ=not incJ
            if incI:
                i+=1
            else:
                i-=1
        while i < n and i > startI:
            lst[i][j] = k+1
            k+=1
            if incI:
                i+=1
            else:
                i-=1
        else:
            if incI:
                n-=1
                i-=1
            else:
                m-=1
                i+=1
            incI=not incI
            if incJ:
                j+=1
            else:
                j-=1
    for q in lst:
        for s in q:
            print("{0:3d}".format(s),end=" ")
        print()
task4()