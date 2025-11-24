# Task Manager 

## 📌 Project Title
Task Manager – A Command-Line To-Do Application

## 📘 Overview
This project is a simple yet functional command-line task manager built in Python.
It allows users to create, view, update, delete, and store tasks persistently using a JSON file.
The program runs in a loop with a menu-based interface, making it beginner-friendly and easy to use.

## ✨ Features
Add Tasks – Create tasks with title, description, and an optional due date

View Tasks – Display a list of all tasks along with their status (Pending/Completed)

Mark Task as Completed – Update task status to “Completed”

Delete Tasks – Remove tasks by selecting their number

Save Tasks – Save all tasks to a JSON file (tasks.json)

Load Tasks – Load tasks from the JSON file when the program starts

Persistent Storage – Tasks remain saved even after restarting the program

Simple CLI Menu – User-friendly interface for navigating options

## 🛠 Technologies / Tools Used

Python 3.x

Built-in JSON Module – For data serialization

File System Storage – Saves tasks in a JSON file

## 📥 Installation & Running the Project

1. Install Python
Ensure Python 3.x is installed:
python --version

3. Download or Clone the Project
git clone <your-repo-url>
cd <project-folder>
4. Run the Program
Run the script using:
python task_manager.py
(Replace task_manager.py with the actual filename containing your code.)

## 🧪 Instructions for Testing the Application
1. Add a Task
Choose Option 1 from the menu
Enter the task title, description, and an optional due date
Confirm task appears in "View Tasks"
2. View Tasks
Select Option 2 to view all saved tasks
Check task formatting (title, description, due date, status)
3. Mark a Task as Completed
Choose Option 3
Enter the task number you want to mark complete
Re-view tasks to confirm status changed to Completed
4. Delete a Task
Choose Option 4
Enter the task number
Task should disappear from the list
5. Save Tasks
Choose Option 5
Confirm tasks.json is updated
6. Load Tasks
Restart the program
The tasks should automatically load from tasks.json
