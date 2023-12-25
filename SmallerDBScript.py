import sqlite3

# Connect to the large database named '23_ios.db'
large_db_conn = sqlite3.connect('23_ios.db')
# Create a cursor object using the cursor() method
large_db_cursor = large_db_conn.cursor()

# Connect to the smaller (destination) database
small_db_conn = sqlite3.connect('small_database.db')
# Create a cursor object for the smaller (destination) database
small_db_cursor = small_db_conn.cursor()

# Create a table named "FILE" in the (destination) smaller database
# Edit the title of the table, column names, and data types as necessary
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
# Commit the new table to the smaller (destination) database
small_db_conn.commit()

# Execute an SQL SELECT statement on the large database to retrieve the first 100 records from the 'FILE' table
large_db_cursor.execute('SELECT * FROM FILE LIMIT 100')

# Loop through each record retrieved from the large database and insert the fetched data into the smaller (destination) database
for row in large_db_cursor.fetchall():
    # For each record, execute an SQL INSERT statement to add the record to the 'FILE' table in the smaller database
    small_db_cursor.execute('INSERT INTO FILE (sha256, sha1, md5, crc32, file_name, file_size, package_id) VALUES (?, ?, ?, ?, ?, ?, ?)', row)
    # Commit to make sure that each record insertion is saved in the smaller database
    small_db_conn.commit()

# Close the database connections
large_db_conn.close()
small_db_conn.close()
