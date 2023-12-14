# Notes App

## Description
This Python script implements a simple Notes App using the Tkinter library for the graphical user interface. The application allows users to create, edit, delete, and set reminders for notes. Notes are saved in a JSON file (**notes.json**), and reminders can be set with countdown timers.
## Features
### 1. Notebook Interface
- The main window features a notebook interface that allows users to switch between different notes.
- Each note is represented as a separate tab in the notebook.
### 2. Timer Functionality
- Users can set reminders for each note by specifying a time in the HH:MM:SS format.
- Countdown timers are displayed for notes with reminders, and users are alerted when the time is up.
### 3. Adding New Notes
- Users can add new notes by clicking the "New Note" button.
- For each note, users can provide a title, content, and set a reminder time.
### 4. Saving and Loading
- Notes are saved in a **notes.json** file to persist data between sessions.
- Existing notes are loaded when the application starts.
### 5. Deleting Notes
- Users can delete a note by selecting it and clicking the "Delete" button.
- A confirmation dialog is displayed before deleting a note.
## Dependencies
- Python 3.x
- Tkinter
- ttkbootstrap
- JSON (built-in)
- datetime (built-in)
- messagebox (built-in)
## How to Run
1. Ensure you have Python installed on your system.
2. Install dependencies:
   ```bash
   pip install ttkbootstrap
   
3. Run the script:
   ```bash
   python notes_app.py
   
## Usage
### 1. Adding a New Note:
- Click the "New Note" button to create a new note.
- Enter the title, content, and reminder time (if needed).
- Click the "Save" button to save the note and start the countdown timer.
### 2. Deleting a Note:
- Select the note you want to delete.
- Click the "Delete" button.
- Confirm the deletion in the dialog box.
### 3. Setting a Reminder:
- When adding or editing a note, enter the desired reminder time in the "Reminder Time" field using the HH:MM:SS format.
### 4. Closing the Application:
- Click the close button (X) on the main window to exit the application.
## File Structure
- **notes_app.py**: Main Python script containing the Notes App code.
- **notes.json**: JSON file used to store notes data.
## Note
- The application uses the **ttkbootstrap** library for styling the Tkinter interface with a Bootstrap theme.
- Make sure to have the required dependencies installed before running the script.


Feel free to explore, modify, and enhance the code according to your needs. Enjoy using the Notes App!

