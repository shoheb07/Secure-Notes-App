# Secure-Notes-App
Developed a Secure Notes App using Python, Tkinter, and the Cryptography library to provide encrypted note storage and password-protected access. Implemented AES-based symmetric encryption and secure file handling techniques to ensure data confidentiality and enhance cybersecurity practices.

# Secure Notes App

## Overview

Secure Notes App is a desktop application developed using Python that allows users to securely store and manage personal notes. The application encrypts note contents before saving them, ensuring confidentiality and protection against unauthorized access.

The project demonstrates concepts from cybersecurity, cryptography, file handling, and GUI development.


## Features

- Create and save notes securely
- AES encryption using Fernet
- Password-protected access
- View encrypted notes
- Edit and delete notes
- Simple graphical interface
- Local storage support


## Technologies Used

- Python
- Tkinter
- Cryptography Library
- File Handling

Project Structure

Secure-Notes-App/
│
├── secure_notes.py
├── key.key
├── notes.dat
└── README.md

Working Principle
User writes a note.
A secret encryption key is generated.
The note is encrypted using AES-based Fernet encryption.
Encrypted data is stored locally.
When requested, the note is decrypted and displayed

