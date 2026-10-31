def print_board(board):
    """Выводит поле. Вместо пустых клеток показывает их номера."""
    cells = [
        str(i + 1) if cell == " " else cell
        for i, cell in enumerate(board)
    ]

    for row in range(3):
        start = row * 3
        print(" | ".join(cells[start:start + 3]))

        if row < 2:
            print("---------")

    print()


def read_move(board):
    while True:
        text = input("Номер клетки (1–9): ").strip()

        try:
            number = int(text)
        except ValueError:
            print("Введи целое число от 1 до 9.")
            continue

        if not 1 <= number <= 9:
            print("Такой клетки нет. Выбери число от 1 до 9.")
            continue

        index = number - 1

        if board[index] != " ":
            print("Клетка занята. Выбери другую.")
            continue

        return index


def next_player(player):
    if player == "X":
        return "O"

    return "X"


def check_winner(board):
    lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),

        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),

        (0, 4, 8),
        (2, 4, 6),
    )

    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]

    return None


def check_draw(board):
    return " " not in board and check_winner(board) is None


def ask_restart():
    while True:
        answer = input("Сыграть ещё раз? (да/нет): ").strip().lower()

        if answer in ("да", "д", "yes", "y"):
            return True

        if answer in ("нет", "н", "no", "n"):
            return False

        print("Ответь «да» или «нет».")

def main():
    while True:
        board = [" "] * 9
        player = "X"

        print("Крестики-нолики")
        print_board(board)

        while True:
            print(f"Ход игрока {player}")

            index = read_move(board)
            board[index] = player

            print_board(board)

            winner = check_winner(board)

            if winner is not None:
                print(f"Победил игрок {winner}!")
                break

            if check_draw(board):
                print("Ничья!")
                break

            player = next_player(player)

        if not ask_restart():
            print("Игра завершена.")
            break


if __name__ == "__main__":
    try:
        main()
    except NotImplementedError as error:
        print(f"Каркас игры: {error}")