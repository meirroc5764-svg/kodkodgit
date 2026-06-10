from data_base import connecting,get_schema

def all_data():
    conn = connecting()
    
    curser = conn.cursor()
    
    try:
        curser.execute("SELECT * FROM soldiers")
       
        data = curser.fetchall()
        
        return data
    
    except:
        return None

def create_new_soldier(name, rank, unit):
    conn = connecting()

    curser = conn.cursor()


    try:
        curser.execute("INSERT INTO soldiers (name, ranky, unit) VALUES (%s,%s,%s)",(name,rank,unit))

        conn.commit()
        return "adds a soldier"

    except:
        return None

def get_names_and_ranks() -> list:
    conn = connecting()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT id, name, ranky FROM soldiers")
    
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return rows


def get_soldier_by_rank(rank) -> list:
    conn = connecting()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute(
    "SELECT * FROM soldiers WHERE ranky = %s",(rank,)
    )
    
    rows = cursor.fetchall()
    
    cursor.close()
    conn.close()
    
    return rows




if __name__ == "__main__":
    print(get_soldier_by_rank("turay"))
    # print(get_names_and_ranks())
    # print(create_new_soldier("meir","turay","8200"))


