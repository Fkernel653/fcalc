import customtkinter
from style import BACKGROUND, COMMENT, FOREGROUND, PINK, PURPLE, RED, SELECTION


class Button(customtkinter.CTkButton):
    def __init__(self, master, text, command, color, font_family="Arial", font_size=20):
        super().__init__(
            master=master,
            text=text,
            command=command,
            font=(font_family, font_size),
            fg_color=color,
        )


class Calc(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("")
        self.geometry("500x600")
        self.configure(fg_color=BACKGROUND)

        # Display
        self.display = customtkinter.CTkEntry(
            self,
            state="disabled",
            font=("Arial", 20),
            height=70,
            fg_color=SELECTION,
            text_color=FOREGROUND,
        )
        self.display.pack(padx=20, pady=20, fill="x")

        # Button frame
        self.button_frame = customtkinter.CTkFrame(self, fg_color=BACKGROUND)
        self.button_frame.pack(pady=10, padx=20, fill="both", expand=True)

        for i in range(4):
            self.button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            self.button_frame.grid_rowconfigure(i, weight=1)

        # Button configuration
        buttons = {
            "AC": (0, 0, RED),
            "DEL": (0, 1, COMMENT),
            "/": (0, 2, PINK),
            "*": (0, 3, PINK),
            "7": (1, 0, SELECTION),
            "8": (1, 1, SELECTION),
            "9": (1, 2, SELECTION),
            "-": (1, 3, PINK),
            "4": (2, 0, SELECTION),
            "5": (2, 1, SELECTION),
            "6": (2, 2, SELECTION),
            "+": (2, 3, PINK),
            "1": (3, 0, SELECTION),
            "2": (3, 1, SELECTION),
            "3": (3, 2, SELECTION),
            "=": (3, 3, PURPLE),
            "0": (4, 0, SELECTION),
            ".": (4, 1, SELECTION),
        }

        for text, (row, col, color) in buttons.items():
            btn = Button(
                self.button_frame, text, lambda t=text: self.handle_input(t), color
            )

            # Special sizing for equals button
            if text == "=":
                btn.grid(row=row, column=col, rowspan=2, padx=5, pady=5, sticky="nsew")
            else:
                btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        self.bind("<Key>", self.key_press)

    def handle_input(self, value):
        """Process button clicks"""
        if value == "AC":
            self.AC()
        elif value == "DEL":
            self.backspace_call()
        elif value == "=":
            self.answer()
        else:
            self.input(value)

    def key_press(self, event):
        """Handle keyboard input"""
        key_map = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "+": "+",
            "-": "-",
            "*": "*",
            "/": "/",
            ".": ".",
            "=": "=",
            "Return": "=",
            "BackSpace": "DEL",
            "Escape": "AC",
        }

        if event.char in key_map or event.keysym in key_map:
            self.handle_input(key_map.get(event.char) or key_map.get(event.keysym))

    def input(self, sign):
        """Add input to display"""
        self.display.configure(state="normal")

        if "Error" in self.display.get():
            self.display.delete(0, "end")

        self.display.insert("end", str(sign))
        self.display.configure(state="disabled")

    def backspace_call(self):
        """Delete last character"""
        self.display.configure(state="normal")
        cursor_position = self.display.index("insert")

        if cursor_position > 0:
            self.display.delete(cursor_position - 1, cursor_position)
        self.display.configure(state="disabled")

    def AC(self):
        """Clear display"""
        self.display.configure(state="normal")
        self.display.delete(0, "end")
        self.display.configure(state="disabled")

    def answer(self):
        """Calculate result"""
        self.display.configure(state="normal")
        expression = self.display.get()

        if expression:
            try:
                result = eval(expression)
                self.display.delete(0, "end")
                self.display.insert(0, str(result))
            except SyntaxError:
                self.display.delete(0, "end")
                self.display.insert(0, "Error: The syntax is incorrect")
            except ZeroDivisionError:
                self.display.delete(0, "end")
                self.display.insert(0, "Error: Divison by zero")
        else:
            self.display.insert(0, "")

        self.display.configure(state="disabled")


if __name__ == "__main__":
    window = Calc()
    window.mainloop()
