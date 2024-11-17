import sqlite3
import pandas as pd

class SQLiteDB:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self # By returning self, we’re effectively passing the instance of the class back to the with statement,
        #which then allows us to assign it to a variable and access its methods and attributes within the block.

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print(f"Exception type: {exc_type}")
            print(f"Exception value: {exc_value}")
            print(f"Traceback: {traceback}")
        self.conn.close()

    def write_single_record(self, table, record): #params e.g.: ('department', {'department_id': '7', 'department_name': 'Test department'})
        columns = ', '.join(record.keys())
        placeholders = ', '.join(['?' for _ in record])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})" #INSERT INTO department (department_id, department_name) VALUES (?, ?)
        with self.conn: #Manages the transaction that executes the SQL query. It ensures that any database operation is properly committed or rolled back as needed, preserving data consistency and atomicity.
            self.conn.execute(query, tuple(record.values()))

    def write_multiple_records(self, table, records):
 
        columns = ', '.join(records[0].keys())
        placeholders = ', '.join(['?' for _ in records[0]])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        with self.conn:
            self.conn.executemany(query, [tuple(r.values()) for r in records])

    def update_record(self, table, updates, identifier):
        update_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
        identifier_clause = ' AND '.join([f"{k} = ?" for k in identifier.keys()])
        query = f"UPDATE {table} SET {update_clause} WHERE {identifier_clause}" # UPDATE department SET department_name = ? WHERE department_id = ?
        with self.conn:
            self.conn.execute(query, tuple(updates.values()) + tuple(identifier.values()))

    def delete_records(self, table, where_clause, params = None):
        query = f"DELETE FROM {table} WHERE {where_clause}"
        with self.conn:
            self.conn.execute(query, params or [])

    def select_records(self, query, params = None) -> pd.DataFrame:
        df = pd.read_sql_query(query, self.conn, params=params)
        return df

    def upsert_record(self, table, record, conflict_columns):
        columns = ', '.join(record.keys())
        placeholders = ', '.join(['?' for _ in record])
        conflict_clause = ', '.join(conflict_columns)
        update_clause = ', '.join([f"{k} = excluded.{k}" for k in record.keys()])
        query = f"""
            INSERT INTO {table} ({columns}) VALUES ({placeholders})
            ON CONFLICT({conflict_clause}) DO UPDATE SET {update_clause}
        """
        print(query)
        """
            INSERT INTO department (department_id, department_name) VALUES (?, ?)
            ON CONFLICT(department_id) DO UPDATE SET department_name = excluded.department_name
        """
        with self.conn:
            self.conn.execute(query, tuple(record.values()))

    def write_dataframe_to_table(self, df: pd.DataFrame, table: str, if_exists: str = 'append', index: bool = False):

        df.to_sql(name=table, con=self.conn, if_exists=if_exists, index=index)


with SQLiteDB('15/sqlite-db') as db: # Manages the database connection itself — ensuring it opens and closes correctly.

    employee_df = db.select_records("SELECT * FROM employee")
    print(employee_df)

    #db.write_single_record('department', {'department_id': '11', 'department_name': 'Test department'})

    departments = [
        {'department_id': 8, 'department_name': 'ExecutueManyDepartment1'},
        {'department_id': 9, 'department_name': 'ExecuteManyDepartment2'}
    ]
    #db.write_multiple_records('department', departments)

    #db.update_record('department', {'department_name': 'UpdatedDepartmentName'}, {'department_id': 9})

    #db.delete_records('department', "department_id = ?", [8])
    #where_clause = "employee_id = ? AND status = ?"
    #params = [5, 'inactive']
    
    db.upsert_record('department', {'department_id': 9, 'department_name': 'UpsertedDepartment3'}, ['department_id'])
    db.upsert_record('department', {'department_id': 10, 'department_name': 'UpsertedDepartment4'}, ['department_id'])

    df = pd.DataFrame({"department_id": ["anataloy"], "department_name": ["anatly department"]})

    #db.write_dataframe_to_table(df, "department")

    print(db.select_records("SELECT * FROM department"))