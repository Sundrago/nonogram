
rule = [5,2]

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

def Guess(MyMtrix, MyRule):
    if len(MyRule) == 0: return
    flag = True

    def Fill(idx):
        if not 0 in MyMtrix: return
        begin = MyMtrix.index(0)
        for i in range(begin, len(MyMtrix)):
            flag = True
            for k in range(begin, i):
                MyMtrix[k] = 2
            for j in range(0, MyRule[idx]):
                if i+j >= len(MyMtrix): 
                    flag = False
                    continue
                MyMtrix[i+j] = 1
                for l in range (i+j+1, len(MyMtrix)):
                    MyMtrix[l] = 0
            if(flag): 
                if idx == len(MyRule)-1:
                    for k in range(i, len(MyMtrix)):
                        if MyMtrix[k] == 0: MyMtrix[k] = 2
                    PrintMatrix(MyMtrix)
                else:
                    if 0 in MyMtrix: MyMtrix[MyMtrix.index(0)] = 2
                    Fill(idx+1)
    Fill(0)

Guess(matrix[:], rule[:])