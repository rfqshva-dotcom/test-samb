from connect import get_connection


def tampilkan_detail_penerimaan():
    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT TrxInDPK, TrxInIDF, TrxInDProductIdf,
               TrxInDQtyDus, TrxInDQtyPcs
        FROM transaksi_penerimaan_barang_detail
    """)

    data = cursor.fetchall()

    print("\n=== DETAIL PENERIMAAN BARANG ===")

    if not data:
        print("Belum ada detail penerimaan")
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


def tambah_detail_penerimaan(
    id_transaksi,
    id_product,
    qty_dus,
    qty_pcs
):
    db = get_connection()
    cursor = db.cursor()

    sql = """
        INSERT INTO transaksi_penerimaan_barang_detail
        (TrxInIDF, TrxInDProductIdf, TrxInDQtyDus, TrxInDQtyPcs)
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

    print("Detail penerimaan berhasil ditambahkan")

    cursor.close()
    db.close()