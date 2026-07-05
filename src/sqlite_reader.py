import sqlite3

def create_and_read_db():
    # Connect to database
    conn = sqlite3.connect("sales.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        product TEXT,
        category TEXT,
        quantity INTEGER,
        price INTEGER
    )
    """)

    # Check if table already has data
    cursor.execute("SELECT COUNT(*) FROM sales")
    count = cursor.fetchone()[0]

    # Insert data only once (prevents duplicates)
    if count == 0:
        cursor.execute("INSERT INTO sales VALUES ('Laptop','Electronics',5,60000)")
        cursor.execute("INSERT INTO sales VALUES ('Mouse','Electronics',20,500)")
        cursor.execute("INSERT INTO sales VALUES ('Keyboard','Electronics',15,1200)")
        conn.commit()

    # Read data
    cursor.execute("SELECT * FROM sales")
    rows = cursor.fetchall()

    print("\nSQLite Data:\n")

    for row in rows:
        print(row)

    # Close connection
    conn.close()


if __name__ == "__main__":
    create_and_read_db()