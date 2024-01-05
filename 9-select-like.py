import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

nama = 'B%'
kursor.execute("SELECT *FROM FAUNA WHERE nama_fauna LIKE ?", (nama,))

baris_tabel = kursor.fetchall()

print('DATA FAUNA')
print("="*120)
print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format("ID  ", "NAMA FAUNA", "JENIS FAUNA", "ASAL FAUNA", "JUMLAH FAUNA", "TAHUN TERAKHIR DITEMUKAN"))
print("="*120)

# menampilkan data dengan perulangan
for baris in baris_tabel:
    print("{:<5} {:<20} {:<20} {:<20} {:<20} {:<10}".format(baris[0], baris[1], baris[2], baris[3], baris[4], baris[5]))
    
koneksi.close()