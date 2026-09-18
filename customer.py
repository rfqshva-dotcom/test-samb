from connect import get_connection


def tampilkan_customer():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT CustomerPK, CustomerName
        FROM master_customer
    """)

    data = cursor.fetchall()

    print("\n=== DATA CUSTOMER ===")

    if not data:
        print("Belum ada data customer")
    else:
        for row in data:
            print(f"ID: {row[0]} | Nama: {row[1]}")

    cursor.close()
    db.close()


def tambah_customer(nama):
    db = get_connection()
    cursor = db.cursor()

    sql = "INSERT INTO master_customer (CustomerName) VALUES (%s)"

    cursor.execute(sql, (nama,))

    db.commit()

    print(f"Customer '{nama}' berhasil ditambahkan")

    cursor.close()
    db.close()


def ubah_customer(id_customer, nama_baru):
    db = get_connection()
    cursor = db.cursor()

    sql = "UPDATE master_customer SET CustomerName = %s WHERE CustomerPK = %s"

    nilai = (nama_baru, id_customer)

    cursor.execute(sql, nilai)

    db.commit()

    print("Customer berhasil diubah")

    cursor.close()
    db.close()