import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("1000x1000")
root.configure(bg="#2e2e2e")  


entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='solid', justify='right', bg="#1e1e1e", fg="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(symbol):
    entry.insert(tk.END, symbol)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

number_bg = "#3e3e3e"
operator_bg = "#fe9241"
equal_bg = "#00cc66"
clear_bg = "#cc0000"


buttons = [
    ('7', 1, 0, number_bg), ('8', 1, 1, number_bg), ('9', 1, 2, number_bg), ('/', 1, 3, operator_bg),
    ('4', 2, 0, number_bg), ('5', 2, 1, number_bg), ('6', 2, 2, number_bg), ('*', 2, 3, operator_bg),
    ('1', 3, 0, number_bg), ('2', 3, 1, number_bg), ('3', 3, 2, number_bg), ('-', 3, 3, operator_bg),
    ('0', 4, 0, number_bg), ('.', 4, 1, number_bg), ('=', 4, 2, equal_bg), ('+', 4, 3, operator_bg),
]

for (text, row, col, color) in buttons:
    action = calculate if text == '=' else lambda t=text: button_click(t)
    tk.Button(root, text=text, width=5, height=2, font=('Arial', 18),
              bg=color, fg="white", activebackground="#505050", command=action).grid(row=row, column=col, padx=1, pady=1)


tk.Button(root, text='C', width=22, height=2, font=('Arial', 18),
          bg=clear_bg, fg="white", activebackground="#800000", command=clear).grid(row=5, column=0, columnspan=4, pady=10)


root.mainloop()
