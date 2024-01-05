import sqlite3

koneksi = sqlite3.connect('database_fauna.db')

delete_data = "DELETE FROM FAUNA WHERE asal='Kalimantan' "

koneksi.execute(delete_data)
koneksi.commit()
koneksi.close()