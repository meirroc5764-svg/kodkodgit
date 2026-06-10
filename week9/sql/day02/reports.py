from database_manager import *

def get_summary():
    conn = connecting()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total from soldiers")

    total = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS active from soldiers WHERE active = TRUE")

    active = cursor.fetchone()["active"]

    cursor.close()
    conn.close()

    return {"total":total, "active":active, "inactive": total - active}


def count_by_unit():
    conn = connecting()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""SELECT unit, COUNT(unit) AS total from soldiers 
                   GROUP BY unit 
                   ORDER BY total DESC""")
    
    total = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return total 

def get_missing_data():
    conn = connecting()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""SELECT * FROM soldiers 
                   WHERE ranky IS NULL""")
    
    total = cursor.fetchall()

    cursor.close()
    conn.close()

    return total

def get_units_with_multiple_soldiers():
    conn = connecting()

    cursor = conn.cursor(dictionary=True)

    cursor.execute("""SELECT unit ,COUNT(unit) AS total from soldiers
                   GROUP BY unit 
                   HAVING total > 1""")
    
    total = cursor.fetchall()

    cursor.close()
    conn.close()


    return total

if __name__ == "__main__":
    print(get_summary())
    print(count_by_unit())
    print(get_missing_data())
    print(get_units_with_multiple_soldiers())