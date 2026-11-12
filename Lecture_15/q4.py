#!/usr/bin/python3
import MySQLdb

def get_table_choice(host, user, password, database):
# These are the Python comment lines in our function
    """
    Queries the database for all available tables and prompts the user to select one.
    Returns the string name of the chosen table, or None if exit/error.
    """
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        # Fetch all tables in the database
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        # Error trap...        
        if not tables:
            print("No tables found in this database.")
            return None
        # Display the tables as a numbered menu
        print("\nAvailable Tables:")
        print("-" * 30)
        for index, table_name in enumerate(tables, 1):
            print(f"[{index}] {table_name}")
        print("-" * 30)
        # Get the user to choose one!
        while True:
            try:
                choice = input(f"Pick a table number (1-{len(tables)}) or 'q' to quit: ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(tables):
                    return tables[choice_num - 1]
                else:
                    print(f"Invalid number. Please choose between 1 and {len(tables)}.")
            except ValueError:
                print("Please enter a valid number or 'q'.")
    except MySQLdb.Error as e:
        print(f"Database error while fetching tables: {e}")
        return None
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()






def show_table_structure(host, user, password, database, table_name):
    connection = None
    try:
        connection = MySQLdb.connect(
            host=host,
            user=user,
            passwd=password,
            db=database
        )
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        print(f"\nStructure for table: '{table_name}'")
        print("~" * 60)
        print(f"{'Field Name':<20} | {'Type':<15} | {'Null Allowed?':<12} | {'Key'}")
        print("~" * 60)
        for col in columns:
            print(f"{col[0]:<20} | {col[1]:<15} | {col[2]:<13} | {col[3]}")
        print("-" * 60)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.open:
            cursor.close()
            connection.close()


host = "127.0.0.1"
user = "s3014457"
password = "Angel09260926@"
database = "s3014457_blast"

table = get_table_choice(host, user, password, database)
if table:
    show_table_structure(host, user, password, database, table)
