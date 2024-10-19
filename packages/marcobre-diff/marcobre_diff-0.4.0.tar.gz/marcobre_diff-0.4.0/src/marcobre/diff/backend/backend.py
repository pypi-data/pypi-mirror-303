import os
import sqlite3
import datetime

def create_database_connection():
    try:
        home_dir = os.path.expanduser("~")
        marcobre_home_dir = os.path.join(home_dir, '.marcobre')
        os.makedirs(marcobre_home_dir, exist_ok=True)
        marcobre_db = os.path.join(marcobre_home_dir, 'marcobre.db')

        conn = sqlite3.connect(marcobre_db)
        return  conn
    except sqlite3.Error as err:
        print(f"Error connecting to the database: {err}")
        return  None

def create_historical_table():
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS historical (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file1_input_name VARCHAR(255) NOT NULL,
                file2_input_name VARCHAR(255) NOT NULL,
                file_output_name VARCHAR(255) NOT NULL,
                created_at DATETIME NOT NULL DEFAULT (datetime('now', 'localtime'))
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating notes table: {err}")

def execute_query(query, params = None):
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        if params:
            cursor.execute(query,params)
        else:
            cursor.execute(query)
        results = cursor.fetchall()
        print(results,'aqui')
        cursor.close()
        conn.close()
        return  results
    except sqlite3.Error as err:
        print(f"Error executing query: {err}")
        return []

# Crud
def create_historical(file1_input_name='', file2_input_name='', file_output_name=''):
    now_local = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    insert_query = "INSERT INTO historical (file1_input_name, file2_input_name, file_output_name, created_at) VALUES (?, ?, ?, ?)"
    params = (file1_input_name, file2_input_name, file_output_name, now_local)
    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute(insert_query, params)
        conn.commit()
        print("Historical created successfully")
    except sqlite3.Error as err:
        print(f"Error inserting historical record: {err}")
    finally:
        if conn:
            conn.close()


def get_historical_by_id(historical_id):
    result = None
    select_query = "SELECT * FROM historical WHERE id = ?"
    params = (historical_id,)
    results = execute_query(select_query,params)
    if len(results) == 1:
        print(f"Retrieved historical {historical_id} successfully.")
        result = results[0]
    else:
        print(f"Historical {historical_id} not found.")
        result = None
    return result


def get_all_historical():
    select_query = "SELECT * FROM historical ORDER BY created_at DESC"
    results = execute_query(select_query)
    print(f"Retrieved {len(results)} historical(s) successfully.")
    return  results


def delete_historical(historical_id):
    delete_query = "DELETE FROM historical WHERE id = ?"
    params = (historical_id,)

    try:
        conn = create_database_connection()
        cursor = conn.cursor()
        cursor.execute(delete_query, params)
        conn.commit()

        if cursor.rowcount > 0:
            print(f"Deleted historical {historical_id} successfully.")
        else:
            print(f"No historical record found with id {historical_id}.")

    except sqlite3.Error as err:
        print(f"Error deleting historical record: {err}")

    finally:
        cursor.close()
        if conn:
            conn.close()



