import sqlite3  # Import the sqlite3 module to work with SQLite databases.

# Connect to the large database
# Establish a connection to the source SQLite database named '23_ios.db'.
large_db_conn = sqlite3.connect('23_ios.db')
# Create a cursor object using the cursor() method. It is used to traverse and interact with the database records.
large_db_cursor = large_db_conn.cursor()

# Connect to the new, smaller database.
# Establish a connection to the destination SQLite database named 'small_database.db'.
# If this database does not exist, it will be created.
small_db_conn = sqlite3.connect('small_database.db')
# Create a cursor object for the smaller database.
small_db_cursor = small_db_conn.cursor()

# Create a table in the small database.
# Execute an SQL statement to create a table named 'FILE' in the smaller database.
# The CREATE TABLE statement includes column names and their respective data types.
small_db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS FILE (
        sha256     VARCHAR NOT NULL,
        sha1       VARCHAR NOT NULL,
        md5        VARCHAR NOT NULL,
        crc32      VARCHAR NOT NULL,
        file_name  VARCHAR NOT NULL,
        file_size  INTEGER NOT NULL,
        package_id INTEGER NOT NULL
    )
''')
# Commit the transaction, ensuring that the table creation is saved in the smaller database.
small_db_conn.commit()

# Query to get the subset of data from the large database.
# Execute an SQL SELECT statement on the large database to retrieve the first 100 records from the 'FILE' table.
large_db_cursor.execute('SELECT * FROM FILE LIMIT 100')

# Insert the fetched data into the smaller database.
# Loop through each record retrieved from the large database.
for row in large_db_cursor.fetchall():
    # For each record, execute an SQL INSERT statement to add the record to the 'FILE' table in the smaller database.
    small_db_cursor.execute('INSERT INTO FILE (sha256, sha1, md5, crc32, file_name, file_size, package_id) VALUES (?, ?, ?, ?, ?, ?, ?)', row)
    # Commit the transaction, ensuring that each record insertion is saved in the smaller database.
    small_db_conn.commit()

# Close the database connections when done.
# It's vital to close connections to release resources and ensure that no further changes can be made to the databases.
large_db_conn.close()
small_db_conn.close()