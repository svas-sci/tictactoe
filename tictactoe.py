playspace = {11:'-', 12:'-', 13:'-', 21:'-', 22:'-', 23:'-', 31:'-', 32:'-', 33:'-'}
valspace = {11:1, 12:0, 13:1, 21:0, 22:1, 23:0, 31:1, 32:0, 33:1}
availspace = [11, 12, 13, 21, 22, 23, 31, 32, 33]

def printplayspace():
    print(playspace[11], '|', playspace[12], '|', playspace[13])
    print(playspace[21], '|', playspace[22], '|', playspace[23])
    print(playspace[31], '|' ,playspace[32] ,'|', playspace[33])

def findadjacent(currentspace):
    adjacent = []
    if currentspace+1 in availspace: adjacent.append(currentspace+1)
    if currentspace-1 in availspace: adjacent.append(currentspace-1)
    if currentspace+10 in availspace: adjacent.append(currentspace+10)
    if currentspace-10 in availspace: adjacent.append(currentspace-10)
    return(adjacent)

def incrementadjacent(nowspace):
    adjacentlist = findadjacent(nowspace)
    for i in adjacentlist:
        print('------------')
        print('this is i', i)
        valspace[i] +=1
    
    print(valspace)


def bonusblock(yesspace):
    tocheck = findadjacent(yesspace)
    for i in range(len(tocheck)):
        if playspace[yesspace] == playspace[tocheck[i]]:
            if yesspace-tocheck[i] == 1:
                valspace[yesspace-1] +=5
            if yesspace-tocheck[i] == -1:
                valspace[yesspace+1] +=5
            if yesspace-tocheck[i] == 10:
                valspace[yesspace-10] +=5
            if yesspace-tocheck[i] == -10:
                valspace[yesspace+10] += 5
    
    if yesspace in [11, 22, 33]:
        if yesspace == 11:
            if playspace[22] == playspace[11]:
                valspace[33] +=5
        if yesspace == 22:
            if playspace[22] == playspace[11]:
                valspace[33] +=5
            elif playspace[22] == playspace[33]:
                valspace[11] +=5
        if yesspace == 33:
            if playspace[33] == playspace[22]:
                valspace[11] +=5

    if yesspace in [31, 22, 13]:
        if yesspace == 31:
            if playspace[31] == playspace[22]:
                valspace[13] +=5
        if yesspace == 22:
            if playspace[22] == playspace[31]:
                valspace[13] +=5
            elif playspace[22] == playspace[13]:
                valspace[31] +=5
        if yesspace == 13:
            if playspace[13] == playspace[22]:
                valspace[31] +=5

def gapbonus(inputyes):
    if playspace[inputyes] == playspace[11] and playspace[11] == playspace[13]:
        valspace[12] +=5
    if playspace[inputyes] == playspace[21] and  playspace[21] == playspace[23]:
        valspace[22] +=5
    if playspace[inputyes] == playspace[31] and  playspace[31] == playspace[33]:
        valspace[32] +=5
    if playspace[inputyes] == playspace[11] and  playspace[11] == playspace[31]:
        valspace[21] +=5
    if playspace[inputyes] == playspace[12] and  playspace[12] == playspace[32]:
        valspace[22] +=5
    if playspace[inputyes] == playspace[13] and  playspace[13] == playspace[33]:
        valspace[23] +=5
    if playspace[inputyes] == playspace[11] and  playspace[11] == playspace[33]:
        valspace[22] +=5
    if playspace[inputyes] == playspace[13] and  playspace[13] == playspace[31]:
        valspace[22] +=5

def printboard():
    print(
        f"      {valspace[11]}|      {valspace[12]}|      {valspace[12]}\n"
        f"   {playspace[11]}   |   {playspace[12]}   |   {playspace[13]}   \n"
        "       |       |       \n"
        "-----------------------\n"
        f"      {valspace[21]}|      {valspace[22]}|      {valspace[23]}\n"
        f"   {playspace[21]}   |   {playspace[22]}   |   {playspace[23]}   \n"
        "       |       |       \n"
        "-----------------------\n"
        f"      {valspace[31]}|      {valspace[32]}|      {valspace[33]}\n"
        f"   {playspace[31]}   |   {playspace[32]}   |   {playspace[33]}   \n"
        "       |       |       \n"
        )

def checkwin():
    global win
    if playspace[11] != '-' and playspace[11] == playspace[22] and playspace[22]==playspace[33]:
        print(playspace[11], 'wins!') #top left to bottom right diagonal
        return True
    if playspace[31] != '-' and playspace[31] == playspace[22] and playspace[22]==playspace[13]:
        print(playspace[31], 'wins!') #bottom left to top right diagonal
        return True
    if playspace[11] != '-' and playspace[11] == playspace[12] and playspace[12]==playspace[13]:
        print(playspace[11], 'wins!') #top row
        return True
    if playspace[21] != '-' and playspace[21] == playspace[22] and playspace[22]==playspace[23]:
        print(playspace[21], 'wins!') #middle row
        return True
    if playspace[31] != '-' and playspace[31] == playspace[32] and playspace[32]==playspace[33]:
        print(playspace[31], 'wins!') #bottom row
        return True
    if playspace[11] != '-' and playspace[11] == playspace[21] and playspace[21]==playspace[31]:
        print(playspace[11], 'wins!') #left column
        return True
    if playspace[12] != '-' and playspace[12] == playspace[22] and playspace[22]==playspace[32]:
        print(playspace[12], 'wins!') #middle column
        return True
    if playspace[13] != '-' and playspace[13] == playspace[23] and playspace[23]==playspace[33]:
        print(playspace[13], 'wins!') #right column
        return True
    
printboard()
while True:
    if checkwin() != True:
        while True:
            spot = int(input('enter your position (x)'))
            print('this is now your spot')
            if playspace[spot] == '-':
                playspace[spot] = 'x'
                incrementadjacent(spot)
                bonusblock(spot)
                gapbonus(spot)
                printboard()
                break
            else:
                print('invalid move')

        checkwin()

        bestspot = list(dict(sorted(valspace.items(), key = lambda item: item[1], reverse=True)))
        print('this is bestspot list', bestspot)
        for i in range(len(bestspot)):
            if playspace[bestspot[i]] == '-':
                print(bestspot[i])
                playspace[bestspot[i]] = 'o'
                yes = findadjacent(bestspot[i])
                print('these are adjacent', yes)
                incrementadjacent(bestspot[i])
                bonusblock(bestspot[i])
                gapbonus(bestspot[i])
                printboard()
                break
        checkwin()
    
