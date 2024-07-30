import tkinter as tk

def click(event):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(event.widget.cget("text")))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')


root = tk.Tk()
root.title("Calculator")


window_width = 400
window_height = 600
center_window(root, window_width, window_height)

root.configure(bg='light gray')


frame = tk.Frame(root, bg='white', bd=10)
frame.place(relx=0.5, rely=0.5, anchor='center')


entry = tk.Entry(frame, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)


buttons = [
    ('7', 'light blue'), ('8', 'light blue'), ('9', 'light blue'), ('/', 'orange'),
    ('4', 'light blue'), ('5', 'light blue'), ('6', 'light blue'), ('*', 'orange'),
    ('1', 'light blue'), ('2', 'light blue'), ('3', 'light blue'), ('-', 'orange'),
    ('0', 'light blue'), ('.', 'light blue'), ('=', 'green'), ('+', 'orange')
]


row_val = 1
col_val = 0
for (button, color) in buttons:
    btn = tk.Button(frame, text=button, font=('Arial', 18), height=2, width=4, bg=color)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    if button == '=':
        btn.bind("<Button-1>", lambda event: calculate())
    elif button == 'C':
        btn.bind("<Button-1>", lambda event: clear())
    else:
        btn.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


clear_btn = tk.Button(frame, text='C', font=('Arial', 18), height=2, width=4, bg='red', command=clear)
clear_btn.grid(row=row_val, column=0, columnspan=4, sticky='we', padx=5, pady=5)


root.mainloop()
