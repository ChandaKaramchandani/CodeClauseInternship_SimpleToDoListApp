import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Simple To-Do List App")
root.geometry("400x450")
root.configure(bg="lightyellow")

tasks = []

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        del tasks[selected_task]
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

def mark_completed():
    try:
        selected_task = listbox.curselection()[0]
        task = tasks[selected_task]
        tasks[selected_task] = f"✔️ {task}"
        update_listbox()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark completed!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

label = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"), bg="lightyellow")
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30)
entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task, width=15, bg="lightgreen")
add_button.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 12), width=35, height=10)
listbox.pack(pady=10)

complete_button = tk.Button(root, text="Mark as Completed", command=mark_completed, width=20, bg="lightblue")
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, width=15, bg="tomato")
delete_button.pack(pady=5)

root.mainloop()
