from connect import get_connection


def tampilkan_product():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT ProductPK, ProductName
        FROM master_product
    """)

    data = cursor.fetchall()

    print("\n=== DATA PRODUCT ===")

    if not data:
        print("Belum ada data product")
    else:
        for row in data:
            print(f"ID: {row[0]} | Nama: {row[1]}")

    cursor.close()
    db.close()


def tambah_product(nama):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO master_product (ProductName) VALUES (%s)",
        (nama,)
    )

    db.commit()

    print(f"Product '{nama}' berhasil ditambahkan")

    cursor.close()
    db.close()


def ubah_product(id_product, nama_baru):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(
        """
        UPDATE master_product
        SET ProductName = %s
        WHERE ProductPK = %s
        """,
        (nama_baru, id_product)
    )

    db.commit()

    print("Product berhasil diubah")

    cursor.close()
    db.close()