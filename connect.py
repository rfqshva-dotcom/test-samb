import  mysql.connector

def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gudang_projek",
    )

    return db




if __name__ == "__main__":
    db = get_connection()

    if db.is_connected():
        print('koneksi berhasil')
