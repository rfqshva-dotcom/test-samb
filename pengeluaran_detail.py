from connect import get_connection


def tampilkan_detail_pengeluaran():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT TrxOutDPK, TrxOutIDF, TrxOutDProductIdf,
               TrxOutDQtyDus, TrxOutDQtyPcs
        FROM transaksi_pengeluaran_barang_detail
    """)

    data = cursor.fetchall()

    print("\n=== DETAIL PENGELUARAN BARANG ===")

    if not data:
        print("Belum ada detail pengeluaran")
    else:
        for row in data:
            print(
                f"ID Detail: {row[0]} | "
                f"ID Transaksi: {row[1]} | "
                f"Product: {row[2]} | "
                f"Qty Dus: {row[3]} | "
                f"Qty Pcs: {row[4]}"
            )

    cursor.close()
    db.close()


def tambah_detail_pengeluaran(
    id_transaksi,
    id_product,
    qty_dus,
    qty_pcs
):
    db = get_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO transaksi_pengeluaran_barang_detail
        (TrxOutIDF, TrxOutDProductIdf, TrxOutDQtyDus, TrxOutDQtyPcs)
        VALUES (%s, %s, %s, %s)
    """

    nilai = (
        id_transaksi,
        id_product,
        qty_dus,
        qty_pcs
    )

    cursor.execute(sql, nilai)

    db.commit()

    print("Detail pengeluaran berhasil ditambahkan")

    cursor.close()
    db.close()