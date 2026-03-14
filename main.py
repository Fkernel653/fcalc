import customtkinter

class Calc(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('calc')
        self.geometry('500x600')
        self._set_appearance_mode('system')
        
        # Create display entry widget (read-only)
        self.display = customtkinter.CTkEntry(
            self,
            placeholder_text='',
            state='disabled',
            font = ('Arial', 20),
            height=70
            )

        self.display.pack(padx=20, pady=20, fill='x')
        
        # Create frame for buttons
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.pack(pady=10, padx=20, fill='both', expand=True)
        
        # Configure grid layout for button frame
        self.button_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.button_frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        # Addition button
        self.button_plus = customtkinter.CTkButton(
            self.button_frame,
            text='+',
            command=lambda: self.input('+'),
            font = ('Arial', 18),
            fg_color='blue'
        )

        self.button_plus.grid(row=2, column=3, padx=5, pady=5, sticky='nsew')
 
        # Subtraction button
        self.button_minus = customtkinter.CTkButton(
            self.button_frame,
            text='-',
            command=lambda: self.input('-'),
            font = ('Arial', 18),
            fg_color='blue'
        )

        self.button_minus.grid(row=1, column=3, padx=5, pady=5, sticky='nsew')
        
        # Multiplication button
        self.button_multiplication = customtkinter.CTkButton(
            self.button_frame,
            text='*',
            command=lambda: self.input('*'),
            font = ('Arial', 18),
            fg_color='blue'
        )

        self.button_multiplication.grid(row=0, column=3, padx=5, pady=5, sticky='nsew')
        
        # Division button
        self.button_division = customtkinter.CTkButton(
            self.button_frame,
            text='/',
            command=lambda: self.input('/'),
            font = ('Arial', 18),
            fg_color='blue'
        )
    
        self.button_division.grid(row=0, column=2, padx=5, pady=5, sticky='nsew')
        
        # Number 0 button
        self.button_0 = customtkinter.CTkButton(
            self.button_frame,
            text='0',
            command=lambda: self.input(0),
            font=('Arial', 18),
            height=60
        )
        self.button_0.grid(row=4, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')

        # Number 1 button
        self.button_1 = customtkinter.CTkButton(
            self.button_frame,
            text='1',
            command=lambda: self.input(1),
            font=('Arial', 18),
            height=60
        )
        self.button_1.grid(row=3, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 2 button
        self.button_2 = customtkinter.CTkButton(
            self.button_frame,
            text='2',
            command=lambda: self.input(2),
            font=('Arial', 18),
            height=60
        )
        self.button_2.grid(row=3, column=1, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 3 button
        self.button_3 = customtkinter.CTkButton(
            self.button_frame,
            text='3',
            command=lambda: self.input(3),
            font=('Arial', 18),
            height=60
        )
        self.button_3.grid(row=3, column=2, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 4 button
        self.button_4 = customtkinter.CTkButton(
            self.button_frame,
            text='4',
            command=lambda: self.input(4),
            font=('Arial', 18),
            height=60
        )
        self.button_4.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 5 button
        self.button_5 = customtkinter.CTkButton(
            self.button_frame,
            text='5',
            command=lambda: self.input(5),
            font=('Arial', 18),
            height=60
        )
        self.button_5.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 6 button
        self.button_6 = customtkinter.CTkButton(
            self.button_frame,
            text='6',
            command=lambda: self.input(6),
            font=('Arial', 18),
            height=60
        )
        self.button_6.grid(row=2, column=2, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 7 button
        self.button_7 = customtkinter.CTkButton(
            self.button_frame,
            text='7',
            command=lambda: self.input(7),
            font=('Arial', 18),
            height=60
        )
        self.button_7.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 8 button
        self.button_8 = customtkinter.CTkButton(
            self.button_frame,
            text='8',
            command=lambda: self.input(8),
            font=('Arial', 18),
            height=60
        )
        self.button_8.grid(row=1, column=1, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Number 9 button
        self.button_9 = customtkinter.CTkButton(
            self.button_frame,
            text='9',
            command=lambda: self.input(9),
            font=('Arial', 18),
            height=60
        )
        self.button_9.grid(row=1, column=2, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Decimal point button
        self.button_dot = customtkinter.CTkButton(
            self.button_frame,
            text='.',
            command=lambda: self.input('.'),
            height=60
        )
        
        self.button_dot.grid(row=4, column=1, columnspan=1, padx=5, pady=5, sticky='nsew')
        
        # Equals button (calculates result)
        self.button_equals = customtkinter.CTkButton(
            self.button_frame,
            text='=',
            command=self.answer,
            fg_color='green',
            font=("Arial", 18),
            height=60
        )

        self.button_equals.grid(row=3, column=3, rowspan=2, padx=5, pady=5, sticky='nsew')
        
        # Backspace/Delete button
        self.button_backspace = customtkinter.CTkButton(
            self.button_frame,
            text='DEL',
            command=self.backspace_call,
            font = ('Arial', 16),
            fg_color='grey',
            )
        
        self.button_backspace.grid(row=0, column=1, padx=5, pady=5, sticky='nsew')
        
        # Clear All button
        self.button_AC = customtkinter.CTkButton(
            self.button_frame,
            text='AC',
            command=self.AC,
            font = ('Arial', 16),
            fg_color='red'
        )
        
        self.button_AC.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        # Bind keyboard events
        self.bind('<Key>', self.key_press)
        
    def key_press(self, event):
        """Handle keyboard input"""
        self.display.configure('normal')

        # Process different key presses
        if event.char in '0123456789':
            self.input(event.char)
        elif event.char == '+':
            self.input('+')
        elif event.char == '-':
            self.input('-')
        elif event.char == '*':
            self.input('*')
        elif event.char == '/':
            self.input('/')
        elif event.char == '.':
            self.input('.')
        elif event.char == '=' or event.keysym == 'Return':
            self.answer()
        elif event.keysym == 'BackSpace':
            self.backspace_call()
        elif event.keysym == 'Escape':
            self.AC()

        self.display.configure('disabled')

    def input(self, sign):
        """Add input character to display"""
        self.display.configure(state='normal')

        current_text = self.display.get()

        # Clear error message if present
        if 'Ошибка' in current_text:
            self.display.delete(0, 'end')

        self.display.insert('end', str(sign))
        self.display.configure(state='disabled')
    
    def backspace_call(self):
        """Delete last character from display"""
        self.display.configure(state='normal')
        cursor_position = self.display.index('insert')
    
        if cursor_position > 0:
            self.display.delete(cursor_position - 1, cursor_position)
        self.display.configure(state='disabled')
    
    def AC(self):
        """Clear all content from display"""
        self.display.configure(state='normal')
        self.display.delete(0, 'end')
        self.display.configure(state='disabled')
        
    def answer(self):
        """Calculate and display the result of the expression"""
        self.display.configure(state='normal')
        
        expression = self.display.get()

        if expression:
            try:
                # Evaluate the mathematical expression
                result = eval(expression)

                self.display.delete(0, 'end')
                self.display.insert(0, str(result))

            except SyntaxError:
                # Handle syntax errors
                self.display.delete(0, 'end')
                self.display.insert(0, 'Ошибка синтаксиса')

            except ZeroDivisionError:
                # Handle division by zero
                self.display.delete(0, 'end')
                self.display.insert(0, 'Ошибка: деление на ноль')  

        else:
            self.display.insert(0, '')

        self.display.configure('disabled')

if __name__ == "__main__":
    # Create and run the calculator application
    window = Calc()
    window.mainloop()