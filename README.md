# Task Manager

## Description
This is a simple **Task Manager** application developed using Python and Tkinter. It allows users to manage tasks efficiently by adding, editing, viewing, and deleting tasks. The tasks are stored persistently in a JSON file, so they remain available even after the application is closed and reopened.

## Features
- Add new tasks with details such as title, category, description, due date, and priority.
- Edit existing tasks.
- Delete tasks from the list.
- View all tasks in a categorized list.
- Save tasks to a JSON file for persistent storage.
- Automatically load saved tasks upon application startup.

## Requirements
- Python 3.x
- Tkinter (built-in with Python)
- OS with support for Python and Tkinter (Windows, macOS, or Linux)

## Installation
1. Clone or download the project files from the repository.
2. Ensure Python is installed on your system. You can verify it by running:
   ```bash
   python --version
   ```
3. (Optional) Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install any required dependencies (if needed).

## How to Run
1. Navigate to the directory where the project is saved.
2. Run the application using:
   ```bash
   python project.py
   ```

## Files
- **`project.py`**: The main Python file containing the application logic.
- **`tasks.json`**: The JSON file used for storing task data persistently.

## Usage
1. Launch the application.
2. Use the input fields to add new tasks by providing all necessary details (Title, Category, Details, Due Date, Priority).
3. Click the appropriate buttons:
   - **Add Task**: Adds the task to the list.
   - **Edit Task**: Select a task from the list, modify the fields, and save changes.
   - **Delete Task**: Removes the selected task from the list.
   - **View Tasks**: Refreshes and displays all tasks in the listbox.
   - **Save**: Saves the current tasks to the `tasks.json` file.
4. Close the application; tasks will be automatically saved.

## Project Structure
```
.
|-- project.py      # Main application file
|-- tasks.json       # JSON file for storing tasks persistently
```

## Contributing
Feel free to fork this repository and make improvements. Contributions are welcome!


## Contact
For questions or suggestions, please contact:
- **Name**: Angela Jeptoo
- **Email**: angelacheptoo23@gmail.com

