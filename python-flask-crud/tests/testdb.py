import psycopg2

def create_postgres_table():
    # 1. Define your database credentials
    connection_params = {
        "host": "192.168.1.67",
        "database": "pyappdb",
        "user": "app_user",
        "password": "password1",
        "port": "5432"
    }
    
    # 2. Define the SQL query to create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(50) NOT NULL,
        last_name VARCHAR(50) NOT NULL,
        email VARCHAR(100) UNIQUE,
        hire_date DATE DEFAULT CURRENT_DATE,
        salary NUMERIC(10, 2)
    );
    """
    
    try:
        # 3. Connect to the PostgreSQL database
        with psycopg2.connect(**connection_params) as conn:
            
            # 4. Open a cursor to perform database operations
            with conn.cursor() as cursor:
                
                # 5. Execute the SQL command
                cursor.execute(create_table_query)
                print("Table created successfully!")
                
                # Note: The context manager automatically calls conn.commit() 
                # if the block exits without errors.
                
    except Exception as error:
        print(f"Error while creating PostgreSQL table: {error}")

if __name__ == "__main__":
    create_postgres_table()

