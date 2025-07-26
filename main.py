import tkinter as tk
import random

# --- Window setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x800")
root.configure(bg="#576580")  

# --- Task list ---
tasks = []

# --- Functions ---
def update_listbox():
    lb_tasks.delete(0, "end")
    for task in tasks:
        lb_tasks.insert("end", task)

def add_task():
    task = txt_input.get()
    if task:
        tasks.append(task)
        update_listbox()
        lbl_display.config(text=f"Added: {task}", fg="#A3BE8C")
        txt_input.delete(0, "end")
    else:
        lbl_display.config(text="⚠️ Enter a task!", fg="#BF616A")

def del_one():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
        update_listbox()
        lbl_display.config(text=f"Removed: {task}", fg="#D08770")

def del_all():
    global tasks
    tasks = []
    update_listbox()
    lbl_display.config(text="All tasks deleted!", fg="#BF616A")

def sort_asc():
    tasks.sort()
    update_listbox()
    lbl_display.config(text="Sorted A–Z", fg="#88C0D0")

def sort_desc():
    tasks.sort(reverse=True)
    update_listbox()
    lbl_display.config(text="Sorted Z–A", fg="#88C0D0")

def choose_random():
    if tasks:
        task = random.choice(tasks)
        lbl_display.config(text=f"🎲 Do this: {task}", fg="#EBCB8B")
    else:
        lbl_display.config(text="No tasks!", fg="#BF616A")

def num_tasks():
    lbl_display.config(text=f"📋 {len(tasks)} task(s)", fg="#B48EAD")

# --- Title ---
lbl_title = tk.Label(root, text="☑️  My To-Do List", font=("Segoe UI", 20, "bold"), bg="#2E3440", fg="#ECEFF4")
lbl_title.pack(pady=(20, 10))

# --- Feedback display ---
lbl_display = tk.Label(root, text="", font=("Segoe UI", 12), bg="#2E3440", fg="#ECEFF4")
lbl_display.pack(pady=(0, 10))

# --- Entry box ---
txt_input = tk.Entry(root, font=("Segoe UI", 12), width=30)
txt_input.pack(pady=5)

btn_add = tk.Button(root, text="Add Task", command=add_task, bg="#88C0D0", fg="black", width=20)
btn_add.pack(pady=5)

# --- Listbox ---
lb_tasks = tk.Listbox(root, width=40, height=10, font=("Segoe UI", 12))
lb_tasks.pack(pady=10)

# --- Buttons section ---
button_style = {"width": 20, "bg": "#4C566A", "fg": "white", "activebackground": "#434C5E"}

tk.Button(root, text="Delete Selected", command=del_one, **button_style).pack(pady=2)
tk.Button(root, text="Delete All", command=del_all, **button_style).pack(pady=2)
tk.Button(root, text="Sort A–Z", command=sort_asc, **button_style).pack(pady=2)
tk.Button(root, text="Sort Z–A", command=sort_desc, **button_style).pack(pady=2)
tk.Button(root, text="Pick Random", command=choose_random, **button_style).pack(pady=2)
tk.Button(root, text="Count Tasks", command=num_tasks, **button_style).pack(pady=2)

# --- Initial Load ---
update_listbox()

# --- Start App ---
root.mainloop()
