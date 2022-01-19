from array import *

#WRITE txt files
task = '3.5.1.1.4.2/1.1.6.3.1.3.3/3.6.3.1.1.5/4.3.5.2.3/4.3.3.2.2/2.2.6/2.2.6.1/2.3.2.2/1.4.7.1.3/1.2.1.1/1.1.2.6.11/1.2.2.2.1.3/2.1.3.2.2.3.1/2.2.3.2.1/5.6.1.2.1/6.4.1.1.6.2/1.2.6.3.3/1.6.3.4/2.6.11/3.1.3.11/2.1.3.5.3/7.6.2.3/2.1.1.8.1/2.1.3.10.3/4.3.12/4.8.3.3/3.4.3.3/6.1.4.1.1/4.2.4/8.1/1.4.1.1.2.2/1.1.2.1.1.2/1.3.2.4/4.1/4.1.2.1/3.1.3/3.3.5.2/3.2.6.7/2.1.5.9/1.1.1.11/9.1.3.4/8.3.4.4/7.1.3.1.1.3/2.1.4.3/1.4.1.1.1.1.4.2/4.1.1.1.5.2/1.1.1.1.7.2/2.3.3.3.1/3.3.1.3.3.1/2.1.2.2/1.1.1.4.1/1.4.1.5.1/3.3.3.7/5.1.2.5/5.10'
tasks = task.split('/')
print(len(tasks)/2)
file = open("data_row.txt", "w")
for i in range(0, 25):
    file.write(str(tasks[i]) + '\n')
file.close
file = open("data_col.txt", "w")
for i in range(25, len(tasks)):
    file.write(str(tasks[i]) + '\n')
file.close

#Setup
col = []
row = []

#READ data_col.txt
file = open("data_col.txt", "r")
strings = file.readlines()
file.close
for idx, line in enumerate(strings):
    data = line.split('.')
    col.append(data)
    print("Col[" + str(idx) + "] : " + line.rstrip("\n") + " \t (len : " + str(len(data)) + ")")

#READ data_row.txt
file = open("data_row.txt", "r")
strings = file.readlines()
file.close
for idx, line in enumerate(strings):
    data = line.split('.')
    row.append(data)
    print("Row[" + str(idx) + "] : " + line.rstrip("\n") + " \t (len : " + str(len(data)) + ")")


#SET TABLE
x = len(col)
y = len(row)

for i in range (0, x):
    col[i] = list(map(int, col[i]))

for i in range (0, y):
    row[i] = list(map(int, row[i]))

#DEFINE MATRIX
print(x, y)
MATRIX = [[0]*y for i in range(x)]

#PRINT MATRIX
def PrintMatrix(matrix):
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == 0: char = '· '
            elif matrix[i][j] == 1: char = '■ '
            else: char = '□ '
            print(char, end = '')
        print('')
    print('')

PrintMatrix(MATRIX[:])

#READ COLUM FROM MATRIX
def ReadCol(i):
    myList = []
    for myY in range(0,y):
        myList.append(MATRIX[i][myY])
    return myList

#WRITE COLUM ON MATRIX
def WriteCol(MyMatrix, i):
    if(len(MyMatrix) != y):
        print("ERR: LENGTH ERROR ON COL " + str(i))
        return
    for myY in range(0, y):
        MATRIX[i][myY] = MyMatrix[myY]

#READ ROW FROM MATRIX
def ReadRow(i):
    myList = []
    for myX in range(0,x):
        myList.append(MATRIX[myX][i])
    return myList

#WRITE ROW ON MATRIX
def WriteRow(MyMatrix, i):
    if(len(MyMatrix) != x):
        print("ERR: LENGTH ERROR ON ROW " + str(i))
        return
    for myX in range(0, x):
        MATRIX[myX][i] = MyMatrix[myX]

