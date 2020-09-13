""" 
Made by Calvin Miller (CalvinMiller190)

World's hardest sudoku (800000000003600000070090200050007000000045700000100030001000068008500010090000400)
Can be solved in >4 seconds!!

Uses backtracing.

"""

def get_board():
    correct = False
    while not correct:
        try: 
            b = int(input("Board going from left to right, 0 = empty:\n> "))
        except:
            print("Board must be a string of numbers.")
            return
        if len(str(b)) != 81:
            print("Board must be 81 characters long.")
        else:
            lst = list(str(b))
            grid = []
            for num in range(len(lst)+1):
                if num%9==0 and num != 0:
                    for i in range(len(lst)):
                        lst[i] = int(lst[i])
                    grid.append(lst[num-9:num])
            correct = True
            return grid

board = get_board()

def solve(bo):
    find = find_empty(bo)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(bo, (row, col), i):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, pos, num):
    # Check row
    for i in range(0, len(bo)):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Col
    for i in range(0, len(bo)):
        if bo[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box

    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)

    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


print("\n\n        Regular\n------------------------\n------------------------\n\n")
print_board(board)
solve(board)
print("\n\n        Solved\n------------------------\n------------------------\n\n")
print_board(board)
print("\n\n------------------------\n\n")