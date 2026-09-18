from supplier import tampilkan_supplier, tambah_supplier, ubah_supplier
from customer import tampilkan_customer, tambah_customer, ubah_customer
from product import tampilkan_product, tambah_product, ubah_product
from warehouse import tampilkan_warehouse, tambah_warehouse, ubah_warehouse

from penerimaan_header import tampilkan_penerimaan, tambah_penerimaan
from penerimaan_detail import tampilkan_detail_penerimaan, tambah_detail_penerimaan

from pengeluaran_header import tampilkan_pengeluaran, tambah_pengeluaran
from pengeluaran_detail import tampilkan_detail_pengeluaran, tambah_detail_pengeluaran

from stok import tampilkan_stok


while True:

    print("\n==============================")
    print("     SISTEM PERSEDIAAN BARANG")
    print("==============================")
    print("1. Data Supplier")
    print("2. Data Customer")
    print("3. Data Product")
    print("4. Data Warehouse")
    print("5. Penerimaan Barang")
    print("6. Pengeluaran Barang")
    print("7. Laporan Stok")
    print("0. Keluar")
    print("==============================")

    pilihan = input("Pilih menu: ")

    # =========================
    # SUPPLIER
    # =========================

    if pilihan == "1":

        print("\n=== MENU SUPPLIER ===")
        print("1. Tampilkan")
        print("2. Tambah")
        print("3. Ubah")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_supplier()

        elif pilih == "2":
            nama = input("Nama supplier: ")
            tambah_supplier(nama)

        elif pilih == "3":
            id_supplier = input("ID supplier: ")
            nama = input("Nama supplier baru: ")

            ubah_supplier(id_supplier, nama)


    # =========================
    # CUSTOMER
    # =========================

    elif pilihan == "2":

        print("\n=== MENU CUSTOMER ===")
        print("1. Tampilkan")
        print("2. Tambah")
        print("3. Ubah")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_customer()

        elif pilih == "2":
            nama = input("Nama customer: ")
            tambah_customer(nama)

        elif pilih == "3":
            id_customer = input("ID customer: ")
            nama = input("Nama customer baru: ")

            ubah_customer(id_customer, nama)


    # =========================
    # PRODUCT
    # =========================

    elif pilihan == "3":

        print("\n=== MENU PRODUCT ===")
        print("1. Tampilkan")
        print("2. Tambah")
        print("3. Ubah")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_product()

        elif pilih == "2":
            nama = input("Nama product: ")
            tambah_product(nama)

        elif pilih == "3":
            id_product = input("ID product: ")
            nama = input("Nama product baru: ")

            ubah_product(id_product, nama)


    # =========================
    # WAREHOUSE
    # =========================

    elif pilihan == "4":

        print("\n=== MENU WAREHOUSE ===")
        print("1. Tampilkan")
        print("2. Tambah")
        print("3. Ubah")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_warehouse()

        elif pilih == "2":
            nama = input("Nama warehouse: ")
            tambah_warehouse(nama)

        elif pilih == "3":
            id_warehouse = input("ID warehouse: ")
            nama = input("Nama warehouse baru: ")

            ubah_warehouse(id_warehouse, nama)


    # =========================
    # PENERIMAAN BARANG
    # =========================

    elif pilihan == "5":

        print("\n=== MENU PENERIMAAN BARANG ===")
        print("1. Tampilkan Header")
        print("2. Tambah Header")
        print("3. Tampilkan Detail")
        print("4. Tambah Detail")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_penerimaan()

        elif pilih == "2":

            no = input("No transaksi: ")
            warehouse = input("ID warehouse: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            supplier = input("ID supplier: ")
            catatan = input("Catatan: ")

            tambah_penerimaan(
                no,
                warehouse,
                tanggal,
                supplier,
                catatan
            )

        elif pilih == "3":
            tampilkan_detail_penerimaan()

        elif pilih == "4":

            transaksi = input("ID transaksi: ")
            product = input("ID product: ")
            qty_dus = input("Qty Dus: ")
            qty_pcs = input("Qty Pcs: ")

            tambah_detail_penerimaan(
                transaksi,
                product,
                qty_dus,
                qty_pcs
            )


    # =========================
    # PENGELUARAN BARANG
    # =========================

    elif pilihan == "6":

        print("\n=== MENU PENGELUARAN BARANG ===")
        print("1. Tampilkan Header")
        print("2. Tambah Header")
        print("3. Tampilkan Detail")
        print("4. Tambah Detail")

        pilih = input("Pilih: ")

        if pilih == "1":
            tampilkan_pengeluaran()

        elif pilih == "2":

            no = input("No transaksi: ")
            warehouse = input("ID warehouse: ")
            tanggal = input("Tanggal (YYYY-MM-DD): ")
            customer = input("ID customer: ")
            catatan = input("Catatan: ")

            tambah_pengeluaran(
                no,
                warehouse,
                tanggal,
                customer,
                catatan
            )

        elif pilih == "3":
            tampilkan_detail_pengeluaran()

        elif pilih == "4":

            transaksi = input("ID transaksi: ")
            product = input("ID product: ")
            qty_dus = input("Qty Dus: ")
            qty_pcs = input("Qty Pcs: ")

            tambah_detail_pengeluaran(
                transaksi,
                product,
                qty_dus,
                qty_pcs
            )


    # =========================
    # STOK
    # =========================

    elif pilihan == "7":

        tampilkan_stok()


    # =========================
    # KELUAR
    # =========================

    elif pilihan == "0":

        print("\nProgram selesai.")
        break

    else:

        print("\nPilihan tidak tersedia.")