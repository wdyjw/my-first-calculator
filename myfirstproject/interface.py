import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget('text')
    global current_input, last_result

    if text == "=":
        try:
            expression = current_input.get()
            # 安全验证
            safe_chars = "0123456789.+-*/%() "
            if all(char in safe_chars for char in expression):
                result = eval(expression)
                last_result = result
                current_input.set(str(result))
            else:
                messagebox.showerror("错误", "包含非法字符")
            return
        except Exception as e:
            messagebox.showwarning('错误', f'计算失败： {str(e)}')
    elif text == "C":
        current_input.set("")
    elif text == "←":
        current_input.set(current_input.get()[:-1])
    else:
        current_input.set(current_input.get() + text)


# 主窗口设置
root = tk.Tk()
root.title('简易计算器')
root.geometry("300x400")
current_input = tk.StringVar()
last_result = None

# 显示框
entry = tk.Entry(root, textvar=current_input, font=("Aril", 20), bd=10, justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('.', '0', '=', '+'),
    ('**', '%', '←', 'C'),
]

frame = tk.Frame(root)
frame.pack(expand=True, fill=tk.BOTH)

for row_index, row in enumerate(buttons):
    for col_idx, btn_text in enumerate(row):
        btn = tk.Button(frame, text=btn_text, font=("Aril", 15), relief="groove")
        btn.grid(row=row_index, column=col_idx, sticky=tk.NSEW, padx=2, pady=2)
        btn.bind('<Button-1>', on_click)
        frame.columnconfigure(col_idx, weight=1)
    frame.rowconfigure(row_index, weight=1)

# 添加键盘支持
def on_key(event):
    key = event.char
    if key in "0123456789+-*/%.**":
        current_input.set(current_input.get() + key)
    elif event.keysym == 'Return' or key == '=':
        event.widget.event_generate("<Button-1>", x=0, y=0)
    elif event.keysym == 'BackSpace' or key == "\x08":
        current_input.set(current_input.get()[:-1])
    elif event.keysym == 'Escape' or key == "C":
        current_input.set("")

entry.bind('Key>', on_key)
root.bind("<Key>", on_key)


root.mainloop()


