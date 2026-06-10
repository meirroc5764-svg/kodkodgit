from mysql import connector

def connecting():
    return connector.connect(host  ="localhost",
                            user = "root",
                            password = "root",
                            database = "soldier_db"
                            )

def get_schema():
    conn = connecting()
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS soldier_db;")
    cursor.execute("USE soldier_db")
    cursor.execute("""CREATE TABLE IF NOT EXISTS soldiers(
                   id INT PRIMARY KEY AUTO_INCREMENT,
                   name VARCHAR(100) NOT NULL,
                   ranky VARCHAR(50),
                   unit VARCHAR(100),
                   active BOOLEAN DEFAULT TRUE)""")
    conn.commit()
    cursor.close()
    conn.close()
    return "table create"


if __name__ == "__main__":
    print(get_schema())