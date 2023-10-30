import tkinter as tk
from tkinter import ttk, messagebox

# List to store patient names
patient_list = []

def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            # Duplicate Check
            full_name = f"{firstname} {lastname}"
            if full_name in patient_list:
                messagebox.showwarning("Duplicate Record", f"The record for {full_name} already exists.")
            else:
                # Store the name in the list
                patient_list.append(full_name)

                gender = title_combobox.get()
                age = age_spinbox.get()
                nationality = nationality_combobox.get()

                # User's History
                Chronic_status = Chronic_status_var.get()
                previous = Previous_field_entry.get()
                current = Current_field_entry.get()

                # Course info
                registration_status = reg_status_var.get()
                numcourses = numcourses_spinbox.get()
                numduration = numduration_spinbox.get()

                messagebox.showinfo("Success", "Patient's Data Is Saved successfully.")

                # Update the listbox
                update_patient_listbox()
        else:
            messagebox.showwarning("Error", "First name and last name are required.")
    else:
        messagebox.showwarning("Error", "You have not accepted the terms")

    # Clear input fields
    first_name_entry.delete(0, "end")
    last_name_entry.delete(0, "end")
    title_combobox.set("")  
    age_spinbox.delete(0, "end")
    nationality_combobox.set("")  
    Chronic_status_var.set("No")
    Previous_field_entry.delete(0, "end")
    Current_field_entry.delete(0, "end")
    reg_status_var.set("No")
    numcourses_spinbox.delete(0, "end")
    numduration_spinbox.delete(0, "end")
    accept_var.set("Not Accepted")


def update_patient_listbox():
    patient_listbox.delete(0, tk.END)
    for name in patient_list:
        patient_listbox.insert(tk.END, name)

def delete_patient():
    selected_index = patient_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Select a Record", "Please select a record to delete.")
        return

    index = int(selected_index[0])
    deleted_name = patient_list[index]
    del patient_list[index]
    update_patient_listbox()
    messagebox.showinfo("Record Deleted", f"The record for {deleted_name} has been deleted.")


def search_patient():
    search_name = search_entry.get()
    if not search_name:
        messagebox.showwarning("No Search Criteria", "Please type a name to search for.")
        return
    
    found_indices = [i for i, name in enumerate(patient_list) if search_name.lower() in name.lower()]
    
    if found_indices:
        patient_listbox.selection_clear(0, tk.END)
        
        for index in found_indices:
            patient_listbox.select_set(index)
        
        messagebox.showinfo("Search Results", f"Found {len(found_indices)} record(s) matching '{search_name}'.")
    else:
        messagebox.showinfo("Search Results", f"No records found matching '{search_name}'.")


window = tk.Tk()
window.title("Patients Data Entry Form")
window.configure(bg='#333333')

frame = tk.Frame(window, bg='#333333')
frame.pack()

# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="User Information", bg='#333333', fg="#FFFFFF", font=("Arial", 16)
)
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tk.Label(user_info_frame, text="First Name", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
last_name_label.grid(row=0, column=1)

first_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Gender", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
title_combobox = ttk.Combobox(user_info_frame, values=["Male", "Female", "Trans"])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tk.Label(user_info_frame, text="Age", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
age_spinbox = tk.Spinbox(user_info_frame, from_=6, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tk.Label(user_info_frame, text="Native ", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
nationality_combobox = ttk.Combobox(user_info_frame, values=[
    "Africa",
    "Antarctica",
    "Asia",
    "Europe",
    "North America",
    "Oceania",
    "South America",
])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
history_frame = tk.LabelFrame(frame, text="User's Medical History", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
history_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

Chronic_status_var = tk.StringVar(value="No")
Chronic_check = tk.Checkbutton(history_frame, bg='#333333', selectcolor="#FF3399", fg="#FFFFFF", font=("Arial", 11), text="Any Chronic disease",
                                   variable=Chronic_status_var, onvalue="Yes", offvalue="No")

Chronic_check.grid(row=1, column=0, padx=5)

Previous_field_label = tk.Label(history_frame, text="Previously Diagnosed", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
Previous_field_label.grid(row=0, column=1, padx=15, pady=5)
Current_field_label = tk.Label(history_frame, text="Currently Diagnosed", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
Current_field_label.grid(row=0, column=2, padx=15, pady=5)

Previous_field_entry = tk.Entry(history_frame)
Current_field_entry = tk.Entry(history_frame)
Previous_field_entry.grid(row=1, column=1, padx=10, pady=10)
Current_field_entry.grid(row=1, column=2, padx=10, pady=5)

for widget in history_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tk.LabelFrame(frame, text="Registration Status", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
courses_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

reg_status_var = tk.StringVar(value="No")
registered_check = tk.Checkbutton(courses_frame, bg='#333333', selectcolor="#FF3399", fg="#FFFFFF", font=("Arial", 11), text="Currently Registered",
                                   variable=reg_status_var, onvalue="Yes", offvalue="No")

registered_check.grid(row=1, column=0)

numcourses_label = tk.Label(courses_frame, text= "Completed Courses", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
numcourses_spinbox = tk.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numduration_label = tk.Label(courses_frame, text="Duration [Months]", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
numduration_spinbox = tk.Spinbox(courses_frame, from_=0, to="infinity")
numduration_label.grid(row=0, column=2)
numduration_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
terms_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)

accept_var = tk.StringVar(value="Not Accepted")
terms_check = tk.Checkbutton(terms_frame, bg='#333333', selectcolor="#FF3399", fg="#FFFFFF", font=("Arial", 13), text="I accept the terms and conditions.",
                              variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tk.Button(frame, bg='#FF3399', text="Enter data", command=enter_data, fg="#FFFFFF", font=("Arial", 16))
button.grid(row=4, column=0, sticky="news", padx=20, pady=10)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
modify_frame = tk.LabelFrame(frame, text="Information Modification", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
modify_frame.grid(row=5, column=0, sticky="news", padx=10, pady=10)

# Delete button for removing selected patient
delete_label = tk.Label(modify_frame, text="Select and Delete Record", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
delete_label.grid(row=1, column=0, padx=20, pady=(10, 0), sticky="w")

# Listbox to display patient names
patient_listbox = tk.Listbox(modify_frame, selectmode=tk.SINGLE, activestyle="none")
patient_listbox.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

# Delete button for removing selected patient
delete_button = tk.Button(modify_frame, bg='#FF3399', text="Delete", command=delete_patient, fg="#FFFFFF", font=("Arial", 16))
delete_button.grid(row=2, column=1, padx=(0, 20), pady=10, sticky="n")

# search box and search button
search_label = tk.Label(modify_frame, text="Search by Name", bg='#333333', fg="#FFFFFF", font=("Arial", 11))
search_entry = tk.Entry(modify_frame, width=30)
search_button = tk.Button(modify_frame, bg='#FF3399', text="Search", command=search_patient, fg="#FFFFFF", font=("Arial", 16))

search_label.grid(row=0, column=0, padx=5)
search_entry.grid(row=0, column=1, padx=5)
search_button.grid(row=0, column=2, padx=5)

window.mainloop()
