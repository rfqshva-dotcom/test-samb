from connect import get_connection


def tampilkan_warehouse():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT WhsPK, WhsName
        FROM master_warehouse
    """)

    data = cursor.fetchall()

    print("\n=== DATA WAREHOUSE ===")

    if not data:
        print("Belum ada data warehouse")
    else:
        for row in data:
            print(f"ID: {row[0]} | Nama: {row[1]}")

    cursor.close()
    db.close()


def tambah_warehouse(nama):
    db = get_connection()
    cursor = db.cursor()

    sql = "INSERT INTO master_warehouse (WhsName) VALUES (%s)"

    cursor.execute(sql, (nama,))

    db.commit()

    print(f"Warehouse '{nama}' berhasil ditambahkan")

    cursor.close()
    db.close()


def ubah_warehouse(id_warehouse, nama_baru):
    db = get_connection()
    cursor = db.cursor()

    sql = "UPDATE master_warehouse SET WhsName = %s WHERE WhsPK = %s"

    nilai = (nama_baru, id_warehouse)

    cursor.execute(sql, nilai)

    db.commit()

    print("Warehouse berhasil diubah")

    cursor.close()
    db.close()