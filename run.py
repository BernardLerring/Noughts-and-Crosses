theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}


def print_board(board):

    """prints the game board to the terminal to allow the entry of
    noughts or crosses"""

    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+-+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+-+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


def game():

    turn = 'X'
    count = 0