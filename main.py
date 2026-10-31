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
    """Получает и проверяет номер клетки."""
    raise NotImplementedError("Проверка ввода ещё не реализована.")


def next_player(player):
    """Возвращает знак следующего игрока."""
    raise NotImplementedError("Смена игроков ещё не реализована.")


def check_winner(board):
    """Возвращает X, O или None, если победителя нет."""
    raise NotImplementedError("Проверка победы ещё не реализована.")


def check_draw(board):
    """Возвращает True, если партия закончилась ничьей."""
    raise NotImplementedError("Проверка ничьей ещё не реализована.")


def ask_restart():
    """Спрашивает, нужно ли начать новую партию."""
    raise NotImplementedError("Перезапуск ещё не реализован.")


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