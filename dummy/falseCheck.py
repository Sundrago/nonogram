rule = [3,3]
matrix = [2,1,1,1,2,1,1,1,2,2,2,0]

def PrintMatrix(matrix):
    for i in range(0, len(matrix)):
        if matrix[i]==0: char = '-'
        elif matrix[i]==1: char = '■'
        else: char = '□'
        print(char, end='')
    print('')


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
            print("CONTENTS DONT MATCH")
            print(BackEnd(MyMatrix[:]), MyRule)
            return False
        else: return True

    #Sum, Count Check
    count = 0
    for i in range(0,len(MyRule)):
        count += int(MyRule[i])
    if(MyMatrix.count(1) > count):
        print("OVER COUNT")
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
        print("MAX DON'T MATCH : MAX = " + str(max(MyRule)) + " MaxCount = " + str(maxCount))
        return False
    return True

PrintMatrix(matrix)
print(FalseCheck(matrix[:], rule[:]))