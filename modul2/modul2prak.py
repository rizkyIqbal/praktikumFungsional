import random

ulangSemua =""

# Fungsi untuk membuat board matrix
def create_board(width):
    return [["-" for _ in range(width)] for _ in range(width)]


# Fungsi untuk menampilkan board
def display_board(board):
    for row in board:
        print(" ".join(row))


# Fungsi untuk mengacak posisi awal bidak dan tujuan (goals)
def generate_positions(width):
    positions = []
    for _ in range(3):
        x = random.randint(0, width - 1)
        y = random.randint(0, width - 1)
        positions.append((x, y))
    return positions


# Inisialisasi board dengan lebar sesuai input user
width = int(input("Masukkan lebar board: "))
board = create_board(width)


# Membuat posisi awal bidak dan tujuan secara acak
try:
    positions = generate_positions(width)
    start_pos, goal_pos = positions[0], positions[1]
    board[start_pos[0]][start_pos[1]] = "A"
    board[goal_pos[0]][goal_pos[1]] = "O"
except IndexError:
    print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")

display_board(board)

repeat = input(
    "New Position (Y/N)?"
).lower()

ulang = 0

while repeat == "y":
    board[start_pos[0]][start_pos[1]] = "-"
    board[goal_pos[0]][goal_pos[1]] = "-"
    try:
        positions = generate_positions(width)
        start_pos, goal_pos = positions[0], positions[1]
        board[start_pos[0]][start_pos[1]] = "A"
        board[goal_pos[0]][goal_pos[1]] = "O"
    except IndexError:
        print("Kesalahan dalam menghasilkan posisi awal dan tujuan.")
    display_board(board)

    repeat = input(
        "New Position (Y/N)?"
    ).lower()
    ulang += 1
    if(ulang == 3):
        print("Maximal 3 dalam mengubah posisi!")
        repeat = "n"
    




# Fungsi untuk memeriksa apakah permainan selesai
def is_game_over(board, current_pos, goal_pos):
    return current_pos == goal_pos


current_pos = start_pos

while ulangSemua == "y" or ulangSemua == "":
    move = input(
        "Masukkan perintah (w/a/s/d untuk atas/kiri/bawah/kanan, q untuk keluar): "
    ).lower()

    inputList= [char for char in move]
    # print(inputList)
    for list in inputList:
        if list == "q":
            print("Permainan dihentikan.")
            break
        elif list in ["w", "a", "s", "d"]:
            x, y = current_pos
            if list == "w":
                x -= 1
            elif list == "a":
                y -= 1
            elif list == "s":
                x += 1
            elif list == "d":
                y += 1

            if 0 <= x < width and 0 <= y < width:
                board[current_pos[0]][current_pos[1]] = "-"
                current_pos = (x, y)
                board[current_pos[0]][current_pos[1]] = "A"
                

                if is_game_over(board, current_pos, goal_pos):
                    display_board(board)
                    print("Anda menang! Selamat!")
                    break
                else:
                    display_board(board)
                    print("You Lose! Selamat!")
                    False
            else:
                print("Langkah tidak valid. Coba lagi.")

        else:
            print("Perintah tidak valid. Coba lagi.")
    ulangSemua = "n"
