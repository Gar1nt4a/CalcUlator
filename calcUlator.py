import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("КалькУлятор")
        self.window.geometry("320x450")
        self.window.resizable(False, False)

        self.current_input = ""
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.operator = None
        self.first_operand = None

        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.window)
        display_frame.pack(expand=True, fill="both", padx=10, pady=10)

        display = tk.Entry(display_frame, textvariable=self.result_var,
                           font=('Arial', 20), justify='right', state='readonly')
        display.pack(expand=True, fill="both", ipady=10)

        buttons_frame = tk.Frame(self.window)
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]

        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    if text == '0':
                        btn = tk.Button(buttons_frame, text=text, font=('Arial', 16),
                                        command=lambda t=text: self.button_click(t))
                        btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                    else:
                        btn = tk.Button(buttons_frame, text=text, font=('Arial', 16),
                                        command=lambda t=text: self.button_click(t))
                        btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        backspace_btn = tk.Button(buttons_frame, text='⌫', font=('Arial', 16),
                                  command=lambda: self.button_click('⌫'))
        backspace_btn.grid(row=4, column=3, sticky="nsew", padx=2, pady=2)

        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)

    def button_click(self, value):
        try:
            if value.isdigit() or value == '.':
                self.input_number(value)
            elif value in ['+', '-', '*', '/']:
                self.input_operator(value)
            elif value == '=':
                self.calculate()
            elif value == 'C':
                self.clear()
            elif value == '⌫':
                self.backspace()
            elif value == '±':
                self.plus_minus()
            elif value == '%':
                self.percentage()
        except Exception as e:
            self.result_var.set("Ошибка!")

    def input_number(self, num):
        if num == '.' and '.' in self.current_input:
            return

        if self.current_input == "0" and num != '.':
            self.current_input = num
        else:
            self.current_input += num

        self.result_var.set(self.current_input)

    def input_operator(self, op):
        if self.current_input:
            if self.first_operand is None:
                self.first_operand = float(self.current_input)
            elif self.operator:
                self.calculate()

            self.operator = op
            self.current_input = ""

    def calculate(self):
        if self.first_operand is not None and self.operator and self.current_input:
            second_operand = float(self.current_input)

            try:
                if self.operator == '+':
                    result = self.first_operand + second_operand
                elif self.operator == '-':
                    result = self.first_operand - second_operand
                elif self.operator == '*':
                    result = self.first_operand * second_operand
                elif self.operator == '/':
                    if second_operand == 0:
                        raise ZeroDivisionError("На ноль делить нельзя!")
                    result = self.first_operand / second_operand

                if result == int(result):
                    result = int(result)

                self.result_var.set(str(result))
                self.current_input = str(result)
                self.first_operand = result
                self.operator = None

            except ZeroDivisionError:
                self.result_var.set("Деление на 0!")
                self.clear()
            except Exception:
                self.result_var.set("Ошибка!")
                self.clear()

    def clear(self):
        self.current_input = ""
        self.result_var.set("0")
        self.operator = None
        self.first_operand = None

    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
            if not self.current_input:
                self.current_input = "0"
            self.result_var.set(self.current_input)

    def plus_minus(self):
        if self.current_input and self.current_input != "0":
            if self.current_input[0] == '-':
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.result_var.set(self.current_input)

    def percentage(self):
        if self.current_input:
            try:
                value = float(self.current_input) / 100
                if value == int(value):
                    value = int(value)
                self.current_input = str(value)
                self.result_var.set(self.current_input)
            except:
                self.result_var.set("Ошибка!")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()