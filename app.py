#!/usr/bin/env python3
"""Tic-Tac-Toe - a simple terminal game for two players."""

from __future__ import annotations

from typing import Iterable

WIN_LINES: tuple[tuple[int, int, int], ...] = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def create_board() -> list[str]:
    return [" "] * 9


def draw_board(board: list[str]) -> None:
    display = [cell if cell != " " else str(i + 1) for i, cell in enumerate(board)]
    print()
    print(f" {display[0]} | {display[1]} | {display[2]}")
    print("---+---+---")
    print(f" {display[3]} | {display[4]} | {display[5]}")
    print("---+---+---")
    print(f" {display[6]} | {display[7]} | {display[8]}")
    print()


def has_winner(board: list[str], player: str) -> bool:
    return any(all(board[index] == player for index in line) for line in WIN_LINES)


def board_full(board: Iterable[str]) -> bool:
    return all(cell != " " for cell in board)


def get_move(board: list[str], player: str) -> int:
    while True:
        raw = input(f"Player {player}, choose a square (1-9): ").strip()
        if not raw.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        move = int(raw)
        if move < 1 or move > 9:
            print("Square must be between 1 and 9.")
            continue

        index = move - 1
        if board[index] != " ":
            print("That square is already taken. Pick another one.")
            continue

        return index


def play_game() -> None:
    board = create_board()
    current_player = "X"

    while True:
        draw_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        if has_winner(board, current_player):
            draw_board(board)
            print(f"Player {current_player} wins!")
            return

        if board_full(board):
            draw_board(board)
            print("It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"


def ask_replay() -> bool:
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Please answer with 'y' or 'n'.")


def main() -> None:
    print("Welcome to Tic-Tac-Toe!")
    print("Player X goes first.")

    while True:
        play_game()
        if not ask_replay():
            print("Thanks for playing.")
            break


if __name__ == "__main__":
    main()
