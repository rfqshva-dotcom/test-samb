from connect import get_connection


def tampilkan_penerimaan():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT TrxInPK, TrxInNo, WhsIdf, TrxInDate, TrxInSuppIdf, TrxInNotes
        FROM transaksi_penerimaan_barang_header
    """)

    data = cursor.fetchall()

    print("\n=== DATA PENERIMAAN BARANG ===")

    if not data:
        print("Belum ada data penerimaan")
    else:
        for row in data:
            print(
                f"ID: {row[0]} | "
                f"No: {row[1]} | "
                f"Warehouse: {row[2]} | "
                f"Tanggal: {row[3]} | "
                f"Supplier: {row[4]} | "
                f"Catatan: {row[5]}"
            )

    cursor.close()
    db.close()


def tambah_penerimaan(no_transaksi, warehouse, tanggal, supplier, catatan):
    db = get_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO transaksi_penerimaan_barang_header
        (TrxInNo, WhsIdf, TrxInDate, TrxInSuppIdf, TrxInNotes)
        VALUES (%s, %s, %s, %s, %s)
    """

    nilai = (
        no_transaksi,
        warehouse,
        tanggal,
        supplier,
        catatan
    )

    cursor.execute(sql, nilai)

    db.commit()

    print("Penerimaan barang berhasil ditambahkan")

    cursor.close()
    db.close()