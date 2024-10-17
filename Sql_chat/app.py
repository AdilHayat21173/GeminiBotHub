from dotenv import load_dotenv
load_dotenv()  # load all environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure Genai Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to read SQL queries from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return f"Error: {str(e)}"

# Function to execute SQL for table creation
def create_table(table_name, columns, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        column_definitions = ", ".join([f"{col} VARCHAR(25)" for col in columns])
        sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions});"
        cur.execute(sql)
        conn.commit()
        conn.close()
        return "Table created successfully!"
    except Exception as e:
        return f"Error: {str(e)}"

# Function to insert data into any table
def insert_record(table_name, columns, values, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        columns_str = ", ".join(columns)
        placeholders = ", ".join(["?" for _ in values])
        sql = f"INSERT INTO {table_name} ({columns_str}) VALUES ({placeholders});"
        cur.execute(sql, values)
        conn.commit()
        conn.close()
        return "Record inserted successfully!"
    except Exception as e:
        return f"Error: {str(e)}"
# Define your prompt for SQL conversion
prompt = [
    """
    You are an expert in converting simple English questions into SQL queries for various tables, particularly the BOOK table.
    The BOOK table has the following columns:
    - ID: Unique identifier for each book
    - TITLE: Title of the book
    - AUTHOR: Author of the book
    - CATEGORY: Category under which the book is classified
    - PRICE: Price of the book
    - STOCK: Quantity of the book available in inventory

    Here are some types of questions a user might ask:

    1. **Column Names**:
       - What columns are in the BOOK table?
       - Example response: "The BOOK table has the following columns: ID, TITLE, AUTHOR, CATEGORY, PRICE, STOCK."

    2. **Counting Books**:
       - How many books are available?
       - Example SQL: SELECT COUNT(*) FROM BOOK;

    3. **Book Details**:
       - What are the details of the book with ID 5?
       - Example SQL: SELECT * FROM BOOK WHERE ID = 5;

    4. **Finding by Author**:
       - Show me all books written by 'J.K. Rowling'.
       - Example SQL: SELECT * FROM BOOK WHERE AUTHOR = 'J.K. Rowling';

    5. **Price Queries**:
       - How many books cost more than $20?
       - Example SQL: SELECT COUNT(*) FROM BOOK WHERE PRICE > 20;

    6. **Retrieving Specific Columns**:
       - What are the titles and prices of all books?
       - Example SQL: SELECT TITLE, PRICE FROM BOOK;

    7. **Checking Stock Levels**:
       - Show me all books with stock less than 5.
       - Example SQL: SELECT * FROM BOOK WHERE STOCK < 5;

    8. **Updating Book Price**:
       - How do I change the price of the book 'Harry Potter' to $29.99?
       - Example SQL: UPDATE BOOK SET PRICE = 29.99 WHERE TITLE = 'Harry Potter';

    9. **Removing a Book**:
       - How do I delete the book with ID 3?
       - Example SQL: DELETE FROM BOOK WHERE ID = 3;

    10. **Listing Books by Price**:
        - Can you list all books sorted by price in ascending order?
        - Example SQL: SELECT * FROM BOOK ORDER BY PRICE ASC;

    11. **Adding New Book**:
        - How do I add a new book titled 'The Great Gatsby' in the 'Classic' category with a price of $15 and stock of 10?
        - Example SQL: INSERT INTO BOOK (TITLE, AUTHOR, CATEGORY, PRICE, STOCK) VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 'Classic', 15, 10);

    12. **Finding Book by Title**:
        - What is the price of 'To Kill a Mockingbird'?
        - Example SQL: SELECT PRICE FROM BOOK WHERE TITLE = 'To Kill a Mockingbird';

    13. **Checking Out of Stock Books**:
        - Which books are currently out of stock?
        - Example SQL: SELECT * FROM BOOK WHERE STOCK = 0;

    14. **Counting Books by Category**:
        - How many books are in the 'Science Fiction' category?
        - Example SQL: SELECT COUNT(*) FROM BOOK WHERE CATEGORY = 'Science Fiction';

    15. **Average Price of Books**:
        - What is the average price of all books?
        - Example SQL: SELECT AVG(PRICE) FROM BOOK;

    16. **Books in a Price Range**:
        - Show me all books priced between $10 and $30.
        - Example SQL: SELECT * FROM BOOK WHERE PRICE BETWEEN 10 AND 30;

    17. **Book Titles Containing a Word**:
        - Find all books whose titles contain the word 'Adventure'.
        - Example SQL: SELECT * FROM BOOK WHERE TITLE LIKE '%Adventure%';

    18. **Books Sorted by Stock**:
        - List all books sorted by stock in descending order.
        - Example SQL: SELECT * FROM BOOK ORDER BY STOCK DESC;

    19. **Finding Books by Partial ID**:
        - Show me all books with IDs starting with '1'.
        - Example SQL: SELECT * FROM BOOK WHERE ID LIKE '1%';

    20. **Count Distinct Categories**:
        - How many distinct categories are there in the BOOK table?
        - Example SQL: SELECT COUNT(DISTINCT CATEGORY) FROM BOOK;

    21. **Maximum Price of Books**:
        - What is the highest price among all books?
        - Example SQL: SELECT MAX(PRICE) FROM BOOK;

    22. **Minimum Price of Books**:
        - What is the lowest price among all books?
        - Example SQL: SELECT MIN(PRICE) FROM BOOK;

    23. **List All Book Titles**:
        - Can you list the titles of all books?
        - Example SQL: SELECT TITLE FROM BOOK;

    24. **Count Books in Stock**:
        - How many books are currently in stock?
        - Example SQL: SELECT SUM(STOCK) FROM BOOK;

    25. **Change Book Category**:
        - How do I change the category of the book 'Chair' to 'Office Furniture'?
        - Example SQL: UPDATE BOOK SET CATEGORY = 'Office Furniture' WHERE TITLE = 'Chair';

    26. **Get Books with Specific Stock**:
        - List all books that have exactly 15 items in stock.
        - Example SQL: SELECT * FROM BOOK WHERE STOCK = 15;

    27. **Show Books with No Stock**:
        - Which books have never been stocked?
        - Example SQL: SELECT * FROM BOOK WHERE STOCK IS NULL;

    28. **Checking Book Availability**:
        - Are there any books available in the 'History' category?
        - Example SQL: SELECT * FROM BOOK WHERE CATEGORY = 'History' AND STOCK > 0;

    29. **Listing All Categories**:
        - What categories are available in the BOOK table?
        - Example SQL: SELECT DISTINCT CATEGORY FROM BOOK;

    30. **Finding Expensive Books**:
        - List all books that cost more than $50.
        - Example SQL: SELECT * FROM BOOK WHERE PRICE > 50;

    31. **Books with Stock Greater Than Average**:
        - Which books have more stock than the average stock?
        - Example SQL: SELECT * FROM BOOK WHERE STOCK > (SELECT AVG(STOCK) FROM BOOK);

    32. **Get Books with Specific Price**:
        - Which books are priced at $19.99?
        - Example SQL: SELECT * FROM BOOK WHERE PRICE = 19.99;

    33. **Filter by Multiple Conditions**:
        - Show me all books in the 'Children' category that are priced below $15 and are in stock.
        - Example SQL: SELECT * FROM BOOK WHERE CATEGORY = 'Children' AND PRICE < 15 AND STOCK > 0;

    34. **Find Newest Books**:
        - How do I find the most recently added books?
        - Example SQL: SELECT * FROM BOOK ORDER BY ID DESC;  # Assuming ID is incremented for new entries

    35. **Counting Books by Title**:
        - How many 'Mystery' books are available?
        - Example SQL: SELECT COUNT(*) FROM BOOK WHERE TITLE LIKE '%Mystery%';

    36. **Books Above Average Price**:
        - List all books that are more expensive than the average price.
        - Example SQL: SELECT * FROM BOOK WHERE PRICE > (SELECT AVG(PRICE) FROM BOOK);

    37. **Finding Books by Stock Level**:
        - How many books have stock levels greater than 50?
        - Example SQL: SELECT COUNT(*) FROM BOOK WHERE STOCK > 50;

    38. **Checking for Book Existence**:
        - Does the book 'The Hobbit' exist in the database?
        - Example SQL: SELECT EXISTS(SELECT 1 FROM BOOK WHERE TITLE = 'The Hobbit');

    39. **Group Books by Category**:
        - How many books are there in each category?
        - Example SQL: SELECT CATEGORY, COUNT(*) FROM BOOK GROUP BY CATEGORY;

    40. **List Books with Specific Title Length**:
        - Show me all books with titles longer than 10 characters.
        - Example SQL: SELECT * FROM BOOK WHERE LENGTH(TITLE) > 10;

    41. **Identify Non-Stocked Books**:
        - Are there any books that are not stocked?
        - Example SQL: SELECT * FROM BOOK WHERE STOCK = 0;

    42. **Show Total Value of Stock**:
        - What is the total value of all books in stock?
        - Example SQL: SELECT SUM(PRICE * STOCK) FROM BOOK;

    43. **Find Books with Similar Titles**:
        - List all books with titles similar to 'Great'.
        - Example SQL: SELECT * FROM BOOK WHERE TITLE LIKE '%Great%';

    44. **Check Books by Category Count**:
        - How many books are there in the 'Fiction' category?
        - Example SQL: SELECT COUNT(*) FROM BOOK WHERE CATEGORY = 'Fiction';

    45. **List Books with High Stock**:
        - Which books have more than 100 units in stock?
        - Example SQL: SELECT * FROM BOOK WHERE STOCK > 100;

    46. **Calculate Total Books Count**:
        - How do I find the total count of books?
        - Example SQL: SELECT COUNT(*) FROM BOOK;

    47. **Get Books with Exact Price**:
        - Show me books that cost exactly $25.
        - Example SQL: SELECT * FROM BOOK WHERE PRICE = 25;

    48. **Delete Books by Condition**:
        - How do I delete books that have been priced below $5?
        - Example SQL: DELETE FROM BOOK WHERE PRICE < 5;

    49. **Identify Price Range Books**:
        - Show me books priced between $30 and $40.
        - Example SQL: SELECT * FROM BOOK WHERE PRICE BETWEEN 30 AND 40;

    50. **List Top 5 Most Expensive Books**:
        - How do I find the top 5 most expensive books?
        - Example SQL: SELECT * FROM BOOK ORDER BY PRICE DESC LIMIT 5;
    """
]

#
# Initialize session state for table creation and data insertion
if 'columns_list' not in st.session_state:
    st.session_state.columns_list = []
if 'table_created' not in st.session_state:
    st.session_state.table_created = False
if 'table_name' not in st.session_state:
    st.session_state.table_name = ""

# Streamlit App
st.set_page_config(page_title="SQL Data Retriever & Inserter")
st.header("Smart Bookshop Query and Data Manager")
# --- Section to create a new table ---
st.header("Create a New Table(if you want)")

st.session_state.table_name = st.text_input("Enter Table Name:", key="table_name_input")
columns_input = st.text_area("Enter Column Names (comma-separated):", key="columns_input")

create_table_btn = st.button("Submit")
if create_table_btn:
        if st.session_state.table_name and columns_input:
            st.session_state.columns_list = [col.strip() for col in columns_input.split(",")]
            create_table_msg = create_table(st.session_state.table_name, st.session_state.columns_list, "book_shop.db")
            st.session_state.table_created = True
            st.success(create_table_msg)
        else:
            st.error("Please provide both table name and column names.")

# # --- Section to insert records after table is created ---
if st.session_state.get("table_created", False):  # Ensure session state is used correctly
    st.subheader(f"Insert Data into {st.session_state.table_name}")
    
    insert_values = []
    for col in st.session_state.columns_list:
        value = st.text_input(f"Enter value for {col}:", key=f"insert_value_{col}")
        insert_values.append(value)
    
    insert_btn = st.button("Insert Record")
    
    if insert_btn:
        if all(insert_values):
            insert_msg = insert_record(st.session_state.table_name, st.session_state.columns_list, insert_values, "book_shop.db")
            st.success(insert_msg)
            
            # Button to insert more records
            more_records_btn = st.button("Add More Records")
            if more_records_btn:
                st.experimental_rerun()  # Rerun the app to allow adding more records
        else:
            st.error("Please provide values for all columns.")



# --- Section to retrieve data ---
st.subheader("Ask a question to retrieve data")
question = st.text_input("Input your question: ", key="input")
submit = st.button("Retrieve Data")

if submit:
    # Assuming this function generates the SQL query
    sql_query = get_gemini_response(question, prompt)
    
    st.subheader("Generated SQL Query:")
    st.code(sql_query, language='sql')  # Display the SQL query for user review

    # Ensure no markdown formatting in the actual SQL query before execution
    clean_sql_query = sql_query.strip('```sql ')  # Remove markdown if mistakenly added

    response = read_sql_query(clean_sql_query, "book_shop.db")

    if isinstance(response, str) and response.startswith("Error"):
        st.error(response)  # Display the error message
    else:
        st.subheader("Query Result:")
        if response:
            for row in response:  # Loop through the query results and display each row
                st.text(row)  # You can use `st.text` or `st.write` to display the rows
        else:
            st.info("No data returned.")  # Message when no data is returned
