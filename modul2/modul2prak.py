import random


# Fungsi untuk membuat board matrix
def create_board(width):
    return [[" " for _ in range(width)] for _ in range(width)]


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


# Fungsi untuk memeriksa apakah permainan selesai
def is_game_over(board, current_pos, goal_pos):
    return current_pos == goal_pos


current_pos = start_pos

while True:
    move = input(
        "Masukkan perintah (w/a/s/d untuk atas/kiri/bawah/kanan, q untuk keluar): "
    ).lower()

    if move == "q":
        print("Permainan dihentikan.")
        break
    elif move in ["w", "a", "s", "d"]:
        x, y = current_pos
        if move == "w":
            x -= 1
        elif move == "a":
            y -= 1
        elif move == "s":
            x += 1
        elif move == "d":
            y += 1

        if 0 <= x < width and 0 <= y < width:
            board[current_pos[0]][current_pos[1]] = " "
            current_pos = (x, y)
            board[current_pos[0]][current_pos[1]] = "A"
            display_board(board)

            if is_game_over(board, current_pos, goal_pos):
                print("Anda menang! Selamat!")
                break
        else:
            print("Langkah tidak valid. Coba lagi.")

    else:
        print("Perintah tidak valid. Coba lagi.")
