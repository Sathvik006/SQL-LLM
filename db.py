import pandas as pd
import sqlite3

def csv_to_sqlite(csv_file, db_file, table_name):
    df = pd.read_csv(csv_file)
    
    conn = sqlite3.connect(db_file)
    
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"CSV data has been successfully imported to {db_file} in table {table_name}")

filepath = "./Transactions.csv"
# csv_to_sqlite(filepath, 'transactions.db', 'transactions')


def execute_sql_query(db, sql_query):
    try:
        conn = sqlite3.connect(db)
        
        cursor = conn.cursor()
        cursor.execute(sql_query)
        results = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]
        conn.close()
        
        return column_names, results
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None, None

def query_database(db, sql_query):
    column_names, results = execute_sql_query(db, sql_query)
    
    if column_names and results:
        result_dicts = [dict(zip(column_names, row)) for row in results]
        return result_dicts
    else:
        return None
