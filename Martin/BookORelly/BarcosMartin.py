def solution(N, S, T):
    #write your code in Python 3.6
    #Print Received N,S,T
    print("Table:",N)
    print("[S] Corner ship points:",S)
    print("[T] Hits:",T)

    #Dictionary to Map Columns
    ColsMap = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
             'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
             'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
             }

    MapCols = {1: 'A', 2:'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
               9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14:'N', 15: 'O', 16: 'P', 17: 'Q',
               18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
               }

    #Separation for columns and rows
    def ColsRowSeparation(X):
        XColsNum=[]
        XRowsNum = []
        Space = 0
        for j in range(len(X)):
            if X[j] in ColsMap.keys():
                #Change letter to number
                XColsNum.append(ColsMap[X[j]])
                #If no spaces on the first character of the string
                if Space == 0:
                    Space = -1
                XRowsNum.append(int(X[Space+1:j]))
            #Save position of last space
            elif X[j] == " ":
                Space = j
        return XColsNum, XRowsNum
    SColsNum, SRowsNum = ColsRowSeparation(S)
    print("S Columns", SColsNum)
    print("S Rows", SRowsNum)

    # Building Ships
    x = 0
    ShipsMatrix = []
    for k in range(0, int(len(SRowsNum) / 2)):
        OneShip = ""
        for i in range(SRowsNum[x], SRowsNum[x + 1] + 1):
            for j in range(SColsNum[x], SColsNum[x + 1] + 1):
                print("Area:",i,j)
                OneShip = OneShip + str(i) + MapCols[j]
        ShipsMatrix.append(OneShip)
        x = x + 2
    #Removing Ships repeated
    ShipsNoRpt=set(ShipsMatrix)
    ShipsList = list(ShipsNoRpt)
    print("Ships filled:", ShipsList)

    #Build T Hits Colums and Rows to remove spaces
    TColsNum, TRowsNum = ColsRowSeparation(T)
    print("T Columns", TColsNum)
    print("T Rows", TRowsNum)
    THits=[]
    #Map again T Colums to Letters
    TCols = []
    for i in TColsNum:
        TCols.append(MapCols[i])
    for i in range(len(TColsNum)):
        THits.append(str(TRowsNum[i])+TCols[i])
    #Removing Hits repeated
    THitsNoRpt=set(THits)
    THitsList = list(THitsNoRpt)
    print("Hits Matrix Num:",THitsList)

    #Create a list with number of elements of each ship
    ShipsNElmntsBase = []
    for i in range(len(ShipsList)):
        ShipsNElmntsBase.append(len(ShipsList[i]))
    ShipsNElmntsBaseFixed=tuple(ShipsNElmntsBase)
    print("Num Elements of Chars of Each Ship:",ShipsNElmntsBaseFixed)

    #Rest hits characters to each ship
    ShipsNElmntsComp=list(ShipsNElmntsBaseFixed)
    for i in THitsList:
        x=0
        for j in ShipsList:
            if i in j:
                print("Hits identified:",i+"->"+j)
                ShipsNElmntsComp[x]=ShipsNElmntsComp[x]-len(i)
            x+=1
    print("Hits Chars after Restart",ShipsNElmntsComp)

    #O means ships sunk
    ShipsSunk=sum(p == 0 for p in ShipsNElmntsComp)
    print("Ships Sunk:",ShipsSunk)

    #Ships hit but no sunk
    ShipsHitButNoSunk = 0-ShipsSunk
    for i in range(len(ShipsNElmntsBase)):
        if ShipsNElmntsComp[i] != ShipsNElmntsBase[i]:
            ShipsHitButNoSunk += 1
    print("Ships Hit But No Sunk:", ShipsHitButNoSunk)
    return ShipsSunk, ShipsHitButNoSunk

    #for i in range(len(ShipsList)):
    #    if THitsList[1] in ShipsList[i]:
    #        print(THitsList[1])
    #        print(ShipsList[i])

    #ShipsNElmnts = []
    #for i in range(len(ShipsList)):
    #    if ColsMap.keys() in ShipsList[i]:
    #     ShipsNElmnts.append(len(ShipsList[i]))
    #print(ShipsNElmnts)

    #Start filing a ship-hits matrix
    #for i in THitsList:
    #    for j in ShipsList:
    #        if i in j:


    #Start Hits Ships comparison
    #for k in THits:
    #if THits[3] in ShipsMatrix[1]:
        #print(THits[3])
    #if THits[3] in ShipsMatrix[1]:
        #ShipsMatrix.index[THits[3]]="XX"
    #print(ShipsMatrix[1][0])
    #print(len(ShipsMatrix[0]))
    #lst = ['a', 'ab', 'abc', 'bac']
    #res = [k for k in lst if 'ab' in k]
    #NewS=[]
    #for i in range(len(ShipsMatrix)):
    #    NewS.a
    #res = [k for k in ShipsMatrix if THits[0] in k]
    #print(res)
    #print(THits[0])

N = 4
S = "1B 2C, 2D 4D"
T = "2B 2D 3D 4D 4A"

#N = 12
#S = "1B 2C, 2D 4D, 10J 11K, 9C 11C, 1V 2W, 1B 2C "
#T = "  2B 2D 3D 4D 4A 11K 4C 12B 2B"
#ShipsSunk, ShipsHitButNotSunk (1, 2)
print("ShipsSunk, ShipsHitButNotSunk",solution(N,S,T))