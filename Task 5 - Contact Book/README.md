# 📒 Contact Book using Python & Tkinter

A simple GUI-based **Contact Book Application** built with **Python** and **Tkinter**.  
Easily add and view contacts with names, phone numbers, emails, and addresses.

## 🚀 Features

- Add new contacts with:
  - Name (required)
  - Phone (required)
  - Email
  - Address
- View added contacts in a list
- Input validation for required fields
- Clean and intuitive interface

## 🧱 File Structure

📁 ContactBook
<br>
contact_book.py # Main Python script
<br>
README.md # Project documentation


## 💻 How to Run

1. Ensure Python is installed on your system.
2. Save the code in a file named `contact_book.py`.
3. Open a terminal and run:

```bash
python contact_book.py
```

## 🖼️ App Overview
Input Fields:

Name, Phone, Email, Address

Button:

Add Contact – Adds the contact to the list

Listbox:

Displays added contacts as Name - Phone

## 🧠 How It Works
Contacts are stored as a list of tuples: (name, phone, email, address)

add_contact():

Validates required fields

Adds contact to the list

Updates the display

update_listbox():

Refreshes the contact list

clear_entries():

Clears input fields after each addition

## 📌 Note
Name and Phone are mandatory fields.

Data is stored in-memory; it is not saved permanently.

## 📜 License
This project is free for educational and personal use.