#MUST FILL
def MUSTFILL(matrix, rule):
    def PrintMatrix(matrix):
        for i in range(0, len(matrix)):
            if matrix[i]==0: char = '-'
            elif matrix[i]==1: char = '■'
            else: char = '□'
            #print(char, end='')
        #print('')

    def BackEnd(checker):
        #print("checker : " + str(checker))
        def ReduceEmpty():
            if len(checker) >= 2:
                if checker[0] == 2 and checker[1] == 1:
                    del checker[0]
                    ReduceEmpty()
                    return
            for i in range (1, len(checker)):
                if checker[i-1] == 2 and checker[i] == 2:
                    del checker[i]
                    ReduceEmpty()
                    return

        def CheckN():
            for i in range(0, len(checker)):
                if i == len(checker)-1:
                    if not 2 in checker:
                        checks.append(i+1)
                        return
                if checker[i] == 2:
                    for j in range (0, i+1):
                        #print(checker)
                        #print(i, i+1)
                        del checker[0]
                    if i != 0: 
                        checks.append(i)
                        CheckN()
                        return

        checks = []
        ReduceEmpty()
        #print("Reduced : " + str(checker))
        CheckN()
        #print("CHECKS = " + str(checks))
        return checks

    def MustFill(MyMatrix, MyRule):
        defaultMatrix = MyMatrix[:]
        #Rule of Zero
        if len(MyRule) == 0:
            for i in range (0, len(MyMatrix)):
                if MyMatrix[i] == 0 : 
                    MyMatrix[i] = 2

        #Rule of Marking
        def CheckFresh(idx):
            #Not Solid
            for i in range (0, idx):
                if MyMatrix[i] == 0:
                    print("err: Not Solid")
                    return -1
            #Check N
            return BackEnd(MyMatrix[:idx])
        
        #SEND DATA
        def IfChanged(old, new):
            nonlocal fillOutput
            if(old != new): 
                PrintMatrix(new)
                fillOutput = new
                new = MustFill(new[:], rule)
            return new

        if 0 in MyMatrix:
            idx = MyMatrix.index(0)
            id = CheckFresh(idx)

            #COUNT LOGIC - FILL ZERO
            count = 0
            for i in range(0,len(MyRule)):
                count += int(MyRule[i])
            if(MyMatrix.count(1) == count):
                for i in range(0, len(MyMatrix)):
                    if MyMatrix[i] == 0: 
                        MyMatrix[i] = 2
                IfChanged(defaultMatrix, MyMatrix)

            #COUNT LOGIC - FILL ONE
            count = 0
            for i in range(0,len(MyRule)):
                count += int(MyRule[i])
            for i in range(0,len(MyMatrix)):
                if(MyMatrix[i] == 1):
                    count -= 1
            if(count == MyMatrix.count(0)):
                for i in range(0, len(MyMatrix)):
                    if MyMatrix[i] == 0: 
                        MyMatrix[i] = 1
                IfChanged(defaultMatrix, MyMatrix)

            if len(id) == 0: return MyMatrix

            #FILL LOGIC
            if len(MyRule) < len(id):
                #print("err: ID is bigger than the rule")
                return []
            if MyRule[len(id)-1] > id[len(id)-1]:
                for i in range(0, MyRule[len(id)-1] - id[len(id)-1]):
                    if idx+i > len(MyMatrix)-1:
                        #print("err: range err inside " + str(MyMatrix))
                        return []
                    if MyMatrix[idx + i] != 0:
                        #print("err: syntex err on " + str(idx + i) + " inside " + str(MyMatrix))
                        return []
                    MyMatrix[idx + i] = 1
                if(idx + MyRule[len(id)-1] - id[len(id)-1]) < len(MyMatrix) :
                    MyMatrix[idx + MyRule[len(id)-1] - id[len(id)-1]] = 2
                IfChanged(defaultMatrix, MyMatrix)

    fillOutput = matrix[:]
    PrintMatrix(matrix[:])
    #print(matrix, rule)
    MustFill(matrix[:], rule[:])
    return fillOutput

def DoMustFill():
    flag = True
    while(flag):
        flag = False
        for i in range(0, y):
            dataFrom = ReadRow(i)
            dataTo = MUSTFILL(ReadRow(i),row[i])
            if(dataFrom != dataTo):
               WriteRow(dataTo,i)
               flag = True
        for i in range(0, x):
            dataFrom = ReadCol(i)
            dataTo = MUSTFILL(ReadCol(i),col[i])
            if(dataFrom != dataTo):
               WriteCol(dataTo,i)
               flag = True

