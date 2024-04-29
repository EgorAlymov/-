# Создаем игровую доску

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Отбражаем игровую доску

def display_board(board):
    for row in board:
        print(row[0] + ' | ' + row[1] + ' | ' + row[2])
        print('---------')
display_board(board)

# Ход игрока

def make_move(board, row, col, symbol):
    if board[row][col] == ' ':
        board[row][col] = symbol
        return True
    else:
        return False
#Проверка победителя

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    return False

# Основной игровой цикл

def main_game():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    display_board(board)
    current_player = 'X'
    while True:
        print('Ход игрока', current_player)
        row = int(input('Введите номер строки (0-2): '))
        col = int(input('Введите номер столбца (0-2): '))
        if make_move(board, row, col, current_player):
            display_board(board)
            if check_winner(board):
                print('Игрок', current_player, 'победил!')
                break
            elif all([cell != ' ' for row in board for cell in row]):
                print('Игра окончена! Ничья.')
                break
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Неверный ход. Попробуйте еще раз.')

#Запуск игры

if __name__ == '__main__':
    main_game()








