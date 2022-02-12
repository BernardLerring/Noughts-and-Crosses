#this game was created using the framework at medium.com
#to assist with the code. Their are personalisations in 
#my code to make it function as I wanted it to.

"""Board will be made using a dictionary that will be represented by
the numbers on the numerical keypad. These will be empty until the
player selects their position"""

theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

# Prints the game board to the terminal to allow the entry of
# noughts or crosses. A new board will be created and printed
# after every turn


def print_board(board):

    """Prints the game board"""

    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])


def game():

    """Runs the game"""

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(theBoard)
        print('Your move, ' + turn + '.')
        print('Select a number between 1 and 9')

        while True:
            move = input()
            try:
                if move not in theBoard.keys():
                    raise ValueError("Please enter a value between 1 and 9")
            except ValueError as e:
                print(f"Invalid entry: {e}, try again")
            else:
                break

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1    
        else:
            print('That space is taken.\nMove to which other space?')
            continue

        # now we check if either player has won after 5 moves

        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                # top row win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                # middle row win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                # bottom row win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                # left side win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                # middle column win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                # right side win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                # diagonal win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                # diagonal win
                print_board(theBoard)
                print('\nGame Over\n')
                print(' **** ' + turn + ' won. ****')
                break

        # if neither 0 or X wins, and the board is full we declare a tied game
        if count == 9:
            print('\nGame tied\n')
            restart = input('Would you like to play another game?(y/n?)')
            if restart == 'y' or restart == 'Y':
                for key in board_keys:
                    theBoard[key] = ' '

                game()

        # change player after each turn
        if turn == 'X':
            turn = '0'

        else:
            turn = 'X'

    # ask user if they want to play another game
    restart = input('Would you like to play another game?(y/n?)')
    if restart == 'y' or restart == 'Y':
        for key in board_keys:
            theBoard[key] = ' '

        game()


if __name__ == '__main__':
    game()