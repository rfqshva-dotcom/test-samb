from connect import get_connection


def tampilkan_stok():
    db = get_connection()
    cursor = db.cursor()

    sql = """
        SELECT
            p.ProductPK,
            p.ProductName,

            COALESCE(SUM(masuk.TrxInDQtyDus), 0) AS TotalMasukDus,
            COALESCE(SUM(masuk.TrxInDQtyPcs), 0) AS TotalMasukPcs,

            COALESCE(SUM(keluar.TrxOutDQtyDus), 0) AS TotalKeluarDus,
            COALESCE(SUM(keluar.TrxOutDQtyPcs), 0) AS TotalKeluarPcs

        FROM master_product p

        LEFT JOIN transaksi_penerimaan_barang_detail masuk
            ON p.ProductPK = masuk.TrxInDProductIdf

        LEFT JOIN transaksi_pengeluaran_barang_detail keluar
            ON p.ProductPK = keluar.TrxOutDProductIdf

        GROUP BY p.ProductPK, p.ProductName
    """

    cursor.execute(sql)

    data = cursor.fetchall()

    print("\n=== LAPORAN STOK BARANG ===")

    if not data:
        print("Belum ada data stok")
    else:
        for row in data:

            stok_dus = row[2] - row[4]
            stok_pcs = row[3] - row[5]

            print(
                f"ID Product: {row[0]} | "
                f"Product: {row[1]}"
            )

            print(
                f"  Masuk  : {row[2]} Dus | {row[3]} Pcs"
            )

            print(
                f"  Keluar : {row[4]} Dus | {row[5]} Pcs"
            )

            print(
                f"  Stok   : {stok_dus} Dus | {stok_pcs} Pcs"
            )

            print("-----------------------------------")

    cursor.close()
    db.close()