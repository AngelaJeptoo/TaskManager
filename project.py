from tkinter import (
    Tk,
    Label,
    Entry,
    Button,
    Listbox,
    Scrollbar,
    END,
    Toplevel,
    messagebox,
)
import json
import os


class Task:
    def __init__(self, title, category, details, due_date, priority):
        self.title = title
        self.category = category
        self.details = details
        self.due_date = due_date
        self.priority = priority


class TaskManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Set window size and position
        window_width = 600
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Task input fields
        self.title_label = Label(root, text="Title:", fg="blue")
        self.title_entry = Entry(root)
        self.category_label = Label(root, text="Category:", fg="blue")
        self.category_entry = Entry(root)
        self.details_label = Label(root, text="Details:", fg="blue")
        self.details_entry = Entry(root)
        self.due_date_label = Label(root, text="Due Date:", fg="blue")
        self.due_date_entry = Entry(root)
        self.priority_label = Label(root, text="Priority:", fg="blue")
        self.priority_entry = Entry(root)

        # Task listbox and scrollbar
        self.task_listbox = Listbox(root, height=10, width=50)
        self.scrollbar = Scrollbar(root)

        # Buttons
        self.add_button = Button(
            root, text="Add Task", command=self.add_task, bg="green", fg="white"
        )
        self.edit_button = Button(
            root, text="Edit Task", command=self.edit_task, bg="orange", fg="white"
        )
        self.delete_button = Button(
            root, text="Delete Task", command=self.delete_task, bg="red", fg="white"
        )
        self.view_button = Button(
            root, text="View Tasks", command=self.display_tasks, bg="blue", fg="white"
        )
        self.save_button = Button(
            root, text="Save", command=self.save_tasks, bg="purple", fg="white"
        )

        # Grid layout
        self.title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.title_entry.grid(row=0, column=1, padx=5, pady=5)
        self.category_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.category_entry.grid(row=1, column=1, padx=5, pady=5)
        self.details_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.details_entry.grid(row=2, column=1, padx=5, pady=5)
        self.due_date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.due_date_entry.grid(row=3, column=1, padx=5, pady=5)
        self.priority_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.priority_entry.grid(row=4, column=1, padx=5, pady=5)

        self.task_listbox.grid(row=0, column=2, rowspan=5, padx=5, pady=5, sticky="nsew")
        self.scrollbar.grid(row=0, column=3, rowspan=5, sticky="ns")

        self.add_button.grid(row=5, column=0, padx=5, pady=5)
        self.edit_button.grid(row=5, column=1, padx=5, pady=5)
        self.delete_button.grid(row=5, column=2, padx=5, pady=5)
        self.view_button.grid(row=6, column=0, padx=5, pady=5)
        self.save_button.grid(row=6, column=1, padx=5, pady=5)

        # Configure scrollbar to work with the task listbox
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Task list
        self.tasks = []

        # Load tasks from file
        self.load_tasks()

        # Handle application exit
        self.root.protocol("WM_DELETE_WINDOW", self.exit_application)

    def add_task(self):
        title = self.title_entry.get()
        category = self.category_entry.get()
        details = self.details_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if title and category and details and due_date and priority:
            self.tasks.append(Task(title, category, details, due_date, priority))
            self.clear_entry_fields()
            self.display_tasks()
        else:
            messagebox.showwarning("Incomplete Fields", "Please fill in all fields.")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks[selected_index[0]]
            task.title = self.title_entry.get() or task.title
            task.category = self.category_entry.get() or task.category
            task.details = self.details_entry.get() or task.details
            task.due_date = self.due_date_entry.get() or task.due_date
            task.priority = self.priority_entry.get() or task.priority
            self.display_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to edit.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.tasks.pop(selected_index[0])
            self.display_tasks()
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def display_tasks(self):
        self.task_listbox.delete(0, END)
        for task in self.tasks:
            self.task_listbox.insert(
                END, f"{task.title} | {task.category} | {task.due_date} | {task.priority}"
            )

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump([task.__dict__ for task in self.tasks], file)
        messagebox.showinfo("Save Successful", "Tasks saved.")

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                for task_data in json.load(file):
                    self.tasks.append(
                        Task(
                            task_data["title"],
                            task_data["category"],
                            task_data["details"],
                            task_data["due_date"],
                            task_data["priority"],
                        )
                    )
                self.display_tasks()

    def exit_application(self):
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = TaskManagerGUI(root)
    root.mainloop()
