import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("book_shop.db")

# Create a cursor object to insert records and create the table
cursor = connection.cursor()

# Create a table for books
table_info = """
CREATE TABLE IF NOT EXISTS BOOK (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TITLE VARCHAR(100),
    AUTHOR VARCHAR(50),
    CATEGORY VARCHAR(50),
    PRICE REAL,
    STOCK INT
);
"""

cursor.execute(table_info)

# Sample data for inserting records
book_records = [
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 10.99, 20),
    ('1984', 'George Orwell', 'Dystopian', 8.99, 15),
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 7.99, 25),
    ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 9.99, 18),
    ('Pride and Prejudice', 'Jane Austen', 'Romance', 6.99, 30),
    ('The Hobbit', 'J.R.R. Tolkien', 'Fantasy', 12.99, 12),
    ('Moby Dick', 'Herman Melville', 'Adventure', 11.99, 10),
    ('War and Peace', 'Leo Tolstoy', 'Historical Fiction', 15.99, 5),
    ('The Odyssey', 'Homer', 'Epic', 13.99, 7),
    ('Crime and Punishment', 'Fyodor Dostoevsky', 'Psychological', 14.99, 8),
    ('Brave New World', 'Aldous Huxley', 'Dystopian', 10.49, 14),
    ('The Grapes of Wrath', 'John Steinbeck', 'Fiction', 9.49, 9),
    ('Wuthering Heights', 'Emily Brontë', 'Classic', 8.49, 16),
    ('Jane Eyre', 'Charlotte Brontë', 'Classic', 7.49, 22),
    ('The Picture of Dorian Gray', 'Oscar Wilde', 'Classic', 6.49, 19),
    ('The Lord of the Rings', 'J.R.R. Tolkien', 'Fantasy', 29.99, 3),
    ('Fahrenheit 451', 'Ray Bradbury', 'Dystopian', 8.99, 11),
    ('The Bell Jar', 'Sylvia Plath', 'Fiction', 10.99, 17),
    ('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', 'Science Fiction', 9.99, 20),
    ('The Road', 'Cormac McCarthy', 'Post-Apocalyptic', 12.99, 10),
    ('Siddhartha', 'Hermann Hesse', 'Philosophical', 7.99, 24),
    ('Catch-22', 'Joseph Heller', 'Satirical', 8.49, 15),
    ('Little Women', 'Louisa May Alcott', 'Classic', 6.99, 21),
    ('Anne of Green Gables', 'L.M. Montgomery', 'Children', 9.49, 13),
    ('The Secret Garden', 'Frances Hodgson Burnett', 'Children', 5.99, 28),
    ('The Chronicles of Narnia', 'C.S. Lewis', 'Fantasy', 10.49, 14),
    ('A Tale of Two Cities', 'Charles Dickens', 'Historical Fiction', 11.49, 8),
    ('Les Misérables', 'Victor Hugo', 'Historical Fiction', 14.49, 6),
    ('The Alchemist', 'Paulo Coelho', 'Fiction', 9.99, 30),
    ('The Kite Runner', 'Khaled Hosseini', 'Fiction', 10.99, 11),
    ('The Da Vinci Code', 'Dan Brown', 'Mystery', 12.99, 5),
    ('The Fault in Our Stars', 'John Green', 'Young Adult', 9.49, 17),
    ('Gone Girl', 'Gillian Flynn', 'Thriller', 12.49, 9),
    ('Divergent', 'Veronica Roth', 'Young Adult', 8.99, 18),
    ('The Maze Runner', 'James Dashner', 'Young Adult', 10.49, 14),
    ('The Hunger Games', 'Suzanne Collins', 'Dystopian', 10.99, 20),
    ('The Help', 'Kathryn Stockett', 'Historical Fiction', 11.99, 13),
    ('The Girl on the Train', 'Paula Hawkins', 'Thriller', 9.99, 8),
    ('The Time Traveler\'s Wife', 'Audrey Niffenegger', 'Romance', 12.49, 10),
    ('The Immortal Life of Henrietta Lacks', 'Rebecca Skloot', 'Non-Fiction', 15.99, 4),
    ('Educated', 'Tara Westover', 'Memoir', 13.49, 5),
    ('Becoming', 'Michelle Obama', 'Memoir', 14.99, 3),
    ('The Wright Brothers', 'David McCullough', 'Biography', 10.99, 12),
    ('The Glass Castle', 'Jeannette Walls', 'Memoir', 9.99, 10),
    ('Into the Wild', 'Jon Krakauer', 'Adventure', 8.49, 15),
    ('Outliers', 'Malcolm Gladwell', 'Non-Fiction', 12.99, 6),
    ('Thinking, Fast and Slow', 'Daniel Kahneman', 'Psychology', 11.49, 8),
    ('Quiet: The Power of Introverts in a World That Can\'t Stop Talking', 'Susan Cain', 'Psychology', 10.49, 9),
    ('The Power of Habit', 'Charles Duhigg', 'Non-Fiction', 13.99, 7),
    ('The Subtle Art of Not Giving a F*ck', 'Mark Manson', 'Self-Help', 9.99, 18),
    ('You Are a Badass', 'Jen Sincero', 'Self-Help', 11.99, 5),
]

# Insert the records into the BOOK table
for record in book_records:
    cursor.execute('''
        INSERT INTO BOOK (TITLE, AUTHOR, CATEGORY, PRICE, STOCK) 
        VALUES (?, ?, ?, ?, ?)
    ''', record)

# Display all the records
print("The inserted records are:")
data = cursor.execute('SELECT * FROM BOOK')
for row in data:
    print(row)

# Commit your changes in the database
connection.commit()
connection.close()
