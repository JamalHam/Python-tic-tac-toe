#python tic tac toe

def tictactoe():
    turnCounter = 1

    baseTile = 'x'

    R1_1 = ' '
    R1_2 = ' '
    R1_3 = ' '

    R2_1 = ' '
    R2_2 = ' '
    R2_3 = ' '

    R3_1 = ' '
    R3_2 = ' '
    R3_3 = ' '

    refList = [1, 2, 3, 4, 5, 6, 7, 8, 9, '1', '2', '3', '4', '5', '6', '7', '8', '9']

    usedNums = []

    print("time for a game of x's and o's!")
    print("X goes first!!")
    print("3 in a row wins!")
    print('when picking a number between 1 and 9, numbers flow right to left and top to bottom')
    print(
        '''
         1 | 2 | 3
        ---+---+---
         4 | 5 | 6
        ---+---+---
         7 | 8 | 9
        '''
    )

    while turnCounter != 10:
        if (turnCounter % 2) == 0:
            baseTile = 'o'
        else:
            baseTile = 'x'

        txt = input("pick a number between 1 and 9: ")

        if txt in refList and txt not in usedNums:

            if txt == 1 or txt == '1':
                R1_1 = baseTile
            
            if txt == 2 or txt == '2':
                R1_2 = baseTile
            
            if txt == 3 or txt == '3':
                R1_3 = baseTile
            
            if txt == 4 or txt == '4':
                R2_1 = baseTile
            
            if txt == 5 or txt == '5':
                R2_2 = baseTile
            
            if txt == 6 or txt == '6':
                R2_3 = baseTile

            if txt == 7 or txt == '7':
                R3_1 = baseTile

            if txt == 8 or txt == '8':
                R3_2 = baseTile

            if txt == 9 or txt == '9':
                R3_3 = baseTile

            usedNums.append(txt)
            printBoard(R1_1, R1_2, R1_3, R2_1, R2_2, R2_3, R3_1, R3_2, R3_3)

            turnCounter += 1

            #winner check
            sets1 = [('o', R1_1, R1_2, R1_3), ('o', R2_1, R2_2, R2_3), ('o', R3_1, R3_2, R3_3), ('o', R1_1, R2_1, R3_1), ('o', R1_2, R2_2, R3_2), ('o', R1_3, R2_3, R3_3), ('o', R1_1, R2_2, R3_3), ('o', R1_3, R2_2, R3_1)]
            sets2 = [('x', R1_1, R1_2, R1_3), ('x', R2_1, R2_2, R2_3), ('x', R3_1, R3_2, R3_3), ('x', R1_1, R2_1, R3_1), ('x', R1_2, R2_2, R3_2), ('x', R1_3, R2_3, R3_3), ('x', R1_1, R2_2, R3_3), ('x', R1_3, R2_2, R3_1)]
            for setTest in sets1:
                if winTester(*setTest):
                    print('player 2 has one the game!!!!')
                    turnCounter = 10
            
            for setTest in sets2:
                if winTester(*setTest):
                    print('player 1 has one the game!!!!')
                    turnCounter = 10
            

        else:
            print("try again! you pick a number between 1 and 9 that hasn't been used")

    
def printBoard(R1_1, R1_2, R1_3, R2_1, R2_2, R2_3, R3_1, R3_2, R3_3):
        board = '''
             {0} | {1} | {2}
            ---+---+---
             {3} | {4} | {5}
            ---+---+---
             {6} | {7} | {8}
            '''.format(R1_1, R1_2, R1_3, R2_1, R2_2, R2_3, R3_1, R3_2, R3_3)

        print(board)


def winTester(val, option1, option2, option3):
    winLose = False
    values = [option1, option2, option3]

    if all(v == val for v in values):
        winLose = True
    else:
        winLose = False

    return winLose

tictactoe()

    