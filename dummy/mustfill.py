rule = [3,3,2]
matrix = [2,1,0,0,2,2,1,0,0,2,2,2,2,0,0,2]

def MUSTFILL(matrix, rule):
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
            if(old != new): 
                PrintMatrix(new)
                nonlocal output
                output = new
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
            if MyRule[len(id)-1] > id[len(id)-1]:
                for i in range(0, MyRule[len(id)-1] - id[len(id)-1]):
                    if idx+i > len(MyMatrix)-1:
                        print("err: range err inside " + str(MyMatrix))
                        return -1
                    if MyMatrix[idx + i] != 0:
                        #print("err: syntex err on " + str(idx + i) + " inside " + str(MyMatrix))
                        return -1
                    MyMatrix[idx + i] = 1
                if(idx + MyRule[len(id)-1] - id[len(id)-1]) < len(MyMatrix) :
                    MyMatrix[idx + MyRule[len(id)-1] - id[len(id)-1]] = 2
                IfChanged(defaultMatrix, MyMatrix)

    output = matrix
    PrintMatrix(matrix)
    MustFill(matrix[:], rule)
    return output

print(MUSTFILL(matrix,rule))