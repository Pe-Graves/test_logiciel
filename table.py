import sqlite3
from sqlite3 import Error

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
        return False

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        return False


def add_user(conn, project):
    sql = ''' INSERT INTO utilisateur(username, password, spublickey, epublickey, sprivatekey, eprivatekey)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return True

def logging(utilisateur):
    if len(utilisateur[0]) <= 3:
        return False
    for i in utilisateur[0]:
        if i not in digits:
            return False
    if len(utilisateur[1]) < 8:
        return False
    for i in utilisateur[1]:
        if i not in ascii_letters or i not in digits:
            return False
    return True

def clefs(utilisateur):
    return utilisateur[2], utilisateur[3], utilisateur[4], utilisateur[5]

def check_all(utilisateur):
    clef1, clef2, clef3, clef4 = clefs(utilisateur)
    if len(clef1) < 128 or len(clef2) < 128 or len(clef3) < 128 or len(clef4) < 128:
        return False
    return logging(utilisateur)
    


def main():
    database = 'DataBase.db'

    sql_create_utilisateur_table = """ CREATE TABLE IF NOT EXISTS utilisateur (
                                    username TEXT,
                                    password TEXT,
                                    spublickey char(128),
                                    epublickey char(128),
                                    sprivatekey char(128),
                                    eprivatekey char(128)
                                    ); """
    
    # create a database connection
    conn = create_connection(database)

     # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_utilisateur_table)
        print("Successful ! Table was created.")

    else:
        print("Error! cannot create the database connection.")
        return False

    with conn:
        # create a new project
        utilisateur_1 = ('1234567', '2Ll0150101', 'Paul', 'Edouard', 'EISE5', '2021-2022')
        add_user(conn, utilisateur_1)
        check1 = logging(utilisateur_1)
        clef1, clef2, clef3, clef4 = clefs(utilisateur_1)
        check2 = check_all(utilisateur_1)
        
    return check1,clef1,clef2,clef3,clef4,check2


if __name__ == '__main__':
    main()