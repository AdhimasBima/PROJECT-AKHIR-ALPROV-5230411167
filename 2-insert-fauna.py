import sqlite3

conn = sqlite3.connect('database_fauna.db')
curr = conn.cursor()

input_nama = input("Masukkan Nama Fauna: ")
input_jenis = input('Masukkan Jenis Fauna: ')
input_asal = input("Masukkan Asal Fauna: ")
input_jumlah = input('Masukkan Jumlah Fauna Saat Ini: ')
input_tahun = input("Masukkan Tahun Terakhir Ditemukan: ")

insert_data = '''
             INSERT INTO FAUNA (nama_fauna, jenis, asal, jml_skrng, thn_ditemukan)
             VALUES (?,?,?,?,?)
'''

try: 
    curr.execute(insert_data, (input_nama, input_jenis, input_asal, input_jumlah, input_tahun))
    conn.commit()
    print("Data berhasil ditambahkan")
except Exception as e:
    print("Input Data Error!")
    
conn.close()