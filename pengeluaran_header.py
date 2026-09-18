from connect import get_connection


def tampilkan_pengeluaran():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT TrxOutPK, TrxOutNo, WhsIdf, TrxOutDate,
               TrxOutSuppIdf, TrxOutNotes
        FROM transaksi_pengeluaran_barang_header
    """)

    data = cursor.fetchall()

    print("\n=== DATA PENGELUARAN BARANG ===")

    if not data:
        print("Belum ada data pengeluaran")
    else:
        for row in data:
            print(
                f"ID: {row[0]} | "
                f"No: {row[1]} | "
                f"Warehouse: {row[2]} | "
                f"Tanggal: {row[3]} | "
                f"Customer: {row[4]} | "
                f"Catatan: {row[5]}"
            )

    cursor.close()
    db.close()


def tambah_pengeluaran(
    no_transaksi,
    warehouse,
    tanggal,
    customer,
    catatan
):
    db = get_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO transaksi_pengeluaran_barang_header
        (TrxOutNo, WhsIdf, TrxOutDate, TrxOutSuppIdf, TrxOutNotes)
        VALUES (%s, %s, %s, %s, %s)
    """

    nilai = (
        no_transaksi,
        warehouse,
        tanggal,
        customer,
        catatan
    )

    cursor.execute(sql, nilai)

    db.commit()

    print("Pengeluaran barang berhasil ditambahkan")

    cursor.close()
    db.close()