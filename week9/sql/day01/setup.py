from mysql import connector



def get_connection():
    return connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="soldier_db")
    
def manager():    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS soldier_db;")
    # cursor.execute("USE soldier_db")
    cursor.execute("""CREATE TABLE IF NOT EXISTS soldiers(
                   id INT PRIMARY KEY AUTO_INCREMENT,
                   name VARCHAR(100) NOT NULL,
                   ranky VARCHAR(50),
                   unit VARCHAR(100),
                   active BOOLEAN DEFAULT TRUE)""")
    conn.commit()
    cursor.close()
    conn.close()
    return


def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    # each row is (Field, Type, Null, Key, Default, Extra)
    return [{"column": row[0], "type": row[1]} for row in rows]

manager()
print(get_schema())