def ReturnGuess(matrix, rule):
    myOutput = []
    def Guess():
        if len(rule) == 0: return
        flag = True
        myMatrix = []
        for i in range(0, len(matrix)):
            myMatrix.append(0)

        def Fill(idx):
            nonlocal myOutput
            if not 0 in myMatrix: return
            begin = myMatrix.index(0)
            for i in range(begin, len(myMatrix)):
                flag = True
                for k in range(begin, i):
                    myMatrix[k] = 2
                for j in range(0, rule[idx]):
                    if i+j >= len(myMatrix): 
                        flag = False
                        continue
                    myMatrix[i+j] = 1
                    for l in range (i+j+1, len(myMatrix)):
                        myMatrix[l] = 0
                if(flag): 
                    if idx == len(rule)-1:
                        for k in range(i, len(myMatrix)):
                            if myMatrix[k] == 0: myMatrix[k] = 2
                        myOutput.append(myMatrix[:])
                    else:
                        if 0 in myMatrix: myMatrix[myMatrix.index(0)] = 2
                        Fill(idx+1)
        Fill(0)
    Guess()


    for i in range(len(myOutput)-1, -1, -1):
        for j in range(0, len(matrix)):
            if matrix[j] != 0:
                if myOutput[i][j] != matrix[j]:
                    myOutput.remove(myOutput[i])
                    break

    return myOutput

#FALSE CHECK : CHECK VALIDITY
def BackEnd(checker):
    #print("checker : " + str(checker))
    def ReduceEmpty():
        if len(checker) >= 2:
            if checker[0] == 2 and checker[1] == 1:
                del checker[0]
                ReduceEmpty()
                return
        for i in range (1, len(checker)):
            if checker[i-1] == 2 and checker[i] == 2:
                del checker[i]
                ReduceEmpty()
                return

    def CheckN():
        #print("CHECK CALLED")
        #print("CHECKER = " + str(checker))
        for i in range(0, len(checker)):
            #print("i = " + str(i) + " checker[i] = " + str(checker[i]))
            if i == len(checker)-1:
                if not 2 in checker:
                    checks.append(i+1)
                    return
            if checker[i] == 2:
                #print("GET" + str(i))
                for j in range (0, i+1):
                    #print(checker)
                    #print(i, i+1)
                    del checker[0]
                if i != 0: 
                    checks.append(i)
                    CheckN()
                    return

    checks = []
    ReduceEmpty()
    #print("Reduced : " + str(checker))
    CheckN()
    #print("CHECKS = " + str(checks))
    return checks

def FalseCheck(MyMatrix, MyRule):
    #Contents Match Check
    if not 0 in MyMatrix:
        if BackEnd(MyMatrix[:]) != MyRule:
            #print("CONTENTS DONT MATCH")
            #print(BackEnd(MyMatrix[:]), MyRule)
            return False

    #Sum, Count Check
    count = 0
    for i in range(0,len(MyRule)):
        count += int(MyRule[i])
    if(MyMatrix.count(1) > count):
        #print("OVER COUNT")
        return False

    #Max Number Check
    count = 0
    maxCount = 0
    for i in range(0, len(MyMatrix)):
        if(MyMatrix[i] == 1):
            count += 1
        else:
            if count > maxCount:
                maxCount = count
            count = 0
    if maxCount > max(MyRule):
        #print("MAX DON'T MATCH : MAX = " + str(max(MyRule)) + " MaxCount = " + str(maxCount))
        return False
    return True

def DoFalseCheck():
    for x in range(0, len(col)):
        if FalseCheck(ReadCol(x), col[x]) == False:
            return False
    for y in range(0, len(row)):
        if FalseCheck(ReadRow(y), row[y]) == False:
            return False
    return True

#BRUTE FORCE EACH LINE
def GueseCols(colIdx):
    #print(colIdx)
    if colIdx == len(col):
        print("FINISHED")
        PrintMatrix(MATRIX[:])
        return -1

    if not 0 in ReadCol(colIdx):
        if GueseCols(colIdx+1) == -1:
                return -1

    guess = ReturnGuess(ReadCol(colIdx), col[colIdx])
    if guess == []:
        #print("NULL ERROR")
        return -2
    
    savedData = []
    for i in range(0, len(col)):
        savedData.append(ReadCol(i))

    for i in range(len(guess)-1, -1, -1):
        #print(len(guess)-i, '/', len(guess))
        for j in range(0, len(col)):
                WriteCol(savedData[j], j)
        WriteCol(guess[i], colIdx)
        DoMustFill()
        FC = DoFalseCheck()
        if FC == True:
            PrintMatrix(MATRIX[:])
            #Go to next line
            if GueseCols(colIdx+1) == -1:
                return -1

GueseCols(0)