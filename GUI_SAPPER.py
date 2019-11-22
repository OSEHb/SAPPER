from tkinter import *
from random import randint


board = {}  # Голая доска для её заполнения
cell_in_board = {}  # Местоположение кнопки на доске
table = []
lst_check = []
color_button = []   # Для хранения цвета кнопки
check_result = 0


def generate_table():
    global table
    table = []
    m = 0

    for r in range(9):
        row = []
        for c in range(9):
            row.append(0)

        table.append(row)

    while True:
        if m >= 10:
            break

        a = randint(0, 8)
        b = randint(0, 8)

        if table[a][b] == 'X':
            continue
        else:
            table[a][b] = 'X'
            m += 1

    row = -1
    for r in table:
        row += 1
        col = -1
        for c in r:
            col += 1

            if c == 'X' and row == 0:
                if col == 0:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row + 1][col + 1] != 'X':
                        table[row + 1][col + 1] = table[row + 1][col + 1] + 1
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                elif col == 8:
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                    if table[row + 1][col - 1] != 'X':
                        table[row + 1][col - 1] = table[row + 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1
                else:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row + 1][col + 1] != 'X':
                        table[row + 1][col + 1] = table[row + 1][col + 1] + 1
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                    if table[row + 1][col - 1] != 'X':
                        table[row + 1][col - 1] = table[row + 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1

            elif c == 'X' and row == 8:
                if col == 0:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row - 1][col + 1] != 'X':
                        table[row - 1][col + 1] = table[row - 1][col + 1] + 1
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                elif col == 8:
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                    if table[row - 1][col - 1] != 'X':
                        table[row - 1][col - 1] = table[row - 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1
                else:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row - 1][col + 1] != 'X':
                        table[row - 1][col + 1] = table[row - 1][col + 1] + 1
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                    if table[row - 1][col - 1] != 'X':
                        table[row - 1][col - 1] = table[row - 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1

            elif c == 'X':
                if col == 0:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row - 1][col + 1] != 'X':
                        table[row - 1][col + 1] = table[row - 1][col + 1] + 1
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                    if table[row + 1][col + 1] != 'X':
                        table[row + 1][col + 1] = table[row + 1][col + 1] + 1
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                elif col == 8:
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                    if table[row - 1][col - 1] != 'X':
                        table[row - 1][col - 1] = table[row - 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1
                    if table[row + 1][col - 1] != 'X':
                        table[row + 1][col - 1] = table[row + 1][col - 1] + 1
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                else:
                    if table[row][col + 1] != 'X':
                        table[row][col + 1] = table[row][col + 1] + 1
                    if table[row - 1][col + 1] != 'X':
                        table[row - 1][col + 1] = table[row - 1][col + 1] + 1
                    if table[row - 1][col] != 'X':
                        table[row - 1][col] = table[row - 1][col] + 1
                    if table[row - 1][col - 1] != 'X':
                        table[row - 1][col - 1] = table[row - 1][col - 1] + 1
                    if table[row][col - 1] != 'X':
                        table[row][col - 1] = table[row][col - 1] + 1
                    if table[row + 1][col - 1] != 'X':
                        table[row + 1][col - 1] = table[row + 1][col - 1] + 1
                    if table[row + 1][col] != 'X':
                        table[row + 1][col] = table[row + 1][col] + 1
                    if table[row + 1][col + 1] != 'X':
                        table[row + 1][col + 1] = table[row + 1][col + 1] + 1


def zero(value):
    lst_zero = []
    board[value].configure(text='', bg='white')
    color_button.pop(0)
    color_button.append(board[value]['background'])
    word = value[0:6]
    number = int(value[6:])
    lst_check.append(value)

    if number - 10 >= 1:
        number_x = str(number - 10)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
            and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]), bg='white',
                                     font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number - 9 >= 1:
        number_x = str(number - 9)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
            and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]), bg='white',
                                     font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number - 8 >= 1:
        number_x = str(number - 8)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
            and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]), bg='white',
                                     font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number + 10 <= 81:
        number_x = str(number + 10)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
                and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]),
                                     bg='white', font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number + 9 <= 81:
        number_x = str(number + 9)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
                and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]),
                                     bg='white', font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number + 8 <= 81:
        number_x = str(number + 8)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
                and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]),
                                     bg='white', font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number + 1 <= 81:
        number_x = str(number + 1)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
                and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]),
                                     bg='white', font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    if number - 1 >= 1:
        number_x = str(number - 1)
        value_x = word + number_x

        if table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 'X' \
                and table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] != 0:
            board[value_x].configure(text=str(table[cell_in_board[value_x][0]][cell_in_board[value_x][1]]),
                                     bg='white', font='Helvetica 9 bold', fg='red')

        elif table[cell_in_board[value_x][0]][cell_in_board[value_x][1]] == 0:
            board[value_x].configure(text='', bg='white')
            lst_zero.append(value_x)

    while len(lst_zero) > 0:
        z = lst_zero[0]
        lst_zero.pop(0)
        if z not in lst_check:
            zero(z)


