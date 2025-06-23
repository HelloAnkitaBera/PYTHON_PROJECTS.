import tkinter as tk

def press(num):
    current = entry_var.get()
    entry_var.set(current + str(num))

def clear():
    entry_var.set("")

def equal():
    try:
        result = str(eval(entry_var.get()))
        entry_var.set(result)
    except:
        entry_var.set("Error")

def clear_one():
   
    current_text = entry.get() 
    entry.delete(0, 'end')
    entry.insert(0, current_text[:-1])

def percent():
    try:
        current = entry.get()
        result = str(eval(current) / 100)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, 'Error')
import math
def sqrt_func():
            try:
                current = float(entry.get())
                result = str(math.sqrt(current))
                entry.delete(0, tk.END)
                entry.insert(0, result)
            except:
                entry.delete(0, tk.END)
                entry.insert(0, 'Error')



# GUI setup
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("295x510")
root.configure(bg="#18212E")  # Dark gray or any hex color

# root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=20, insertwidth=2, width=15, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=20)



frame = tk.Frame(root, bg='#00ADB5', padx=20, pady=20)
frame.grid(row=1, column=0, columnspan=4)


buttons = [
    ('AC', 1, 0), ('C', 1, 1), ('√', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('%', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3),

]


for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1

    # Set button colors based on button type
    if text in {'+', '-', '*', '/'}:
        bg_color = '#FFA500'   
        fg_color = 'white'
    elif text in {'C', 'AC', '√'}:
        bg_color = '#FF6347'   
        fg_color = 'white'
    elif text == '%':
        bg_color = "#ED8AA4"  
        fg_color = 'black'    
    elif text == '=':
        bg_color = '#32CD32'  
        fg_color = 'white'
    else:
        bg_color = "#E5F50E"  
        fg_color = 'black'

    if text == '=':
        btn = tk.Button(root, text=text, padx=18, pady=20, font=('Arial', 18), command=equal, bg=bg_color, fg=fg_color)
    elif text == '%':
        btn = tk.Button(root, text=text, padx=16, pady=20, font=('Arial', 18), command=percent, bg=bg_color, fg=fg_color)
    elif text == '√':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=sqrt_func, bg=bg_color, fg=fg_color)
    elif text == 'AC':
        btn = tk.Button(root, text=text, padx=12, pady=20, font=('Arial', 18), command=clear, bg=bg_color, fg=fg_color)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=clear_one, bg=bg_color, fg=fg_color)
    elif text == '.':
        btn = tk.Button(root, text=text, padx=22, pady=20, font=('Arial', 18), command=lambda: press('.'), bg=bg_color, fg=fg_color)
    elif text == '+':
        btn = tk.Button(root, text=text, padx=18, pady=20, font=('Arial', 18), command=lambda t=text: press(t), bg=bg_color, fg=fg_color)
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: press(t), bg=bg_color, fg=fg_color)
    btn.grid(row=row, column=col, columnspan=colspan)

root.mainloop()