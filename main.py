import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkbootstrap import Style
from datetime import timedelta

# Create the main window
root = tk.Tk()
root.title("Notes App")
root.geometry("600x500")
style = Style(theme='journal')
style.configure("TNotebook.Tab", font=("TkDefaultFont", 14, "bold"))

notebook = ttk.Notebook(root, style="TNotebook")

#here we are saving the notes
notes = {}
try:
    with open("notes.json", "r") as f:
        notes = json.load(f)
except FileNotFoundError:
    pass

#creating notebook
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

timer_frame = ttk.Frame(root)
timer_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)


timer_label = ttk.Label(timer_frame, text="Set Reminder Time (HH:MM:SS):")
timer_label.pack(pady=5)


reminder_entry = ttk.Entry(timer_frame)
reminder_entry.pack(pady=5)

# timer function
def start_timer():
    reminder_time_str = reminder_entry.get()
    try:
        reminder_time = timedelta(
            hours=int(reminder_time_str.split(":")[0]),
            minutes=int(reminder_time_str.split(":")[1]),
            seconds=int(reminder_time_str.split(":")[2])
        )
    except (ValueError, IndexError):
        messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM:SS format.")
        return

    remaining_time = reminder_time

    def update_timer():
        nonlocal remaining_time
        timer_label.config(text=f"Time remaining: {remaining_time}")
        remaining_time -= timedelta(seconds=1)

        if remaining_time >= timedelta(0):
            root.after(1000, update_timer)
        else:
            timer_label.config(text="Reminder!")
            # уведомление
            messagebox.showinfo("Reminder", "Time is up!")

    update_timer()


start_timer_button = ttk.Button(timer_frame, text="Start Timer", command=start_timer)
start_timer_button.pack(pady=5)

# Adding a new note
def add_note():
    # New tab for the note
    note_frame = ttk.Frame(notebook, padding=10)
    notebook.add(note_frame, text="New Note")

    # Title
    title_label = ttk.Label(note_frame, text="Title:")
    title_label.grid(row=0, column=0, padx=10, pady=10, sticky="W")

    title_entry = ttk.Entry(note_frame, width=40)
    title_entry.grid(row=0, column=1, padx=10, pady=10)

    content_label = ttk.Label(note_frame, text="Content:")
    content_label.grid(row=1, column=0, padx=10, pady=10, sticky="W")

    content_entry = tk.Text(note_frame, width=40, height=10)
    content_entry.grid(row=1, column=1, padx=10, pady=10)

    # Reminder
    reminder_label = ttk.Label(note_frame, text="Reminder Time (HH:MM:SS):")
    reminder_label.grid(row=2, column=0, padx=10, pady=10, sticky="W")

    reminder_entry_note = ttk.Entry(note_frame)
    reminder_entry_note.grid(row=2, column=1, padx=10, pady=10)

    # Saving a note and starting a timer
    def save_note():

        title = title_entry.get()
        content = content_entry.get("1.0", tk.END)
        reminder_time_note_str = reminder_entry_note.get()

        try:
            reminder_time_note = timedelta(
                hours=int(reminder_time_note_str.split(":")[0]),
                minutes=int(reminder_time_note_str.split(":")[1]),
                seconds=int(reminder_time_note_str.split(":")[2])
            )
        except (ValueError, IndexError):
            messagebox.showerror("Invalid Input", "Please enter a valid time in HH:MM:SS format.")
            return

        # Adding the note to the notes dictionary
        notes[title] = {"content": content.strip(), "reminder_time": reminder_time_note_str}

        # Saving the notes dictionary to the file
        with open("notes.json", "w") as f:
            json.dump(notes, f)

        # Adding the note to the notebook
        note_content = tk.Text(notebook, width=40, height=10)
        note_content.insert(tk.END, content)
        notebook.forget(notebook.select())
        notebook.add(note_content, text=f"{title} - Reminder Set")

        # Set the countdown timer for the note
        remaining_time_note = reminder_time_note

        def update_timer_note():
            nonlocal remaining_time_note
            notebook.tab(notebook.select(), text=f"{title} - Time remaining: {remaining_time_note}")
            remaining_time_note -= timedelta(seconds=1)

            if remaining_time_note >= timedelta(0):
                root.after(1000, update_timer_note)
            else:
                notebook.tab(notebook.select(), text=f"{title} - Reminder!")
                # Added messagebox reminder
                messagebox.showinfo("Reminder", f"Time is up for \"{title}!\"")

        update_timer_note()

    # Save-button
    save_button = ttk.Button(note_frame, text="Save", command=save_note, style="secondary.TButton")
    save_button.grid(row=3, column=1, padx=10, pady=10)

#function to load existing notes
def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)

        for title, content in notes.items():
            # Add the note to the notebook
            note_content = tk.Text(notebook, width=40, height=10)
            note_content.insert(tk.END, content)
            notebook.add(note_content, text=title)

    except FileNotFoundError:
        # If the file does not exist, do nothing
        pass


# Calling a funtion
load_notes()


# Function to delete a note
def delete_note():
    current_tab = notebook.index(notebook.select())

    # Get the deleted note's title
    note_title = notebook.tab(current_tab, "text").split(" - ")[0]

    # Confirmation
    confirm = messagebox.askyesno("Delete Note",
                                  f"Are you sure you want to delete {note_title}?")

    if confirm:
        # Removing the note from the notebook
        notebook.forget(current_tab)

        # Removing the note from the notes dictionary
        notes.pop(note_title)

        # Saving the notes dictionary to the file
        with open("notes.json", "w") as f:
            json.dump(notes, f)


# New button
new_button = ttk.Button(root, text="New Note", command=add_note, style="info.TButton")
new_button.pack(side=tk.LEFT, padx=10, pady=10)

delete_button = ttk.Button(root, text="Delete", command=delete_note, style="primary.TButton")
delete_button.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()