class Click:

    def __init__(self, cell, value):
        self.cell = cell
        self.value = value
        board[self.cell].bind('<Button-1>', self.open_cell)
        board[self.cell].bind('<Button-3>', self.find_mine)
        board[self.cell].bind('<Enter>', self.on_enter)
        board[self.cell].bind('<Leave>', self.on_leave)

    def find_mine(self, event):
        global check_result

        board[self.cell].configure(text='!', bg='green')
        color_button.pop(0)
        color_button.append(board[self.cell]['background'])
        if table[cell_in_board[self.cell][0]][cell_in_board[self.cell][1]] == 'X':
            check_result += 1
            if check_result == 10:
                for c in board:
                    if table[cell_in_board[c][0]][cell_in_board[c][1]] == 'X':
                        board[c].configure(text='!', bg='green', fg='white')
                    else:
                        board[c].configure(text=str(table[cell_in_board[c][0]][cell_in_board[c][1]]), bg='white')

                root.configure(bg='green')
                btn.configure(bg='white', fg='black')
                lbl_win.configure(height=3, text='YOU WIN !', bg='green', fg='white')
                lbl_win.grid(row=10, column=0, columnspan=9, sticky='ew')

    def open_cell(self, event):
        text_in_cell = str(table[self.value[0]][self.value[1]])

        if text_in_cell == 'X':
            for c in board:
                if table[cell_in_board[c][0]][cell_in_board[c][1]] == 'X':
                    board[c].configure(text=str(table[cell_in_board[c][0]][cell_in_board[c][1]]), bg='red', fg='white')
                    color_button.pop(0)
                    color_button.append(board[self.cell]['background'])
                else:
                    board[c].configure(text=str(table[cell_in_board[c][0]][cell_in_board[c][1]]), bg='black', fg='white')

            root.configure(bg='red')
            btn.configure(bg='black')
            lbl_lose.configure(height=3, text='YOU LOSE !', bg='red', fg='white')
            lbl_lose.grid(row=10, column=0, columnspan=9, sticky='ew')
        elif text_in_cell == '0':
            zero(self.cell)
        else:
            board[self.cell].configure(text=text_in_cell, bg='white', fg='red', font='Helvetica 9 bold')
            color_button.pop(0)
            color_button.append(board[self.cell]['background'])

    def on_enter(self, event):
        color_button.append(board[self.cell]['background'])  # сохраняю цвет кнопки при наведении
        board[self.cell].configure(bg='#b0e2e8')  # меняю цвет кнопки при наведении

    def on_leave(self, event):
        board[self.cell].configure(bg=color_button[0])  # возвращаю сохранённый цвет кнопки при уходе с кнопки
        color_button.pop(0)  # удаляю цвет


def start_game():
    global board, check_result, cell_in_board, table, lst_check

    lbl_win.grid_forget()
    lbl_lose.grid_forget()
    root.configure(bg='white')
    btn.configure(bg='#2b576e', fg='white')
    board = {}
    cell_in_board = {}
    table = []
    lst_check = []
    check_result = 0
    generate_table()

    for n in range(1, 82):  # n - номер button на доске
        b = 'button' + str(n)
        cell_number = 0

        for row in range(1, 10):
            if cell_number >= n:
                break

            for col in range(9):
                cell_number += 1
                if cell_number > n:
                    break
                elif cell_number != n:
                    continue
                else:
                    board[b] = Button(root, width=4, height=2, bg='#2b576e')
                    board[b].grid(row=row, column=col, padx=1, pady=1)
                    cell_in_board[b] = (row - 1, col)
                    break

    for cell in board:
        Click(cell, cell_in_board[cell])


root = Tk()
root.title('Sapper')
root.resizable(width=False, height=False)
root.configure(bg='black')

btn = Button(root, text='Начать Игру', command=start_game)
btn.grid(row=0, column=0, columnspan=9, padx=5, pady=3, sticky='ew')

lbl_win = Label(root)
lbl_lose = Label(root)

# заполняем доску board
for n in range(1, 82):  # n - номер lebel на доске
    l = 'lebel' + str(n)
    cell_number = 0

    for row in range(1, 10):
        if cell_number >= n:
            break

        for col in range(9):
            cell_number += 1
            if cell_number > n:
                break
            elif cell_number != n:
                continue
            else:
                board[l] = Label(root, width=4, height=2)
                board[l].grid(row=row, column=col, padx=1, pady=1)
                break


root.mainloop()


