from connect import get_connection


def tampilkan_supplier():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT SupplierPK, SupplierName
        FROM master_supplier
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data


def tambah_supplier(nama):
    db = get_connection()
    cursor = db.cursor()

    sql = "INSERT INTO master_supplier (SupplierName) VALUES (%s)"

    cursor.execute(sql, (nama,))

    db.commit()

    cursor.close()
    db.close()


def ubah_supplier(id_supplier, nama_baru):
    db = get_connection()
    cursor = db.cursor()

    sql = "UPDATE master_supplier SET SupplierName = %s WHERE SupplierPK = %s"

    cursor.execute(sql, (nama_baru, id_supplier))

    db.commit()

    cursor.close()
    db.close()