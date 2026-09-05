import tkinter as tk


def draw_maze():
    # shape.txt 파일이 같은 폴더에 있어야 합니다.
    with open("shape.txt", "r") as file:
        lines = [line.rstrip("\n") for line in file.readlines()]

    box_size = 40
    max_cols = max(len(line) for line in lines)
    max_rows = len(lines)

    root = tk.Tk()
    root.title("Pacman Maze")

    canvas = tk.Canvas(
        root, width=max_cols * box_size, height=max_rows * box_size, bg="white"
    )
    canvas.pack()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            top_left_column = col * box_size
            top_left_row = row * box_size
            bottom_right_column = top_left_column + box_size
            bottom_right_row = top_left_row + box_size

            if char == "*":
                canvas.create_rectangle(
                    top_left_column,
                    top_left_row,
                    bottom_right_column,
                    bottom_right_row,
                    fill="#ffffff",
                    outline="#000000",
                )
            elif char.upper() == "P":
                canvas.create_arc(
                    top_left_column,
                    top_left_row,
                    bottom_right_column,
                    bottom_right_row,
                    start=25,
                    extent=315,
                    fill="#ffff00",
                    outline="#000000",
                    width=2,
                )

                eye_x1 = top_left_column + box_size * 0.4
                eye_y1 = top_left_row + box_size * 0.2
                eye_x2 = top_left_column + box_size * 0.55
                eye_y2 = top_left_row + box_size * 0.35

                canvas.create_oval(
                    eye_x1, eye_y1, eye_x2, eye_y2, fill="#000000", width=0.1
                )

    root.mainloop()


if __name__ == "__main__":
    draw_maze()