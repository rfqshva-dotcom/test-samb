from flask import Flask, render_template, request, redirect

from connect import get_connection

app = Flask(__name__)



# HALAMAN UTAMA


@app.route("/")
def index():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT SupplierPK, SupplierName
        FROM master_supplier
    """)
    supplier = cursor.fetchall()

    cursor.execute("""
        SELECT CustomerPK, CustomerName
        FROM master_customer
    """)
    customer = cursor.fetchall()

    cursor.execute("""
        SELECT ProductPK, ProductName
        FROM master_product
    """)
    product = cursor.fetchall()

    cursor.execute("""
        SELECT WhsPK, WhsName
        FROM master_warehouse
    """)
    warehouse = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template(
        "index.html",
        supplier=supplier,
        customer=customer,
        product=product,
        warehouse=warehouse
    )



# SUPPLIER


@app.route("/supplier")
def supplier():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT SupplierPK, SupplierName
        FROM master_supplier
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("supplier.html", data=data)



# CUSTOMER


@app.route("/customer")
def customer():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT CustomerPK, CustomerName
        FROM master_customer
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("customer.html", data=data)



# PRODUCT


@app.route("/product")
def product():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT ProductPK, ProductName
        FROM master_product
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("product.html", data=data)



# WAREHOUSE

@app.route("/warehouse")
def warehouse():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT WhsPK, WhsName
        FROM master_warehouse
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("warehouse.html", data=data)


# PENERIMAAN BARANG


@app.route("/penerimaan")
def penerimaan():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            h.TrxInPK,
            h.TrxInNo,
            h.WhsIdf,
            h.TrxInDate,
            h.TrxInSuppIdf,
            h.TrxInNotes,
            d.TrxInDProductIdf,
            d.TrxInDQtyDus,
            d.TrxInDQtyPcs
        FROM transaksi_penerimaan_barang_header h
        JOIN transaksi_penerimaan_barang_detail d
            ON h.TrxInPK = d.TrxInIDF
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("penerimaan.html", data=data)



# PENGELUARAN BARANG


@app.route("/pengeluaran")
def pengeluaran():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            h.TrxOutPK,
            h.TrxOutNo,
            h.WhsIdf,
            h.TrxOutDate,
            h.TrxOutSuppIdf,
            h.TrxOutNotes,
            d.TrxOutDProductIdf,
            d.TrxOutDQtyDus,
            d.TrxOutDQtyPcs
        FROM transaksi_pengeluaran_barang_header h
        JOIN transaksi_pengeluaran_barang_detail d
            ON h.TrxOutPK = d.TrxOutIDF
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("pengeluaran.html", data=data)



# LAPORAN STOK


@app.route("/stok")
def stok():

    db = get_connection()
    cursor = db.cursor()

    cursor.execute("""
        SELECT
            p.ProductPK,
            p.ProductName,

            COALESCE(SUM(masuk.TrxInDQtyDus), 0),
            COALESCE(SUM(masuk.TrxInDQtyPcs), 0),

            COALESCE(SUM(keluar.TrxOutDQtyDus), 0),
            COALESCE(SUM(keluar.TrxOutDQtyPcs), 0)

        FROM master_product p

        LEFT JOIN transaksi_penerimaan_barang_detail masuk
            ON p.ProductPK = masuk.TrxInDProductIdf

        LEFT JOIN transaksi_pengeluaran_barang_detail keluar
            ON p.ProductPK = keluar.TrxOutDProductIdf

        GROUP BY p.ProductPK, p.ProductName
    """)

    data = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("stok.html", data=data)



# BARANG MASUK


@app.route("/barang-masuk", methods=["POST"])
def barang_masuk():

    db = get_connection()
    cursor = db.cursor()

    no = request.form["no"]
    warehouse = request.form["warehouse"]
    tanggal = request.form["tanggal"]
    supplier = request.form["supplier"]
    product = request.form["product"]
    qty_dus = request.form["qty_dus"]
    qty_pcs = request.form["qty_pcs"]
    catatan = request.form["catatan"]

    cursor.execute("""
        INSERT INTO transaksi_penerimaan_barang_header
        (TrxInNo, WhsIdf, TrxInDate, TrxInSuppIdf, TrxInNotes)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        no,
        warehouse,
        tanggal,
        supplier,
        catatan
    ))

    id_transaksi = cursor.lastrowid

    cursor.execute("""
        INSERT INTO transaksi_penerimaan_barang_detail
        (TrxInIDF, TrxInDProductIdf, TrxInDQtyDus, TrxInDQtyPcs)
        VALUES (%s, %s, %s, %s)
    """, (
        id_transaksi,
        product,
        qty_dus,
        qty_pcs
    ))

    db.commit()

    cursor.close()
    db.close()

    return redirect("/")



# BARANG KELUAR

@app.route("/barang-keluar", methods=["POST"])
def barang_keluar():

    db = get_connection()
    cursor = db.cursor()

    no = request.form["no"]
    warehouse = request.form["warehouse"]
    tanggal = request.form["tanggal"]
    supplier = request.form["supplier"]
    product = request.form["product"]
    qty_dus = request.form["qty_dus"]
    qty_pcs = request.form["qty_pcs"]
    catatan = request.form["catatan"]

    cursor.execute("""
        INSERT INTO transaksi_pengeluaran_barang_header
        (TrxOutNo, WhsIdf, TrxOutDate, TrxOutSuppIdf, TrxOutNotes)
        VALUES (%s, %s, %s, %s, %s)
    """, (
        no,
        warehouse,
        tanggal,
        supplier,
        catatan
    ))

    id_transaksi = cursor.lastrowid

    cursor.execute("""
        INSERT INTO transaksi_pengeluaran_barang_detail
        (TrxOutIDF, TrxOutDProductIdf, TrxOutDQtyDus, TrxOutDQtyPcs)
        VALUES (%s, %s, %s, %s)
    """, (
        id_transaksi,
        product,
        qty_dus,
        qty_pcs
    ))

    db.commit()

    cursor.close()
    db.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)