import tkinter as tk
import random

from a2_snake_functions import (
    make_board,
    clear_board,
    place_snake_and_food,
    board_to_string,
    snake_as_pairs,
    move_snake,
    check_self_collision,
    update_direction,
    would_collide_after_move,
)
from constants import (
    BG_COLOR,
    CELL,
    DELAY_MIN_MS,
    DELAY_START_MS,
    DOWN,
    FOOD_COLOR,
    GRID_H,
    GRID_LINE,
    GRID_W,
    HEAD_COLOR,
    LEFT,
    RIGHT,
    SCORE_SPEED_CAP,
    SNAKE_COLOR,
    UP,
)


class SnakeGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Snake — A2")
        self.root.resizable(False, False)

        self.score = 0
        self.best = 0

        top = tk.Frame(root, bg=BG_COLOR)
        top.pack(fill="x")

        self.score_label = tk.Label(
            top, text="Score: 0   Best: 0",
            fg="white", bg=BG_COLOR
        )
        self.score_label.pack(side="left", padx=10)

        self.canvas = tk.Canvas(
            root,
            width=GRID_W * CELL,
            height=GRID_H * CELL,
            bg=BG_COLOR,
            highlightthickness=0
        )
        self.canvas.pack()

        self.draw_grid()

        root.bind("<Up>", lambda e: self.on_key(UP))
        root.bind("<Down>", lambda e: self.on_key(DOWN))
        root.bind("<Left>", lambda e: self.on_key(LEFT))
        root.bind("<Right>", lambda e: self.on_key(RIGHT))
        root.bind("r", lambda e: self.restart())
        root.bind("p", lambda e: self.print_board_once())

        self.restart()

    def restart(self):
        self.score = 0
        self.update_score()

        cx, cy = GRID_W // 2, GRID_H // 2

        self.snake_xs = [cx, cx - 1, cx - 2]
        self.snake_ys = [cy, cy, cy]

        self.dx, self.dy = 1, 0

        self.food = self.spawn_food()
        self.board = make_board(GRID_W, GRID_H)
        self._console_board_printed = False  

        self.tick()

    def tick(self):
        ate_food = move_snake(
            self.snake_xs,
            self.snake_ys,
            self.dx,
            self.dy,
            GRID_W,
            GRID_H,
            self.food
        )

        if check_self_collision(self.snake_xs, self.snake_ys):
            self.show_game_over()
            return

        if ate_food:
            self.score += 1
            self.best = max(self.best, self.score)
            self.update_score()
            self.food = self.spawn_food()

        self.update_board()
        self.render()

        delay = self.delay_for_score(self.score)
        self.root.after(delay, self.tick)

    def delay_for_score(self, score: int) -> int:
        """Return delay in ms for this score. Start slow, faster up to score 20, then cap."""
        if score >= SCORE_SPEED_CAP:
            return DELAY_MIN_MS
     
        t = score / SCORE_SPEED_CAP
        return int(DELAY_START_MS - (DELAY_START_MS - DELAY_MIN_MS) * t)

    def update_board(self):
        """Rebuild board using nested list utilities."""
        clear_board(self.board)

        snake_pairs = snake_as_pairs(self.snake_xs, self.snake_ys)

        place_snake_and_food(
            self.board,
            snake_pairs,
            self.food
        )

    def render(self):
        self.canvas.delete("all")
        self.draw_grid()

        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                value = self.board[y][x]

                if value == "H":
                    self.draw_cell(x, y, HEAD_COLOR)
                elif value == "S":
                    self.draw_cell(x, y, SNAKE_COLOR)
                elif value == "F":
                    self.draw_cell(x, y, FOOD_COLOR)

        
        if self._console_board_printed:
            print("\033[%dA" % GRID_H, end="")
        print(board_to_string(self.board))
        self._console_board_printed = True

    def draw_grid(self):
        for x in range(0, GRID_W * CELL, CELL):
            self.canvas.create_line(x, 0, x, GRID_H * CELL, fill=GRID_LINE)
        for y in range(0, GRID_H * CELL, CELL):
            self.canvas.create_line(0, y, GRID_W * CELL, y, fill=GRID_LINE)

    def draw_cell(self, x, y, color):
        x1 = x * CELL
        y1 = y * CELL
        x2 = x1 + CELL
        y2 = y1 + CELL
        self.canvas.create_rectangle(
            x1 + 1, y1 + 1, x2 - 1, y2 - 1,
            fill=color,
            outline=color
        )

    def print_board_once(self):
        """Print current board to console (press P). Fixed amount, no expanding."""
        print(board_to_string(self.board))
        print("---")

    def on_key(self, key: str):
        new_dx, new_dy = update_direction(self.dx, self.dy, key)
        # Ignore direction change if it would cause instant self-collision
        # (e.g. rapid Right -> Down -> Left with a short snake)
        if would_collide_after_move(
                self.snake_xs, self.snake_ys, new_dx, new_dy, GRID_W, GRID_H
        ):
            return
        self.dx, self.dy = new_dx, new_dy

    def spawn_food(self):
        snake_coords = snake_as_pairs(self.snake_xs, self.snake_ys)
        while True:
            x = random.randint(0, GRID_W - 1)
            y = random.randint(0, GRID_H - 1)
            if [x, y] not in snake_coords:
                return [x, y]

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}   Best: {self.best}")

    def show_game_over(self):
        self.canvas.create_text(
            GRID_W * CELL // 2,
            GRID_H * CELL // 2,
            text="GAME OVER\nPress R to Restart",
            fill="white",
            font=("Arial", 18, "bold"),
            justify="center"
        )


def main():
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
