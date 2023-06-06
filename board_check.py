def visualize(board):
    f1 = f'| {board[0]} | {board[1]} | {board[2]} |'
    f2 = f'| {board[3]} | {board[4]} | {board[5]} |'
    f3 = f'| {board[6]} | {board[7]} | {board[8]} |'
    lf1 = len(f1)
    lf2 = len(f2)
    print(f1)
    print('-'*lf1)
    print(f2)
    print('-'*lf2)
    print(f3)

def sorter(board):
        def win(player):
                if board[0:3] == player:
                    return True
                    
                elif board[3:6] == player:
                    return True
                    
                elif board[6:9] == player:
                    return True
                    
                elif board[0::3] == player:
                    return True
                    
                elif board[1::3] == player:
                    return True
                    
                elif board[2::3] == player:
                    return True
                    
                elif board[0::4] == player:
                    return True
                    
                elif board[2:7:2] == player:
                    return True
        x_win = ['1', '1', '1']
        o_win = ['2', '2', '2']
        if win(x_win) is True:
            board.insert(0, '1')
            return board
        elif win(o_win) is True:
            board.insert(0, '2')
            return board
        else:
            board.insert(0, '0')
            board
        # def conditions(x_win, o_win):
        #     if win(x_win) is True:
        #         return '1'
        #     elif win(o_win) is True:
        #         return '2'
        # if len(board) < 9:
        #     for p in range(9-len(board)):
        #         board.insert(0, '0')
        # if conditions(x_win, o_win) == '1':
        #     board.insert(0, '1')
        #     return board
        # elif conditions(x_win, o_win) == '2':
        #     board.insert(0, '2')
        #     return board
        # else:
        #      board.insert(0, '0')
        #      return board
def game():
    board = ['0']*9
    print(board)
    turns = 0
    while turns != 9:
        visualize(board)
        if turns%2 == 0:
            x = int(input('X: '))
            if board[x] == '0':
                board.pop(x)
                board.insert(x, '1')
                turns += 1
            else:
                print('This cell is occupied! Try somewhere else.')
        else:
            o = int(input('O: '))
            if board[o] == '0':
                board.pop(o)
                board.insert(o, '2')
                turns += 1
            else:
                print('This cell is occupied! Try somewhere else.')
        # print(sorter(board))
        # if sorter(board)[0] == '1':
        #     print('X wins')
        #     return 1
        # elif sorter(board)[0] == '2':
        #     print('O wins')
        #     return 2
    print('Its a draw')
    return 0
game()