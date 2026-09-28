## Problem Statement
Managing books manually in a library can be time-consuming and may lead to errors while keeping track of available and issued books. It can also be difficult to quickly find a book based on its name, genre, or author.\
The Library Management System is a Python-based program designed to simplify basic library operations. It allows users to donate books, view all books in the library, issue books, search for books, and return books. The system maintains the availability status of each book so that users can easily know whether a book is available or already issued.\
The main objective of this project is to provide a simple and user-friendly way to manage basic library activities using Python.
## Scope of the Project
The scope of this project is to manage the basic operations of a small library through a simple Python program.\
The system can:\
Store information about books such as book name, genre, author, and availability.\
Add new books to the library through the donation feature.\
Display all books available in the library.\
Issue books to users and change their availability status.\
Return issued books and make them available again.\
Search for books by book name, genre, or author.\
Provide a simple menu-driven interface for users.\
The current project is intended for basic library management. It does not include advanced features such as databases, online book reservations, login systems, fine calculation, or automatic due-date management.
## Target Users
The main target users of this project are:\
Students — to search for and issue books easily.\
Teachers — to manage and access library books.\
Librarians — to perform basic book management operations.\
Small libraries — where a simple system is sufficient for maintaining book records.\
Beginners learning Python — as the project demonstrates the use of lists, tuples, functions, loops, conditional statements, and user input.
## High-Level Features
### 1. Donate Book
Users can add a new book to the library by entering its book name, genre, and author. The newly added book is automatically marked as Available.
### 2. View Total Books
The system displays the details of all books currently stored in the library.
### 3. Issue Book
Users can enter the name of a book they want to borrow. If the book is available, its status is changed to Not Available.
### 4. Search Books
The system provides three search options:\
Search by Book Name\
Search by Genre\
Search by Author\
This makes it easier to find a particular book or books belonging to a specific category or author.
### 5. Return Book
Users can return a previously issued book. The status of the book is changed back to Available.
### 6. Menu-Driven Interface
The program provides a simple menu through which users can select different library operations.
### 7. Book Availability Tracking
The system keeps track of whether each book is Available or Not Available, helping users determine whether a book can currently be issued.
