import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

id_fauna = 10
jml_baru = 650

kursor.execute(f"UPDATE FAUNA SET jml_skrng = {jml_baru} WHERE id_fauna = {id_fauna}")
koneksi.commit()

if kursor.rowcount > 0:
    print(f"Data dengan ID {id_fauna} berhasil diubah")

else:
    print(f"Tidak ada data pegawai dengan ID {id_fauna}!")
    
koneksi.close()