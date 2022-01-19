length = 10
rule = [1,3]

matrix = []
for i in range(0, length):
    matrix.append(0)


def PrintMatrix(matrix):
    for i in range(0, len(matrix)):
        if matrix[i]==0: char = '-'
        elif matrix[i]==1: char = '■'
        else: char = '□'
        print(char, end='')
    print('')

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
                        PrintMatrix(myMatrix)
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

    return myOutput


matrix = [1,0,0,0,0,0,0,0,0,0]
output = ReturnGuess(matrix, rule)
print(output)